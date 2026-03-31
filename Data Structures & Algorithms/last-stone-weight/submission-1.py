class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        #we heapify the stones array to a max heap
        #we gpo through a while loop while the array len is greater than 1
        #at each steap we pop 2 times
        #if equal do nothing otherwise we add a new stone with the weight of y-x
        
        maxHeap = []
        for stone in stones:
            heapq.heappush(maxHeap, -stone)
        

        
        while len(maxHeap) > 1:
            x = abs(heapq.heappop(maxHeap))
            y = abs(heapq.heappop(maxHeap))

            if x != y:
                heapq.heappush(maxHeap, -(x-y))
                
        
        if maxHeap:
            return abs(maxHeap[0])
        else:
            return 0

        