# https://leetcode.com/problems/sum-of-unique-elements/description/

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        k=[]
        sum=0
        for i in nums:
            k.append(nums.count(i))
        print(k)
        for i in range(len(k)):
            if k[i]==1:
                sum+=nums[i]
        return sum