"""
Check whether the input string is palindrome.
"""

def main():
    """Check palindrome."""
    s = input()
    mid = len(s)//2

    if s == s[::-1]:
        print("yes")
    else:
        print("no")

if __name__ == "__main__":
    main()
