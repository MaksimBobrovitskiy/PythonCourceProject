"""https://leetcode.com/problems/permutation-in-string/?envType=problem-list-v2&envId=sliding-window"""


class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False
        s1_freq = [0] * 26
        window_freq = [0] * 26
        for char in s1:
            s1_freq[ord(char) - ord("a")] += 1
        for i in range(len(s2)):
            window_freq[ord(s2[i]) - ord("a")] += 1
            if i >= len(s1):
                window_freq[ord(s2[i - len(s1)]) - ord("a")] -= 1
            if s1_freq == window_freq:
                return True
        return False
