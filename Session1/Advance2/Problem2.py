# Pooh is eating all of his hunny jars in order of smallest to largest. Given a list of integers hunny_jar_sizes, write a function delete_minimum_elements() that continuously removes the minimum element until the list is empty. Return a new list of the elements of hunny_jar_sizes in the order in which they were removed.

def delete_minimum_elements(hunny_jar_sizes):
    result = []
    for i in range(len(hunny_jar_sizes)):
        min_val = min(hunny_jar_sizes)
        hunny_jar_sizes.remove(min_val)
        result.append(min_val)
    print(result)
    
    
# Example Usage

hunny_jar_sizes = [5, 3, 2, 4, 1]
delete_minimum_elements(hunny_jar_sizes)

hunny_jar_sizes = [5, 2, 1, 8, 2]
delete_minimum_elements(hunny_jar_sizes)
# Example Output:

# [1, 2, 3, 4, 5]
# [1, 2, 2, 5, 8]