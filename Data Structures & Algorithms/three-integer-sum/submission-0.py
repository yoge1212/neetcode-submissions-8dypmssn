class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i, n in enumerate(nums):
            if i > 0 and n == nums[i-1]:
                continue

            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left+=1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    left += 1
        return ans