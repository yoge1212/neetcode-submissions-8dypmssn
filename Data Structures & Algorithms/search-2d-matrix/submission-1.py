class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        #[[1, 2, 4, 8], [10, 11, 12, 13]]
        #matrix[0] = [1, 2, 4, 8]

        #
        for i in range(len(matrix)):
            left = 0
            right = len(matrix[i]) - 1

            while left <= right:
                mid = (left + right) // 2
                if matrix[i][mid] < target:
                    left = mid + 1
                elif matrix[i][mid] > target:
                    right = mid - 1
                else:
                    return True
            

        return False

        