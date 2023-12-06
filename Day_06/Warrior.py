# https://www.codechef.com/problems/WARRIORCHEF

for i in range(int(input())):
    n,h=map(int,input().split())
    l=list(map(int,input().split()))
    l.sort()
    l.reverse()
    k=0
    for i in l:
        h-=i 
        if h<1:
            k=i
            break
    print(k)