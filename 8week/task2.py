"""https://leetcode.com/problems/find-all-anagrams-in-a-string/?envType=problem-list-v2&envId=sliding-window"""


class Solution(object):
    def findAnagrams(self, s, p):
        n = len(s)
        m = len(p)
        freq1 = [0] * 26
        for i in range(m):
            freq1[ord(p[i]) - 97] += 1
        res = []
        freq2 = [0] * 26
        ws = 0
        for we in range(n):
            freq2[ord(s[we]) - 97] += 1
            if we > m - 2:
                if freq1 == freq2:
                    res.append(ws)
                freq2[ord(s[ws]) - 97] -= 1
                ws += 1
        return res
