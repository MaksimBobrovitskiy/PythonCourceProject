"""https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/submissions/1455986144/?envType=problem-list-v2&envId=sliding-window"""


class Solution:
    def longestSubstring(self, s, k):
        result = 0
        for T in range(1, len((s)) + 1):
            beg, end, Found, freq, MoreEqK = 0, 0, 0, [0] * 26, 0
            while end < len(s):
                if MoreEqK <= T:
                    s_new = ord(s[end]) - 97
                    freq[s_new] += 1
                    if freq[s_new] == 1:
                        MoreEqK += 1
                    if freq[s_new] == k:
                        Found += 1
                    end += 1
                else:
                    symb = ord(s[beg]) - 97
                    beg += 1
                    if freq[symb] == k:
                        Found -= 1
                    freq[symb] -= 1
                    if freq[symb] == 0:
                        MoreEqK -= 1

                if MoreEqK == T and Found == T:
                    result = max(result, end - beg)

        return result
