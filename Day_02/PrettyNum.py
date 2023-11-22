# https://www.codechef.com/problems/NUM239?tab=statement

# Iterate through each test case
for _ in range(int(input("Enter the number of test cases: "))):
    # Input: Range [L, R]
    L, R = map(int, input().split())

    # Initialize a counter for pretty numbers
    c = 0

    # Iterate through each number in the range [L, R]
    for i in range(L, R + 1):
        # Check if the last digit of the number is 2, 3, or 9
        if i % 10 in (2, 3, 9):
            # Increment the counter if the number is pretty
            c += 1

    # Output the count of pretty numbers for the current test case
    print(c)