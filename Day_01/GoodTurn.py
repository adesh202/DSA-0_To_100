# Chef and Chefina are playing with dice. In one turn, both of them roll their dice at once. They consider a turn to be good if the sum of the numbers on their dice is greater than 6 Given that in a particular turn Chef and Chefina got X and Y on their respective dice, find whether the turn was good

# Input: Number of test cases
T = int(input())

# Run a loop for each test case
for i in range (T):
    # Input: Two space-separated integers for the current test case
    X, Y = map(int, input().split())
    if(X+Y>6):
        print("YES")
    else:
        print("NO")