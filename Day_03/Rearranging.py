# https://www.codechef.com/problems/DIGARR?tab=submissions

t = int(input())
for i in range(t):
    N = int(input())
    C = 0
    D = int(input())
    while D > 0:
      K=D%10
      if K%5 == 0:C+=1
      D//=10
    if C==0:print("No")
    elif C>0:print("Yes")