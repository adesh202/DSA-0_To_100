# https://www.codechef.com/problems/PRACTICEPERF?tab=statement

# Taking input in the list
Q = list(map(int,input().split()))
# Counter 
W = 0
# Parsing the elements of list
for i in Q:
    # Comparing wether the value of i is > or = 10 if yes makes the counter +1
    if(i>=10):
        W +=1
print(W)