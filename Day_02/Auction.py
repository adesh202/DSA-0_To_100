# https://www.codechef.com/problems/AUCTION?tab=statement

t=int(input())
for i in range (t):
    a,b,c=map(int, input().split())
    if a>b and a>c:
        print('ALICE')
    elif b>a and b>c:
        print('BOB')
    elif c>a and c>b:
        print("Charlie")