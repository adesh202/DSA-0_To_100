# https://www.codechef.com/problems/HAPPYSTR?tab=submissions

t=int(input())
while t:
    s=input()
    k="Sad"
    for i in range(len(s)-2):
        if s[i] in {'a','e','i','o','u'}:
            if s[i+1] in {'a','e','i','o','u'}:
                if s[i+2] in {'a','e','i','o','u'}:
                    k="Happy"
                    break
    print(k)            
    t=t-1