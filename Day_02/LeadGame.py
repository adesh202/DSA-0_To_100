# https://www.codechef.com/problems/TLG?tab=statement

# Input: Number of rounds
n = int(input())

# Initialize variables for cumulative scores and winning leads
play1 = play2 = max1 = max2 = 0

# Process each round
for _ in range(n):
    # Input: Scores for Player 1 and Player 2 in the current round
    a, b = map(int, input().split())

    # Update cumulative scores
    max1 += a
    max2 += b

    # Calculate the lead after the current round
    # Update the winning leads for each player
    if max1 > max2:
        play1 = max(play1, max1 - max2)
    else:
        play2 = max(play2, max2 - max1)

# Output the winner and winning lead
if play1 > play2:
    print(1, play1)
else:
    print(2, play2)