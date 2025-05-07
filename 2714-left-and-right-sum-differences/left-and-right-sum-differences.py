class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        diff_arr = [0] * len(nums)
        leftSum = 0
        rightSum = sum(nums)

        for i in range(len(nums)):
            rightSum -= nums[i]
            diff_arr[i] = abs(rightSum -leftSum)
            leftSum += nums[i]

        return diff_arr
        