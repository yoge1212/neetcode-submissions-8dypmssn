# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        smallest = 0
        counter = 0
        



        def dfs(node):
            nonlocal smallest
            nonlocal counter
            if not node:
                return
            
            left = dfs(node.left)
            counter += 1
            if counter == k:
                smallest = node.val
                return
            right = dfs(node.right)
        
        dfs(root)

        return smallest


        


        