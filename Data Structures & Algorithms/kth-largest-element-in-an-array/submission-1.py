class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = []
        for num in nums:
            heapq.heappush(maxHeap, num)
        
        for i in range(len(maxHeap) - k):
            heapq.heappop(maxHeap)

        return maxHeap[0]

        