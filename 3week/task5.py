"""https://leetcode.com/problems/pascals-triangle/submissions/1409814932/?envType=problem-list-v2&envId=array"""


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for _ in range(numRows - 1):
            dummy_row = [0] + ans[-1] + [0]
            row = []
            for i in range(len(ans[-1]) + 1):
                row.append(dummy_row[i] + dummy_row[i + 1])
            ans.append(row)
        return ans
