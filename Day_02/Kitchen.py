# https://www.codechef.com/problems/KITCHENTIME?tab=statement

T=int(input())
for _ in range(T):
    X,Y=map(int,input().split())
    print(Y-X)