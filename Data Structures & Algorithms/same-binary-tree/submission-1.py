# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #the first case is if the roots are not the same then we return False
        #we need to rraverse the two trees either simulataneously or one after the othe
        #if we do one after the other we need to store the order at which they get visited

        if not p and not q:
            return True

        if (not p and q) or (p and not q):
            return False
            

        def dfs(node1, node2):
            if not node1 and not node2:
                return True

            if (not node1 and node2) or (node1 and not node2):
                return False
            
            if node1.val != node2.val:
                return False
            
            left = dfs(node1.left, node2.left)
            right = dfs(node1.right, node2.right)

            return left and right


            
        
        return dfs(p, q)
