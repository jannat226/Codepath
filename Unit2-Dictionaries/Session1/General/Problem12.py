

def sort_performers(performer_names, performance_times):
    """
    Problem 12: Sort the Performers
    You are given an array of strings performer_names, and an array performance_times that consists of distinct positive integer
    representing the performance durations in minutes. Both arrays are of length n.

    For each index i, performer_names[i] and performance_times[i] denote the name and performance duration of the ith performer.

    Return performer_names sorted in descending order by the performance durations.
    :type performer_names: List[str]
    :type performance_times: List[int]
    :rtype: List[str]
    """
    map ={}
    for i in range(len(performance_times)):
        map[performer_names[i]] = performance_times[i]
    
    sorted_performers = sorted(map.items(),key = lambda x:x[1], reverse=True)

    
    return  [name for name, time in sorted_performers]
    
# Example Usage:

performer_names1 = ["Mary", "John", "Emma"]
performance_times1 = [180, 165, 170]

performer_names2 = ["Alice", "Bob", "Bob"]
performance_times2 = [155, 185, 150]

print(sort_performers(performer_names1, performance_times1)) 
print(sort_performers(performer_names2, performance_times2))
# Example Output:

# ["Mary", "Emma", "John"]
# ["Bob", "Alice", "Bob"]