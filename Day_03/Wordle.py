# https://www.codechef.com/problems/WORDLE?tab=statement

# Iterate through each test case
for _ in range(int(input("Enter the number of test cases: "))):
    # Input: Hidden word (S) and guess word (T)
    S = input()
    T = input()

    # Initialize the result string
    M = ''

    # Iterate through the characters of S and T
    for i in range(len(S)):
        # Check if the characters at the same index match
        if S[i] == T[i]:
            # If yes, add 'G' to the result string
            M += 'G'
        else:
            # If no, add 'B' to the result string
            M += 'B'

    # Output the result for the current test case
    print(M)