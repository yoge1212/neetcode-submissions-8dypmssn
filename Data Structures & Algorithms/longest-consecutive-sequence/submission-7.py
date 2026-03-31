class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_sequence = 0
        for num in nums:
            if num - 1 not in nums:
                counter = 1
                temp = num
                while temp + 1 in nums:
                    counter += 1
                    temp += 1
                max_sequence = max(counter, max_sequence)
                

        

        return max_sequence
            

        