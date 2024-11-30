"""https://leetcode.com/problems/repeated-dna-sequences/?envType=problem-list-v2&envId=sliding-window"""


class Solution(object):
    def findRepeatedDnaSequences(self, s):
        map = {}
        res = []

        for i in range(len(s) - 9):
            substring = s[i : i + 10]
            if substring in map:
                if map[substring] == 1:
                    res.append(substring)
                map[substring] += 1
            else:
                map[substring] = 1

        return res
