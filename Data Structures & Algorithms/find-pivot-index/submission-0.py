class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftArr = []
        rightArr = [0] * len(nums)
        previousSum = 0
        afterSum = 0
        for i in range(len(nums)):
            leftArr.append(nums[i] + previousSum)
            previousSum += nums[i]
        
        for i in range(len(nums) -1, -1, -1):
            rightArr[i] = nums[i] + afterSum;
            afterSum += nums[i]

        print(leftArr)
        print(rightArr)

        for i in range(len(nums)):
            if leftArr[i] == rightArr[i]:
                return i
        
        return -1
