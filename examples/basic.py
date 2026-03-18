"""Basic usage example for katha."""
from src.core import Katha

def main():
    instance = Katha(config={"verbose": True})

    print("=== katha Example ===\n")

    # Run primary operation
    result = instance.generate(input="example data", mode="demo")
    print(f"Result: {result}")

    # Run multiple operations
    ops = ["generate", "create", "validate]
    for op in ops:
        r = getattr(instance, op)(source="example")
        print(f"  {op}: {"✓" if r.get("ok") else "✗"}")

    # Check stats
    print(f"\nStats: {instance.get_stats()}")

if __name__ == "__main__":
    main()
