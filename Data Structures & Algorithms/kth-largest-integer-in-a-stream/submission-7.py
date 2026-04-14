class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)
        for i in range(len(self.nums) - self.k):
            heapq.heappop(self.nums)
        #1, 2, 3, 3
        #3, 3
        #
        

    def add(self, val: int) -> int:
        
        heapq.heappush(self.nums, val)

        if len(self.nums) > self.k:
            heapq.heappop(self.nums)

        return self.nums[0]
        

        
