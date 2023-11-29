# https://www.codechef.com/problems/AUDIBLE?tab=statement

t=int(input())
for i in range(t):
    x=int(input())
    if(x>=67 and x<=45000):
        print("YES")
    else:
        print("NO")