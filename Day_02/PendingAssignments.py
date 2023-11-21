# https://www.codechef.com/problems/ASSIGNMNT?tab=statement

# Iterate through each test case
for i in range(int(input())):
    
    # Input: Number of assignments (X), time to complete each assignment (Y), and number of days (Z)
    X, Y, Z = map(int, input().split())
    
    # Calculate total time required to complete all assignments (r) and total time available in minutes (n)
    r = X*Y
    
    n = Z*24*60 # Convert days to minutes (24 hours * 60 minutes)

    # Check if Chef can complete all assignments in Z days and print the result
    if(n>=r):
        print("YES")
    else:
        print("NO")