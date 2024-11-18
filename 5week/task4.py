"""https://leetcode.com/problems/majority-element-ii/?envType=problem-list-v2&envId=hash-table"""


class Solution:
    def majorityElement(self, nums):
        e1, n1, e2, n2 = None, 0, None, 0

        for v in nums:
            if e1 == v:
                n1 += 1
            elif e2 == v:
                n2 += 1
            elif n1 == 0:
                e1, n1 = v, 1
            elif n2 == 0:
                e2, n2 = v, 1
            else:
                n1, n2 = n1 - 1, n2 - 1

        n1, n2 = 0, 0
        for v in nums:
            if v == e1:
                n1 += 1
            elif v == e2:
                n2 += 1

        res = []
        if n1 > len(nums) // 3:
            res.append(e1)

        if n2 > len(nums) // 3:
            res.append(e2)

        return res
