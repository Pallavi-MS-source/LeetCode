class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        sum = 0
        ans = []
        for i in range (len(nums)):
            sum = sum + nums[i]
            ans. append(sum)
        return ans