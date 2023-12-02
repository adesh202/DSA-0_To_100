# https://www.codechef.com/problems/MVR

a,b,x,y = map(int,input().split())
messi = a*2 + b
ronald = x*2 + y
if messi>ronald:
    print("Messi")
elif ronald>messi:
    print("Ronaldo")
else:
    print("Equal")