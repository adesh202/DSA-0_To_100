# https://www.codechef.com/problems/MAX_BIN?tab=statement

for _ in range(int(input())):
    n,k=map(int,input().split())
    s=input()
    lis=list(s)
    if(lis[0]=='0'):
        lis[0]='1'
        k-=1
    s1="".join(lis)
    print(s1+'0'*(k))