strs = ['def','ghk','abc']
doubled = ''.join(sorted(strs))

doubled = [value * 2 for value in strs]

# Example 3: Sorting Keys in a Dictionary
my_dict = {'apple': 2, 'banana': 3, 'cherry': 1}
result = sorted(my_dict)
print(result)  # Output: ['apple', 'banana', 'cherry']

print(doubled) # Output: [2, 4, 6, 8, 10]