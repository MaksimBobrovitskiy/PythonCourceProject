"""https://leetcode.com/problems/path-sum-ii/?envType=problem-list-v2&envId=binary-tree"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, sm):
        def dfs(node, sm):
            if not node:
                return []
            if not node.left and not node.right and sm == node.val:
                return [[node.val]]

            lft = dfs(node.left, sm - node.val)
            rgh = dfs(node.right, sm - node.val)
            return [cand + [node.val] for cand in lft + rgh]

        return [s[::-1] for s in dfs(root, sm)]
