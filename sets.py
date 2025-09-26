"""
Find common items in 2 lists without duplicates. Sort the result list before output.
"""

def main():
    """Find common numbers."""
    li1 = list(map(int, input().split()))
    li2 = list(map(int, input().split()))

    set1 = set(li1)
    set2 = set(li2)

    result = sorted(set1 & set2)
    print(result)

if __name__ == "__main__":
    main()
