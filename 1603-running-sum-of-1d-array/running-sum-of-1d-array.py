class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = [0] * len(nums)
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            running_sum[i] = s
        return running_sum 