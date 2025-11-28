# Medium
# Insert Interval

# You are given an array of non-overlapping intervals intervals 
# where intervals[i] = [starti, endi] represent the start and the end of the ith interval 
# and intervals is sorted in ascending order by starti. 
# You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals 
# (merge overlapping intervals if necessary).
# Return intervals after the insertion.
# Note that you don't need to modify intervals in-place. You can make a new array and return it.

# Input: intervals = [[1,3],[6,9]],                       newInterval = [2,5]             Output: [[1,5],[6,9]]
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]],  newInterval = [4,8]             Output: [[1,2],[3,10],[12,16]]

# Edge cases        : 
# Time Complexity   : 
# Space complexity  : 
# Best case         : 
# Worst Case        : 
########################################################################
class Solution:
    def insert(self, intervals:list[list[int]], newInterval:list[int])->list[list[int]]:
        if not intervals:
            return newInterval
        i = 0
        n = len(intervals)
        res = []

        while i < n and (intervals[i][1] < newInterval[0]):
            res.append(intervals[i])
            i = i + 1
        
        while i < n and (intervals[i][0] <= newInterval[1]):
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i = i + 1
        res.append(newInterval)
        
        while i < n:
            res.append(intervals[i])
            i = i + 1
        return  res

if __name__ == "__main__":
    intervals = [[1,3],[6,9]]
    newInterval = [2,5]
    print(Solution().insert(intervals, newInterval))

    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [4,8]
    print(Solution().insert(intervals, newInterval))






