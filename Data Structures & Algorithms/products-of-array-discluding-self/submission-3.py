class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #[1, 2, 8, 48]

        #[1, 48 ,24 ,6]


        answer = []
        prefix = [0] * len(nums)
        suffix = [0] * len(nums)

        for i in range(len(prefix)):
            if i == 0:
                prefix[i] = nums[i]
            else:
                prefix[i] = nums[i] * prefix[i-1]
        
        for i in range(len(suffix) - 1, -1, -1):
            if i == len(suffix) - 1:
                suffix[i] = nums[i]
            else:
                suffix[i] = nums[i] * suffix[i+1]
        
            
        print(prefix)
        print(suffix)

        for i in range(len(nums)):
            if i == 0:
                answer.append(suffix[i+1])
            
            elif i == len(nums) - 1:
                answer.append(prefix[i-1])
            
            else:
                answer.append(prefix[i-1] * suffix[i+1])
        
        return answer
    
        