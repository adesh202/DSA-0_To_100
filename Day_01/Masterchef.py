# Chef has been working hard to compete in MasterChef. He is ranked X out of all contestants. However, only 10 contestants would be selected for the finals. Check whether Chef made it to the top 10 or not?

for i in range (int(input())):
    R = int(input())
    if(R <= 10):
        print("YES")
    else:
        print("NO")