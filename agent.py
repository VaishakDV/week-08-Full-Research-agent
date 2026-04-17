import anthropic
import os
import json
from dotenv import load_dotenv
from tools import Tools, TOOL_DEFINITIONS

load_dotenv()

SYSTEM_PROMPT = """You are a research agent. Your job is to research topics thoroughly and produce well-structured reports.

When given a research topic:
1. Search for relevant information multiple times with different queries
2. Look for facts, statistics, recent developments, and key insights
3. Synthesise everything into a clear, structured report
4. Always cite your sources with URLs

Be thorough — search at least 3 times before writing your final report."""


class ResearchAgent:
    def __init__(self):
        self.client = anthropic.Anthropic(
            api_key=os.getenv("ANTHROPIC_API_KEY")
        )
        self.tools = Tools()
        self.max_iterations = 10

    def run(self, topic):
        print(f"\nResearching: {topic}")
        print("="*50)

        messages = [
            {"role": "user", "content": f"Research this topic and write a detailed report: {topic}"}
        ]

        iteration = 0

        while iteration < self.max_iterations:
            iteration += 1
            print(f"\n[Step {iteration}]")

            response = self.client.messages.create(
                model="claude-sonnet-4-6",
                max_tokens=8096,
                system=SYSTEM_PROMPT,
                tools=TOOL_DEFINITIONS,
                messages=messages
            )

            print(f"Stop reason: {response.stop_reason}")

            if response.stop_reason in("end_turn", "max_tokens"):
                final_answer = ""
                for block in response.content:
                    if hasattr(block, "text"):
                        final_answer += block.text
                print("\n" + "="*50)
                print("RESEARCH REPORT:")
                print("="*50)
                print(final_answer)
                return final_answer

            if response.stop_reason == "tool_use":
                messages.append({
                    "role": "assistant",
                    "content": response.content
                })

                tool_results = []
                for block in response.content:
                    if block.type == "tool_use":
                        print(f"Searching: {block.input['query']}")
                        results = self.tools.search_web(block.input["query"])
                        formatted = self.tools.format_search_results(results)

                        tool_results.append({
                            "type": "tool_result",
                            "tool_use_id": block.id,
                            "content": formatted
                        })

                messages.append({
                    "role": "user",
                    "content": tool_results
                })

        return "Max iterations reached."