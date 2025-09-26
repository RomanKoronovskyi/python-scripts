"""
Drop empty items from a dictionary.
"""
import json

def main():
    """Drop empty items from a dictionary."""
    d = json.loads(input())

    new_dict = {k: v for k, v in d.items() if v not in (None, "", [], {})}
    print(new_dict)

if __name__ == "__main__":
    main()
