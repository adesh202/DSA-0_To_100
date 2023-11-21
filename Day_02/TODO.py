# https://www.codechef.com/problems/TODOLIST?tab=statement

# Iterate through each test case
for i in range (int(input())):
    
    # Input: Number of problems (N)
    N = int(input())
    
    # Input: Difficulty ratings for each problem
    D = list(map(int, input().split()))
    
    # Initialize a counter to count problems with difficulty rating >= 1000
    counter = 0
    
    # Iterate through each difficulty rating and count problems to be removed
    for d in D:
        if d>=1000:
            counter +=1

    # Print the number of problems to be removed for the current test case
    print(counter)