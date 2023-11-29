# https://www.codechef.com/problems/TALLER?tab=submissions

for _ in range(int(input())):
    x,y = map(int,input().split())
    if x < y:
        print('b')
    else:
        print('a')