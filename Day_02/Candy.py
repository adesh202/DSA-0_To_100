# https://www.codechef.com/problems/CANDIVIDE?tab=statement

t = int(input())
for i in range(t):
    x = int(input())
    if (x % 3):
        print("NO")
    else:
        print("YES")