
# Tony Stark, aka Iron Man, has designed many different suits over the years.
# Given a list of strings suits where each string is a suit in Stark's collection,
# count the total number of suits in the list.

# Implement the solution iteratively without the use of the len() function.
# Implement the solution recursively.

# Discuss: what are the similarities between the two solutions? What are the differences?
def count_suits_iterative(suits):
    '''Implement the solution iteratively without the use of the len() function.'''
    counter = 0
    for suit in suits:
        counter += 1
    return counter
    

def count_suits_recursive(suits):
    '''Implement the solution recursively.'''
    counter = 0
    # base case
    if not suits:
        return counter 
    # recursive
    return 1 + count_suits_recursive(suits[1:])
    
# Example Usage:

print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
print(count_suits_recursive(["Mark I", "Mark I", "Mark III", "Mark IV"]))
# Example Output:

3
4