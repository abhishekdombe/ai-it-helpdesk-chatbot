import json
from pathlib import Path

DATA_FILE = Path(__file__).parent.parent / "data" / "faq.json"


def load_faqs(path=DATA_FILE):
    """Load the FAQ knowledge base from a JSON file."""
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def find_answer(question, faqs):
    """Return the answer whose keywords match the question, or None."""
    question = question.lower()
    for faq in faqs:
        if any(keyword in question for keyword in faq["keywords"]):
            return faq["answer"]
    return None


def main():
    faqs = load_faqs()
    print("🤖 IT Helpdesk Bot - type 'exit' to quit.")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ("exit", "quit"):
            print("Bot: Goodbye! 👋")
            break
        answer = find_answer(user_input, faqs)
        if answer:
            print(f"Bot: {answer}")
        else:
            print("Bot: Sorry, I don't know that yet. I'll create a ticket for a human agent.")


if __name__ == "__main__":
    main()