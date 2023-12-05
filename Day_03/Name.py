# https://www.codechef.com/problems/CALPOWER

n=int(input())
for i in range(n):
    S=list(sorted(input()))
    a=0
    z=1
    for i in range(0,len(S)):
        a=a+(z*(ord(S[i])-96))
        z+=1
    print(a)
        