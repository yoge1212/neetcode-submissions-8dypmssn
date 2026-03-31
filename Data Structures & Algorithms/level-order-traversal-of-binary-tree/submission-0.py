# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #bfs 
        #use a queue
        #at every root we add its children to the queue
        #and we can loop through this queue
        #and add the children to a new array
        #append the new array to the full list
        #then add their children

        if root is None:
            return []

        queue = collections.deque([root])
        result = []
        while queue:
            temp = []
            for i in range(len(queue)):
                node = queue.popleft()
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(temp)
        
        return result



        