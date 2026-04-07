# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #we are give nthe roots of two binary treees ( root and subroot ),
        #we need to return true if there is a subtree of root with the same strucutre and node values
        #of subroot and false otherwise

        #we first dfs through root until we find the elemenent that equals the root of subroot
        #then we check to see if they are the same tree with another dfs
        
        def dfs(node) -> bool:
            if not node:
                return False

            left = dfs(node.left)
            right = dfs(node.right)

            if node.val == subRoot.val:
                return sameTree(node, subRoot)
            
            else:
                return left or right
        
        def sameTree(node1, node2) -> bool:
            if node1 and not node2:
                return False
            
            elif not node1 and node2:
                return False
            
            elif not node1 and not node2:
                return True
            
            left = sameTree(node1.left, node2.left)
            right = sameTree(node1.right, node2.right)

            return (node1.val == node2.val) and left and right
        
        return dfs(root)

