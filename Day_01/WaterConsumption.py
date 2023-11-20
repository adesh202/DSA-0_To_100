# Recently, Chef visited his doctor. The doctor advised Chef to drink at least 2000 ml of water each day. Chef drank X ml of water today. Determine if Chef followed the doctor's advice or not.

# Input: Number of test cases
for i in range (int(input())):
    W = int(input())
    # if water in take is less than 2000 print NO else Yes
    if(W >= 2000):
        print("YES")
    else:
        print("NO")