# https://www.codechef.com/problems/MINHEIGHT?tab=statement

for _ in range(int(input())):
    x,h = map(int,input().split())
    if x >= h:
        print('yes')
    else:
        print('no')