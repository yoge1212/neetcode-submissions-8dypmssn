# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        listOfNodes = []
        if not root:
            return []
        queue = deque([root])

        while queue:
            finalNode = queue[0]
            for i in range(len(queue)):
                currentNode = queue.popleft()
                finalNode = currentNode

                if currentNode.left:
                    queue.append(currentNode.left)

                if currentNode.right:
                    queue.append(currentNode.right)
            
            listOfNodes.append(finalNode.val)

        return listOfNodes
                
        #we need ot return the values of the nodes that are visible form the right side of the tree
        #queue = [1], [2]

        