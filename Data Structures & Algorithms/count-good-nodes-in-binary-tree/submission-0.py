# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#a node is considered good if the path from the root node to itself 
#doesn't contain nodes with a value greater than the value of the node itself

#if the root is none we can return 0
#the root will always be a good node
#we perform dfs, but we keeep track of the highest number in the path
#at every node we check to see ifs null if it is we return 0
#otherwise we check to see if its a good node (< hgiest in path)
#if its good node we return 1 + left + right
#else return left + right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, maxVal) -> int:
            if not node:
                return 0
            
            if node.val < maxVal:
                left = dfs(node.left, maxVal)
                right = dfs(node.right, maxVal)
                return left + right
            else:
                left = dfs(node.left, node.val)
                right = dfs(node.right, node.val)
                return 1 + left + right
            



        
        return dfs(root, -math.inf)
            



        