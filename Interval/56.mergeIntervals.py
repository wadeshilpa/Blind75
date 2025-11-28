# Medium
# Merge Intervals
# Sorting + Greedy Interval Merging

# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]        Output: [[1,6],[8,10],[15,18]]
# Input: intervals = [[1,4],[4,5]]                       Output: [[1,5]]
# Input: intervals = [[4,7],[1,4]]                       Output: [[1,7]]
# Input: intervals = [[1,4],[2,3]]                       Output: [[1, 4]]

# Edge cases        : empty, single interval, negative numbers, non-overlapping, touching intervals
# Time Complexity   : O(n log n) + O(n) + O(1)
# Space complexity  : O(n) for merged output
# Best case         : 
# Worst Case        : 
########################################################################
class Solution:
    def mergeIntervals(self, intervals: list[list[int]]) -> list[list[int]]:
        if not intervals:
            return []
        
        intervals.sort() 
        prev = intervals[0]
        merged = []

        for i in range(1, len(intervals)):
            if intervals[i][0] <= prev[1]:
                prev[1] = max(prev[1], intervals[i][1])   #MAX for edge case - [[1,4],[2,3]]
            else:
                merged.append(prev)
                prev = intervals[i]
        merged.append(prev)
        return merged
if __name__ == "__main__":
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    print(Solution().mergeIntervals(intervals))
    intervals = [[1,4],[4,5]]
    print(Solution().mergeIntervals(intervals))
    intervals = [[4,7],[1,4]]
    print(Solution().mergeIntervals(intervals))
    intervals = [[1,4],[2,3]]
    print(Solution().mergeIntervals(intervals))