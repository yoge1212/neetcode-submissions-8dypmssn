class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Prefix: [1, 1, 2, 6]
        #Suffix: [24,12,4,1]
        prefix = []
        suffix = [0 for i in range(len(nums))]

        answer = []

        prefixProduct = 1
        suffixProduct = 1

        for i in range(len(nums)):
            prefix.append(prefixProduct)
            prefixProduct = prefixProduct * nums[i]

        for i in range(len(nums)-1, -1, -1):
            suffix[i] = suffixProduct
            suffixProduct = suffixProduct * nums[i]
        
        for i in range(len(nums)):
            answer.append(prefix[i] * suffix[i])
        

        return answer