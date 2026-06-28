import os
from typing import Any
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

tavily_api_key = os.getenv("TAVILY_API_KEY")

if not tavily_api_key:
    raise ValueError("Missing TAVILY_API_KEY in .env file")

tavily_client = TavilyClient(api_key=tavily_api_key)


def internet_search(query: str, max_results: int = 2) -> list[dict[str, Any]]:
    """
    Search the internet for factual or up-to-date information.

    Use this tool when the user asks about current events, recent information,
    companies, technologies, people, documentation, or anything that may need
    external information.

    Args:
        query: The search query.
        max_results: Maximum number of search results to return.

    Returns:
        A list of search results containing title, url, and content.
    """

    response = tavily_client.search(
        query=query,
        max_results=max_results,
        include_raw_content=False,
    )

    results = response.get("results", [])

    clean_results = []

    for item in results:
        clean_results.append(
            {
                "title": item.get("title", ""),
                "url": item.get("url", ""),
                "content": item.get("content", ""),
            }
        )

    return clean_results

