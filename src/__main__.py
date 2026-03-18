"""CLI for katha."""
import sys, json, argparse
from .core import Katha

def main():
    parser = argparse.ArgumentParser(description="Katha — AI Indian Mythology Stories. AI-generated mythology stories from Ramayana, Mahabharata, and Puranas.")
    parser.add_argument("command", nargs="?", default="status", choices=["status", "run", "info"])
    parser.add_argument("--input", "-i", default="")
    args = parser.parse_args()
    instance = Katha()
    if args.command == "status":
        print(json.dumps(instance.get_stats(), indent=2))
    elif args.command == "run":
        print(json.dumps(instance.generate(input=args.input or "test"), indent=2, default=str))
    elif args.command == "info":
        print(f"katha v0.1.0 — Katha — AI Indian Mythology Stories. AI-generated mythology stories from Ramayana, Mahabharata, and Puranas.")

if __name__ == "__main__":
    main()
