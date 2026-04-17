from agent import ResearchAgent


def main():
    print("\n" + "="*50)
    print("     RESEARCH AGENT")
    print("="*50)
    print("Give me any topic and I'll research it for you.")
    print("Type 'quit' to exit.\n")

    agent = ResearchAgent()

    while True:
        topic = input("Research topic: ").strip()

        if not topic:
            continue

        if topic.lower() == "quit":
            print("\nGoodbye!")
            break

        agent.run(topic)
        print("\n" + "-"*50)


if __name__ == "__main__":
    main()