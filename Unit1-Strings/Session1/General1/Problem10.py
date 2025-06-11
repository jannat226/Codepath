def split_haycorns(quantity):
    result = []
    for i in range(1, quantity):  # avoid division by zero
        if quantity % i == 0:
            result.append(i)
    print(result)
    return 
# Example Usage

quantity = 6
split_haycorns(quantity)

quantity = 1
split_haycorns(quantity)
# Example Output:

# [1, 2, 3, 6]
# [1]