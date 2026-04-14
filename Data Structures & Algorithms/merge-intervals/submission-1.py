class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
       

        if not intervals:
            return []
        
        intervals.sort(key=lambda x: x[0])

        newArr = []

        current = intervals[0]
        
        i = 1
        while i < len(intervals):
            if current[1] < intervals[i][0]:
                newArr.append(current)
                current = intervals[i]

            elif current[0] > intervals[i][1]:
                newArr.append(intervals[i])

            else:
                current = [min(current[0], intervals[i][0]), max(current[1], intervals[i][1])]

            i += 1
        newArr.append(current)

        return newArr




         

        