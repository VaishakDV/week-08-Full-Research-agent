from tavily import TavilyClient
import os
from dotenv import load_dotenv

load_dotenv()


class Tools:
    def __init__(self):
        self.tavily = TavilyClient(
            api_key=os.getenv("TAVILY_API_KEY")
        )

    def search_web(self, query):
        response = self.tavily.search(
            query=query,
            max_results=5
        )

        results = []
        for r in response["results"]:
            results.append({
                "title": r["title"],
                "url": r["url"],
                "content": r["content"]
            })

        return results

    def format_search_results(self, results):
        formatted = ""
        for i, r in enumerate(results, start=1):
            formatted += f"\n[{i}] {r['title']}\n"
            formatted += f"URL: {r['url']}\n"
            formatted += f"{r['content']}\n"
        return formatted


TOOL_DEFINITIONS = [
    {
        "name": "search_web",
        "description": "Search the internet for current information on any topic. Use this to find facts, news, data, and research.",
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The search query to look up"
                }
            },
            "required": ["query"]
        }
    }
]