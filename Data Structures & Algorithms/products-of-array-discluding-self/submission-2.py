class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #[1, 2, 8, 48]

        #[1, 48 ,24 ,6]


        answer = []
        prefix = [0] * len(nums)
        suffix = [0] * len(nums)

        for i in range(len(prefix)):
            if i == 0:
                prefix[i] == nums[i]
            else:
                prefix[i] == nums[i] * prefix[i-1]
        
        
            


        for i in range(len(nums)):
            if i == 0:
                answer.append(suffix[i+1])
            
            elif i == len(nums):
                answer.append(prefix[i-1])
            
            else:
                answer.append(prefix[i-1] * suffix[i+1])
        
        return answer
    
        