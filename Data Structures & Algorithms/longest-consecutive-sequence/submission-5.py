class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #nums = {2: 1, 3: 2, 4: 3}
        #
        if nums == []:
            return 0
        consecutives = set(nums)
        #consecutives: {100, 4, 200, 1, 3, 2}
        
        highest = 0
        
        for num in consecutives:
            current = 1
            while num+current in consecutives:
                current += 1
            highest = max(highest, current)
            
        
        return highest
                




    
        

        