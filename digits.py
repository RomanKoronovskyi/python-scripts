"""
Find sum of n-integer digits. n >= 0.
"""

def main():
    """Sum of number digits."""
    n = input()
    digit_sum = sum(int(digit) for digit in n)
    print(digit_sum) 

if __name__ == "__main__":
    main()
