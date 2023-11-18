#Chef classifies a day to be either rainy, cloudy, or clear.In a particular week, Chef finds X days to be rainy and Y days to be cloudy. Find the number of clear days in the week.

# Input: Number of rainy and cloudy days
X, Y = map(int, input().split())

# Calculate the number of clear days
clear_days = 7 - (X + Y)

# Output the result
print("Number of clear days:", clear_days)