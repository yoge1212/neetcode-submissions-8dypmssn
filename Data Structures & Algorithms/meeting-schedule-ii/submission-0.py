"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #we are given a array of meeting time interval objects with start and endtime properties
        #we need to find the minimum noumber of rooms required to schedule all meetings without any conflicts
        #intervals = [(0,40),(5,10),(15,20)]
        #1 room: (0, 40)
        #2 room: (5, 10), (15, 20)
        #first we sort the array
        #if the current one is in the range of the top of the stack
        #then we start a new room and add it to the stack
        #a 2d array stack
        #[[(0, 40)], [(5, 10), (15,20)]]
        #size of stack is 2 so 2 rooms no conflict
        
        stack = []
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x.start)

        for interval in intervals:
            if not stack:
                stack.append([interval])
            else:

                top_room = stack[-1]
                top_room_int = top_room[-1]

                if interval.start < top_room_int.end:
                    stack.append([interval])
                
                else:
                    stack[-1].append(interval)

        

        return len(stack)
        