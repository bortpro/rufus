# Rufus

Rufus is an AI agent designed to effectively crawl websites and return structured data as specified by the prompt. Running Rufus is as straightforward as appending your Rufus API key (and/or LLM key of choice) and prompting the agent to return relevant info you are interested in. Rufus will return the scraped information in JSON format within the variable 'documents', which can be passed along to a RAG system for further data processing.

Example usage:

```python
# Example usage matching the spec

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
```

Example response (printing output as example):

```
python3 rufus.py

--- Executing Fetch Node ---
--- (Fetching HTML from: https://www.withchima.com/sid) ---
--- Executing Parse Node ---
--- Executing GenerateAnswer Node ---
--- Executing SearchInternet Node ---
Search Query: product features site:www.withchima.com
--- Executing GraphIterator Node with batchsize 16 ---
processing graph instances:   0%|                                                                                                | 0/3 [00:00<?, ?it/s]--- Executing Fetch Node ---
--- (Fetching HTML from: https://www.withchima.com/chi-core) ---
--- Executing Fetch Node ---
--- (Fetching HTML from: https://www.withchima.com/terms-of-service) ---
--- Executing Fetch Node ---
--- (Fetching HTML from: https://www.withchima.com/case-study-hr-benefits-success) ---
--- Executing Parse Node ---
--- Executing GenerateAnswer Node ---
--- Executing Parse Node ---
--- Executing GenerateAnswer Node ---
--- Executing Parse Node ---
--- Executing GenerateAnswer Node ---
processing graph instances: 100%|████████████████████████████████████████████████████████████████████████████████████████| 3/3 [00:31<00:00, 10.35s/it]
--- Executing MergeAnswers Node ---
{
    "direct_scrape": {
        "product_features": {
            "Sid": {
                "overview": "Sid is the only fully integrated marketing AI platform, built for the enterprise.",
                "features": {
                    "Compound Human Reasoning": {
                        "Deep Intelligence": [
                            "Gain deeper insights into your market, customers, and competitors.",
                            "Generate comprehensive reports.",
                            "All sources of data and information are referenced.",
                            "Gather deep intelligence on targeted customers from all available sources of data including social media."
                        ],
                        "Create Content, Reports, Decks": [
                            "Generate highly personalized content for individual customers.",
                            "Create personalized pitch decks.",
                            "Create personalized marketing campaign content (image, video, text, audio).",
                            "Complete Request For Proposals (RFPs).",
                            "Update and optimize websites.",
                            "Create blogs based on customer intelligence.",
                            "Complete comprehensive case studies.",
                            "Create personalized newsletters."
                        ],
                        "Website Building and SEO Optimization": [
                            "Build and optimize websites for specific groups or individual customers.",
                            "SEO agent for continuous optimization to bring in organic traffic."
                        ],
                        "Marketing Strategist": [
                            "Gain strategic insights for product positioning.",
                            "Collect pricing data from the market.",
                            "Define product value proposition and strategize on positioning.",
                            "Collect intelligence on product placement to maximize revenue.",
                            "Develop promotion strategies."
                        ],
                        "Execute on Campaigns": [
                            "Autonomous BDRs reach out to qualified customers.",
                            "Autonomous digital specialists create content leveraging market trends.",
                            "Execute and track campaign performance."
                        ],
                        "Analytics: Learn and Optimize": [
                            "Create targeted and personalized content.",
                            "Track engagement metrics and optimize automatically.",
                            "Scale up outreach to achieve lead goals.",
                            "Gather intelligence about customer segments."
                        ]
                    }
                }
            }
        }
    },
    "search_results": {
        "product_features": {
            "AI-driven Knowledge Management": "Chima's suite of AI-driven knowledge management agents unifies internal data sources and streamlines complex tasks, such as verifying broker credentials and extracting essential coverage details.",
            "Integration with Existing Systems": "The system integrates seamlessly with existing Salesforce environments and leverages Slack-based interactions.",
            "Automated Data Retrieval": "The solution includes automated retrieval of SOS and SIC information, as well as real-time updates to reflect regulatory shifts.",
            "Generative AI, OCR, and Computer Vision": "The system uses generative AI, OCR, and computer vision models to extract and contextualize policy data from diverse carriers.",
            "Immediate, Tailored Responses": "Employees can ask complex questions in Slack and Salesforce and receive immediate, tailored responses.",
            "Streamlined Workflow": "The end-to-end workflow, from confirming broker arrangements to ensuring product compliance, is streamlined and transparent.",
            "Reduction in Internal Response Times": "Internal response time dropped by about 80%, from roughly 25 minutes per inquiry down to under 5 minutes.",
            "Substantial Time Savings": "The company projected approximately 12,500 hours saved annually.",
            "Cost Savings": "The organization saved an estimated $500,000 annually in labor costs.",
            "Faster Product Deployment": "The team could bring new or updated benefits products to market more quickly, improving product velocity.",
            "Chi Core": {
                "description": "Simplifies AI deployment and increases AI value realization by integrating AI into existing business and technology stacks.",
                "features": [
                    {
                        "name": "Internal Knowledge Base Q&A",
                        "description": "Provides real-time, precise answers to internal queries, boosting productivity and decision-making speed."
                    },
                    {
                        "name": "Knowledge Base Gap Identifier",
                        "description": "Scans and identifies gaps in the knowledge base to ensure continuous improvement and completeness."
                    },
                    {
                        "name": "Knowledge Base Gap Corrector",
                        "description": "Recommends and fills identified gaps in the knowledge base for comprehensive information coverage."
                    },
                    {
                        "name": "Customer Support Co-pilot",
                        "description": "Connects to customer databases to provide immediate, accurate responses, enhancing response quality and customer satisfaction."
                    },
                    {
                        "name": "Sales Co-pilot",
                        "description": "Enhances sales strategies with AI-driven insights and recommendations."
                    },
                    {
                        "name": "Ultimate AI Assistant",
                        "description": "Interfaces with third-party applications, manages tasks, and sources information to enhance team efficiency."
                    },
                    {
                        "name": "Autonomous Workflow Manager",
                        "description": "Oversees updates, tasks, and workflows autonomously, ensuring team-wide efficiency and productivity."
                    },
                    {
                        "name": "Effective Knowledge Sharing",
                        "description": "Organizes and surfaces key information from conversations and documents to foster informed collaboration."
                    }
                ]
            },
            "Platform": {
                "description": "Central space to deploy multiple cores across UIs, measure performance, fine-tune, and manage AI model providers.",
                "features": [
                    {
                        "name": "Seamless AI Integration",
                        "description": "Integrates AI into platforms like Slack and MS Teams, supporting diverse AI models and customized use cases."
                    },
                    {
                        "name": "Intelligent Operations and Feedback",
                        "description": "Automates processes and learns from user interactions, supporting diverse AI models and customized use cases."
                    },
                    {
                        "name": "Data Integration and Improvement",
                        "description": "Blends data pipelines and knowledge bases, identifies gaps, and enhances AI functionalities."
                    },
                    {
                        "name": "Analytics and Autonomous Optimization",
                        "description": "Provides in-depth analytics and allows AI to self-optimize for peak performance."
                    },
                    {
                        "name": "Secure and Efficient AI Management",
                        "description": "Ensures secure AI operations and cost management per user."
                    }
                ]
            },
            "Chima Technology": "The computer hardware, software, and other tangible equipment and intangible computer code necessary to deploy and make available the Site.",
            "Destination": "A type of technology application or platform to which the Site sends data.",
            "Event": "A record that the Site queries in a Source via a Sync and inserts (but does not update) in the Destination.",
            "Monthly Queried Records (MQR)": "The number of unique Records to be queried and analyzed by Chima Technology in a Source in a month.",
            "Object": "A record that the Site queries in a Source via a Sync and is then updated in a Destination.",
            "Operation": "An operation is one of an addition, deletion, or modification executed by the Site to a Destination. An addition, deletion, or modification typically consists of one or more application programming interfaces (API) calls made from the Site to a Destination.",
            "Source": "A data repository of Customer connected to the Site from which the Site reads data. An example of a Source is a Snowflake data warehouse or Google Sheet.",
            "Sync": "A process created by Customer in the Site that defines how and when data is activated using machine learning from Source to Destination by the Site.",
            "Third Party Systems": "A third party's web-based, mobile, or other software application that interoperates with the Site and is made available by Customer or a third party, including without limitation any Destination or Source."
        }
    },
    "combined_result": {
        "product_features": {
            "Sid": {
                "overview": "Sid is the only fully integrated marketing AI platform, built for the enterprise.",
                "core_capabilities": {
                    "Compound Human Reasoning": {
                        "Deep Intelligence": [
                            "Gain deeper insights into market, customers, and competitors",
                            "Generate comprehensive reports with referenced data sources",
                            "Gather intelligence from diverse sources including social media"
                        ],
                        "Content Creation": [
                            "Generate personalized content for individual customers",
                            "Create customized marketing materials (pitch decks, campaigns, blogs)",
                            "Complete complex documents like RFPs and case studies",
                            "Produce personalized newsletters tailored to specific audiences"
                        ],
                        "Web Presence Optimization": [
                            "Build and optimize websites for specific customer segments",
                            "Implement continuous SEO optimization for improved organic traffic"
                        ],
                        "Strategic Marketing": [
                            "Develop data-driven product positioning strategies",
                            "Collect and analyze market pricing data",
                            "Optimize product placement for maximum revenue",
                            "Create targeted promotion strategies"
                        ],
                        "Campaign Execution": [
                            "Deploy autonomous BDRs for customer outreach",
                            "Leverage market trends for content creation",
                            "Execute and monitor campaign performance metrics"
                        ],
                        "Analytics & Optimization": [
                            "Track engagement metrics with automatic optimization",
                            "Scale outreach activities to meet lead generation goals",
                            "Gather segment-specific customer intelligence"
                        ]
                    }
                },
                "integration_capabilities": {
                    "System Integration": "Seamlessly connects with existing business systems like Salesforce",
                    "Communication Platforms": "Integrates with platforms like Slack and MS Teams",
                    "Data Sources": "Connects to diverse data repositories including warehouses and spreadsheets"
                },
                "business_benefits": {
                    "Time Efficiency": "Reduces response times by up to 80%",
                    "Cost Reduction": "Saves significant labor costs through automation",
                    "Improved Productivity": "Streamlines workflows and enhances team collaboration",
                    "Faster Go-to-Market": "Accelerates product deployment and marketing velocity"
                },
                "technology_foundation": {
                    "AI Technologies": [
                        "Generative AI for content creation",
                        "OCR and computer vision for data extraction",
                        "Machine learning for process optimization"
                    ],
                    "Data Processing": "Intelligent querying and analysis of customer data sources",
                    "Security": "Enterprise-grade security and user management"
                }
            }
        }
    }
},

    "metadata": {
        "source_url": "https://www.withchima.com/sid",
        "instructions": "Find information about product features.",
        "search_performed": true,
        "timestamp": "2025-03-05T18:28:32.815618"
    }
}
```

## Rufus High Level Overview: Two-Tier Web Scraping Approach

This implementation of Rufus involves a two-tier scraping system that intelligently extracts relevant information from websites based on user instructions.

First Tier: Direct Scraping

The first tier uses SmartScraperGraph (using the library scrapegraphai) to directly scrape the target URL. This approach:

    Analyzes the webpage content based on the user's instructions

    Extracts structured data from the page's HTML

    Formats the information into a clean JSON structure

    Works well for static content and well-structured pages, as well as nested pages

Second Tier: Search-Based Scraping

If the first tier doesn't yield sufficient data (contains "NA" values or returns less than 200 characters), Rufus automatically falls back to a second tier using SearchGraph. This approach:

    Performs a web search related to the user's instructions and the target domain

    Constructs a graph of nodes based on the web search related to the target domain for scraping

    Gathers information from search results rather than just the direct page

    Helps overcome limitations in edge cases when content is dynamically loaded or hidden behind JavaScript in particularly troublesome cases

    Provides additional context that might not be directly accessible on the target page, which can boost scope and interpretation (this happens in the case for Chima's product Sid!)


The documents variable returned by client.scrape() contains a comprehensive JSON structure with:

    direct_scrape: Results from the first-tier direct scraping

    search_results: Results from the second-tier search-based scraping (null if not performed)

    combined_result: The synthesized data

    metadata: Additional information including:

        source_url: The original URL that was scraped

        instructions: The user's original instructions

        search_performed: Boolean indicating whether the second tier was used

        timestamp: When the scraping was performed

This structured output makes it easy to integrate Rufus into RAG (Retrieval-Augmented Generation) pipelines, as the data is already formatted for immediate use by language models. This intuitive API-response paradigm is also in line with higher level system design in mind, as it returns several JSON objects of interest. It returns the individual efforts of both tiers of scraping as well as the synthesized, AI powered understanding of both scraping efforts (using the best of both worlds). Error-handling is accounted for within Rufus, checking for cases where no results were returned from a search/URL. If sufficient information (defined by a character limit) is gained by the first tier approach, Rufus efficiently only runs the first tier of scraping.

## Challenges and Limitations:

While Rufus did a great job with government websites, Chima's website, and well documented products like https://www.notion.com/product/docs, niche cases with more recent company products with ill formatted or hidden elements/images could pose problems with the current approach. Recently launched startups (for example https://flairlabs.ai/#hero-home) could pose problems to the failsafe of constructing a graph of web searches, simply because there was not enough information disseminated from the web yet for recently formulated startups. Further improvements could include dynamic browser use and OpenAI Operator style use of the browser incorporating computer vision/OCR to check for information in these edge cases.
