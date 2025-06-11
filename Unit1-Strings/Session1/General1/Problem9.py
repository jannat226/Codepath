def can_pair(item_quantities):
    if len(item_quantities) == 0:
        print(True)
        return 
    for item in item_quantities:
        if item%2 !=0:
            print(False)
            return 
    print(True)   
    return 
            
# Example Usage

item_quantities = [2, 4, 6, 8]
can_pair(item_quantities)

item_quantities = [1, 2, 3, 4]
can_pair(item_quantities)

item_quantities = []
can_pair(item_quantities)
# Example Output:

# True
# False
# True