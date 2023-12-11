# https://www.codechef.com/problems/WAV2

from bisect import bisect_left
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

n, q = map(int, input().split())
nums = set(map(int, input().split()))
nums = sorted(nums)

queries = []
for qq in range(q):
    queries.append(int(input()))

for qq in queries:
    if binary_search(nums, qq):
        print(0)
    else:
        pos = bisect_left(nums, qq)
        print("POSITIVE" if (n - pos) % 2 == 0 else "NEGATIVE")