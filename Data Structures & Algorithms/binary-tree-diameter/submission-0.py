# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #the diameter is the max height of the left tree and the right tree of every node
        #we test this for every node of tree till we get a max

        if not root:
            return 0

        maxDiam = -math.inf

        def dfs(node):
            nonlocal maxDiam
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if left + right > maxDiam:
                maxDiam = left + right
            
            return 1 + max(left, right)
        
        dfs(root)
        return maxDiam

        
        