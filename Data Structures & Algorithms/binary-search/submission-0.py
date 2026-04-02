class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        mid = int((left + right) / 2)

        while nums[mid] != target:
            if nums[mid] < target:
                left = mid
            else:
                right = mid
            mid = int((left + right) / 2)

            if mid == left or mid == right:
                return -1

        return mid   