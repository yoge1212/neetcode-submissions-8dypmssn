class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #og: [1, 2, 3, 4]
        #Prefix: [1, 2, 6, 24]
        #Postfix:[24, 24, 12, 4]
        #[24, 12, 8, 6]
        prefix = []
        postfix = [0 for i in range(len(nums))]

        answer = []

        prefixProduct = 1
        postfixProduct = 1
        for num in nums:
            prefixProduct = prefixProduct * num
            prefix.append(prefixProduct)
            
        for i in range(len(nums)-1, -1, -1):
            postfixProduct = postfixProduct * nums[i]
            postfix[i] = postfixProduct
           
        
        for i in range(len(nums)):
            if i == len(nums)-1:
                answer.append(prefix[i-1])
            elif i == 0:
                answer.append(postfix[i+1])

            else:
                answer.append(prefix[i-1] * postfix[i+1])
        

        return answer