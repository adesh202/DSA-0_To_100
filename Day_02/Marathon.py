# https://www.codechef.com/problems/OCTATHON

x=int(input())
if(x<3):
    print('gold')
elif(x>=3 and x<6):
    print("silver")
else:
    print("bronze")