import json
import os
import datetime
from scrapegraphai.graphs import SmartScraperGraph, SearchGraph

class RufusClient:
    def __init__(self, api_key=None, model="openai/gpt-4o", verbose=True, headless=True):
        self.config = {
            "llm": {
                "api_key": api_key,
                "model": model,
            },
            "verbose": verbose,
            "headless": headless,
        }

    def _format_prompt(self, instructions):
        """Format user instructions into a detailed prompt for the scraper"""
        return f"""Based on these instructions: '{instructions}',
        extract all relevant information from the webpage.
        Be comprehensive and specific, capturing all concrete details.
        Format the output as a structured JSON with appropriate fields.
        If information is missing or unclear, indicate this in your response."""

    def _is_sufficient_data(self, result):
        """Check if the scraped data is sufficient"""
        # Convert result to string to check its length
        result_str = json.dumps(result)

        # Check if result contains NA values or is too short
        has_na = "NA" in result_str
        is_short = len(result_str) < 20000

        return not (has_na or is_short)

    def scrape(self, url, instructions):
        """Scrape website based on user instructions"""
        import datetime
        import json
        import requests

        formatted_prompt = self._format_prompt(instructions)

        # First tier: Try direct scraping
        smart_scraper = SmartScraperGraph(
            prompt=formatted_prompt,
            source=url,
            config=self.config
        )

        direct_result = smart_scraper.run()

        # Initialize search_result as empty or None
        search_result = None

        # Check if direct scraping provided sufficient data
        if not self._is_sufficient_data(direct_result):
            # Second tier: Use search-based scraping
            domain = url.split("//")[1].split("/")[0]  # Extract just the domain
            search_prompt = f"Find and summarize information about {instructions} from {domain}. Be specific about all the concrete facts."

            search_graph = SearchGraph(
                prompt=search_prompt,
                config=self.config
            )

            # Add error handling for search
            try:
                search_result = search_graph.run()
            except ValueError as e:
                search_result = {"error": str(e), "message": "Search returned no results"}

        # Create combined result
        if search_result and not isinstance(search_result, dict) or \
           (isinstance(search_result, dict) and not search_result.get("error")):
            # If we have both direct and search results, use LLM to synthesize them
            synthesis_prompt = {
                "model": self.config["llm"]["model"].split("/")[1],
                "messages": [
                    {
                        "role": "system",
                        "content": "You are an AI assistant that synthesizes information from multiple sources into a coherent, structured JSON document."
                    },
                    {
                        "role": "user",
                        "content": f"""Synthesize the following information into a single, comprehensive JSON document that addresses: {instructions}

                        DIRECT SCRAPE RESULTS:
                        {json.dumps(direct_result, indent=2)}

                        SEARCH RESULTS:
                        {json.dumps(search_result, indent=2)}

                        Return ONLY a valid JSON object with the synthesized information, structured in a logical way that combines insights from both sources.
                        """
                    }
                ]
            }

            # Call the OpenAI API to synthesize the results
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.config['llm']['api_key']}"
            }

            response = requests.post(
                "https://api.openai.com/v1/chat/completions",
                headers=headers,
                json=synthesis_prompt
            )

            try:
                combined_result = json.loads(response.json()["choices"][0]["message"]["content"])
            except (KeyError, json.JSONDecodeError):
                # Fallback if synthesis fails
                combined_result = {
                    "synthesized_data": "Synthesis failed",
                    "direct_data": direct_result,
                    "search_data": search_result
                }
        else:
            # If we only have direct results, use those
            combined_result = direct_result

        # Get current timestamp in ISO format
        current_timestamp = datetime.datetime.now().isoformat()

        # Always return all three components
        return {
            "direct_scrape": direct_result,
            "search_results": search_result,
            "combined_result": combined_result,
            "metadata": {
                "source_url": url,
                "instructions": instructions,
                "search_performed": search_result is not None,
                "timestamp": current_timestamp
            }
        }


# Example usage matching the case study spec
if __name__ == "__main__":
    # Get API key from environment variable (or use your hardcoded key for testing)
    api_key = os.getenv('RUFUS_API_KEY')

    # Initialize client
    client = RufusClient(api_key=api_key)

    # Define instructions and URL
    instructions = "Find information about product features."
    url = "https://www.withchima.com/sid"

    # Execute scraping
    documents = client.scrape(url, instructions)

    # Print results
    print(json.dumps(documents, indent=4))

    # If you would like to then feed in the JSON formatted data into a RAG pipeline, pass in documents.
    # return documents
