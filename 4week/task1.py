"""https://leetcode.com/problems/maximum-subarray/description/"""


class Solution(object):
    def maxSubArray(self, nums):
        ans = nums[0]
        minx = 0
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            ans = max(ans, s - minx)
            minx = min(minx, s)
        return ans
