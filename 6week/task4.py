"""https://leetcode.com/problems/minimum-size-subarray-sum/?envType=problem-list-v2&envId=sliding-window"""


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        j = 0
        s = 0
        mn = 10**10
        while j < len(nums):
            s += nums[j]
            while s >= target:
                s -= nums[i]
                mn = min(j - i + 1, mn)
                i += 1
            j += 1
        if mn == 10**10:
            return 0
        return mn
