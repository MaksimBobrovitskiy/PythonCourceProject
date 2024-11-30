"""https://leetcode.com/problems/find-k-closest-elements/?envType=problem-list-v2&envId=sliding-window"""


class Solution(object):
    def findClosestElements(self, arr, k, x):
        N = len(arr)
        l, r = 0, N - 1
        while l < r:
            mid = l + (r - l) // 2
            if mid + k < N and (x - arr[mid] > arr[mid + k] - x):
                l = mid + 1
            else:
                r = mid
        return arr[r : r + k]
        N = len(arr)
        j = 0
        res = []
        for i in range(N - k + 1):
            while j < N and j - i < k:
                res.append(arr[j])
                j += 1
            if (
                j == N
                or (abs(arr[j] - x) > abs(arr[i] - x))
                or ((abs(arr[j] - x) == abs(arr[i] - x)) and arr[j] > arr[i])
            ):
                return res
            res.pop(0)
        return res
