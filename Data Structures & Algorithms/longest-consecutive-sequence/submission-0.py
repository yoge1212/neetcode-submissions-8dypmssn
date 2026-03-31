class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #nums = {2: 1, 3: 2, 4: 3}
        #
        consecutives = {}
        highest = 0
        for num in sorted(nums):
            consecutives[num] = consecutives.get(num-1, 0) + 1

        for streak in consecutives:
            if consecutives[streak] > highest:
                highest = consecutives[streak]
        
        return highest

        

        