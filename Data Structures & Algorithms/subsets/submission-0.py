class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #im thinking of doing a double loop
        #and construting a new array within the inner loop
        ans = []
        for i in range(len(nums)):
            temp = [[nums[i]]]
            for j in range(i+1, len(nums)):


                old_len = len(temp)

                for k in range(old_len):
                    current = temp[k].copy()
                    current.append(nums[j])
                    temp.append(current)
                
            ans.extend(temp)



                
            
           
        ans.append([])
        return ans

        