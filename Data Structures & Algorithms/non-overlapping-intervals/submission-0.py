class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #first we sort the array
        #if the interval doest overlap we ignore otherwise we remove the new one

        if not intervals:
            return 0

        count = 0

        i = 1
        current = intervals[0]

        while i < len(intervals):
            if current[1] <= intervals[i][0]:
                current = intervals[i]
            
            elif current[0] >= intervals[i][1]:
                continue
            
            else:
                count += 1

            i += 1
        
        return count


        