class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #we are given an array of integers 
        #is sorted in non-decreasing order (so increasing?)

        #we need to return the indices of two numbers [idx1, idx2]
        #such that they add up to a given target number target
        #and idx1 < idx2
        #also the two numbers cannot be equal (does mean no duplicates and only index cannot be the same)
        #i am curious if there can be duplicates or not

        left = 0 
        right = len(numbers) - 1

        while left < right:
            if numbers[left] + numbers[right] == target and left < right:
                return [left + 1, right + 1]
            
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1
        
        return []
        