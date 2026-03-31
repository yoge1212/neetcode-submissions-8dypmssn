# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#so we need to compute the height of the left and right subtrees
#if the diffence in ehights abs(right - left) is no more than 1 its valid
#do dfs based approach recursivelt
#if node is none -> return 0
#left
#right
#node
#return 1 + left + right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBalanced = True
        def dfs(node):
            nonlocal isBalanced
            
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            if abs(right - left) > 1:
                isBalanced = False


            return 1 + max(left, right)
        
        dfs(root)

        return isBalanced



        