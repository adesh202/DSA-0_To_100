def P(lst1,lst2):
    if(lst1.count(1)==lst2.count(1)):
        print("YES")
    else:
        print("NO")
for _ in range(int(input())):
    x=int(input())
    lst1=list(map(int,str(int(input()))))
    lst2=list(map(int,str(int(input()))))
    P(lst1,lst2)
    