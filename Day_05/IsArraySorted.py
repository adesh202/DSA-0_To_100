# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/

from ast import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        for i in range (len(nums)):
            if nums == sorted(nums):
                return True
            nums= nums[1 : ] + [nums[0]]
        return False