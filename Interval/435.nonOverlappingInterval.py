# Medium
# Non-overlapping Intervals

# Given an array of intervals intervals where intervals[i] = [starti, endi], 
# return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
# Note that intervals which only touch at a point are non-overlapping. 
# For example, [1, 2] and [2, 3] are non-overlapping.

# Input: intervals = [[1,2],[2,3],[3,4],[1,3]]            Output: 1   [1,3] can be removed 
# Input: intervals = [[1,2],[1,2],[1,2]]                  Output: 2   remove two [1,2] 
# Input: intervals = [[1,2],[2,3]]                        Output: 0   don't need to remove 

# Edge cases        : 
# Time Complexity   : 
# Space complexity  : 
# Best case         : 
# Worst Case        : 
########################################################################
class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        n = len(intervals)
        prev = 0
        count = 1

        for i in range(1,n):
            if intervals[i][0] >= intervals[prev][1]:
                prev = i
                count = count + 1
        return (n - count)

if __name__ == "__main__":
    intervals = [[1,2],[2,3],[3,4],[1,3]]
    print(Solution().eraseOverlapIntervals(intervals))

    intervals = [[1,2],[1,2],[1,2]]
    print(Solution().eraseOverlapIntervals(intervals))

    intervals = [[1,2],[2,3]]
    print(Solution().eraseOverlapIntervals(intervals))