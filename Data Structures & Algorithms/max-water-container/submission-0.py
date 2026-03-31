class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxArea = 0
        while left < right:
            shorter = min(height[left], height[right])
            area = (right - left) * shorter
            if area > maxArea:
                maxArea = area
            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1

            else:
                left+= 1
        
        return maxArea
        