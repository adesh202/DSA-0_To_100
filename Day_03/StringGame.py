t = int(input())
for i in range(t):
    n = int(input())
    s = str(input())
    
    for i in set(s):
        if s.count(i)%2 != 0:
            print('NO')
            break
    else:
        print('YES')