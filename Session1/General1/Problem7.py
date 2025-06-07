def count_less_than(race_times, threshold):
    count = 0 
    if (len(race_times)==0 & threshold==0):
        count = 0 
    for i in range(len(race_times)):        
        count = count + 1 if race_times[i] < threshold and race_times[i] > 0 else count
    print(count)
    return count
	
# Example Usage

race_times = [1, 2, 3, 4, 5, 6]
threshold = 4
count_less_than(race_times, threshold)

race_times = []
threshold = 4
count_less_than(race_times, threshold)
# Example Output:

# 3
# 0