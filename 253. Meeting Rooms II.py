class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort( key = lambda x : x[0] )
        rooms = []
        heapq.heapify( rooms )
        res = 0
        for interval in intervals:
            if len( rooms ) == 0:
                heapq.heappush( rooms, interval[1] )
            elif interval[0] >= rooms[0]:
                heapq.heappop( rooms )
                heapq.heappush( rooms, interval[1] )
            else:
                heapq.heappush( rooms, interval[1] )
        return len( rooms )