# Problem 6: Merge Intervals
# Write a function merge_intervals() that accepts an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

def merge_intervals(intervals):
    res = []
    for i in range(len(intervals)-1):
        if intervals[i+1][0] < intervals[i][1] or  intervals[i+1][0] == intervals[i][1]:
            res.append([intervals[i][0],intervals[i+1][1] ])
        else:
            res.append([intervals[i+1][0],intervals[i+1][1]])
    print(res)
            
            
# Example Usage 

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
merge_intervals(intervals)

intervals = [[1, 4], [4, 5]]
merge_intervals(intervals)
# Example Output:

# [[1, 6], [8, 10], [15, 18]]
# [[1, 5]]