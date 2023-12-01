# https://www.codechef.com/problems/DETSCORE?tab=statement

t=int(input())
for i in range(t):
    x,n=map(int,input().split())
    c=x//10
    print(c*n)
