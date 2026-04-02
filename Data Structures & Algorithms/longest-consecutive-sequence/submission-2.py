class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #nums = {2: 1, 3: 2, 4: 3}
        #
        consecutives = set(nums)
        #consecutives: {2, 3, 4, 5, 10, 20, 21, 22, 23, 24, 25}
        highest = 1
        current = 1
        
        for num in consecutives:
            if num-1 in consecutives:
                current += 1
                if current > highest:
                    highest = current
            else:
                current = 1
            
        
        return highest
                




     
        return streak

        

        