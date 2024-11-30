"""https://leetcode.com/problems/binary-subarrays-with-sum/?envType=problem-list-v2&envId=sliding-window"""


class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        length = len(nums)
        count = 0
        prefix_sum = 0
        prefixes = [0] * (length + 2)
        for i in range(length):
            if nums[i] > 0:
                prefix_sum += nums[i]
                prefixes[prefix_sum] = i + 1
            i += 1
        prefixes[prefix_sum + 1] = length + 1
        total_sum = prefix_sum
        prefix_sum = goal
        while prefix_sum <= total_sum:
            zero1 = prefixes[prefix_sum - goal + 1] - prefixes[prefix_sum - goal] - 1
            if goal > 0:
                zero2 = prefixes[prefix_sum + 1] - prefixes[prefix_sum] - 1
                count += (zero1 + 1) * (zero2 + 1)
            else:
                count += zero1 * (zero1 + 1) // 2
            prefix_sum += 1
        return count
