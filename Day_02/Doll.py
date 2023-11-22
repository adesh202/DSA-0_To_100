# https://www.codechef.com/problems/DOLL

for _ in range (int(input())):
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    c = 0
    for i in H:
        if i>K:
            c +=1
    print(c)