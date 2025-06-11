# Implement a function get_last() that accepts a list of items items and returns the last item in the list. If the list is empty, return None.

def get_last(items):
    if len(items)>0:
        print(items[-1])
    else :
        print(None)
# Example Usage

items = ["spider man", "batman", "superman", "iron man", "wonder woman", "black adam"]
get_last(items)

items = []
get_last(items)
# Example Output:

# "black adam"
# None
