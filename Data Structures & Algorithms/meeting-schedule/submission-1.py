"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        #[(0,30),(5,10),(15,20)]

        if not intervals:
            return True
        
        intervals.sort(key=lambda x: x.start)

        i = 1

        while i < len(intervals):
            current = intervals[i]
            prev = intervals[i-1]

            if current.start < prev.end:
                return False

            i += 1
            
        return True









































