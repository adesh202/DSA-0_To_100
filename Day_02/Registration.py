# https://www.codechef.com/problems/COURSEREG

# Iterate through each test case
for i in range (int(input())):
    N, M, K = map(int, input().split())
    if(N+K<=M):
        print("YES")
    else:
        print("No")