# https://www.codechef.com/problems/RECENTCONT?tab=statement

# Iterate through each test case
for _ in range(int(input())):
    # Input: Total count of problems (M) and the list of contest codes (N)
    M = int(input())
    N = list(input().split())

    # Initialize counters for each contest
    S38 = L108 = 0

    # Iterate through each contest code in the list
    for i in N:
        # Count the occurrences of "START38" and "LTIME108"
        if i == 'START38':
            S38 += 1
        elif i == 'LTIME108':
            L108 += 1

    # Output the count of problems in each contest for the current test case
    print(S38, L108)