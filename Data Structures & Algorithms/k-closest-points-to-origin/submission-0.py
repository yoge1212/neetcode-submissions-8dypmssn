class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distanceToPoint = defaultdict(list)
        minHeap = []
        closest = []

        for i in range(len(points)):
            currentPoint = points[i]
            distance = math.sqrt((0 - currentPoint[0])**2 + (0 - currentPoint[1])**2)
            distanceToPoint[distance].append(currentPoint)
            heapq.heappush(minHeap, distance)
        counter = 0
        while counter < k:
            minDist = heapq.heappop(minHeap)
            for point in distanceToPoint[minDist]:
                if not counter < k:
                    break
                closest.append(point)
                counter += 1
        
        return closest


        


        