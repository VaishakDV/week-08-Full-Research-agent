# Week 08 - Research Agent

An autonomous research agent that searches the web multiple 
times, synthesises information, and produces cited reports.

## What it does
- Takes any research topic as input
- Autonomously decides what to search and how many times
- Uses Tavily Search API for clean web results
- Synthesises findings into a structured report with citations
- Stops when it has enough information — not when told to

## What I learned
- Tool use / function calling in the Anthropic API
- The ReAct pattern — Reason, Act, Observe, repeat
- How agents differ from chatbots — action vs text only
- Tool definitions — how Claude knows what tools exist
- Agent loops with iteration limits for safety
- Handling multiple stop reasons — end_turn vs tool_use vs max_tokens
- hasattr() — safely accessing object attributes
- Why agents need stronger models (Sonnet vs Haiku)

## How the agent thinks
1. Receives research topic
2. Thinks — what should I search first?
3. Searches — calls search_web tool
4. Reads — observes results
5. Thinks — what am I missing?
6. Repeats until satisfied
7. Writes final cited report

## Tech Stack
- Claude Sonnet (stronger reasoning for agent decisions)
- Tavily Search API (clean web results for AI agents)
- ReAct pattern (Reason + Act loop)

## How to run
1. Clone the repo
2. Create virtual environment and activate it
3. pip install anthropic python-dotenv tavily-python
4. Create .env with ANTHROPIC_API_KEY and TAVILY_API_KEY
5. python main.py
6. Enter any research topic
