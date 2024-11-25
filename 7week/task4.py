"""https://leetcode.com/problems/new-21-game/?envType=problem-list-v2&envId=sliding-window"""


class Solution(object):
    def new21Game(self, n, k, maxPts):
        if k == 0 or n >= k + maxPts:
            return 1

        dp = [1.0] + [0.0] * n
        maxPts_sum = 1.0
        for i in range(1, n + 1):
            dp[i] = maxPts_sum / maxPts
            if i < k:
                maxPts_sum += dp[i]

            if i - maxPts >= 0:
                maxPts_sum -= dp[i - maxPts]

        return sum(dp[k:])
