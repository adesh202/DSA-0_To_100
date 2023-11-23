# https://www.codechef.com/problems/PALL01

# Function to check if a string is a palindrome
def is_palindrome(num):
    return num == num[::-1]

# Iterate through each test case
for _ in range(int(input("Enter the number of test cases: "))):
    # Input: A string or number N
    N = input()

    # Check if N is a palindrome using the is_palindrome function
    result = is_palindrome(N)

    # Output the result for the current test case
    if result:
        print("wins")
    else:
        print("loses")