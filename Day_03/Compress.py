# https://www.codechef.com/problems/COMPRESSVD?tab=statement

for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    m=1
    for j in range(0,n-1):
        if a[j]!=a[j+1]:
            m+=1
    print(m)