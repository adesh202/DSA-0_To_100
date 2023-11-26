# https://www.codechef.com/problems/TTENIS?tab=statement

t=int(input())
while t>0:
    s=input()
    c0,c1=0,0
    c0=s.count('0')
    c1=s.count('1')
    if c0>c1:
        print("LOSE")
    else:
        print("WIN")
    t=t-1