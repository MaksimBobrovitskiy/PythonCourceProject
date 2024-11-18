"https://leetcode.com/problems/bulls-and-cows/?envType=problem-list-v2&envId=hash-table"


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        raj = [0] * 10

        for i in range(len(secret)):
            sec = int(secret[i])
            gu = int(guess[i])

            if sec == gu:
                bulls += 1
                continue
            if raj[sec] < 0:
                cows += 1
            if raj[gu] > 0:
                cows += 1
            raj[sec] += 1
            raj[gu] -= 1

        return f"{bulls}A{cows}B"
