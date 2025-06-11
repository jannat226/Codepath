def get_item(items, x):
    result = items[x] if x< len(items) and x > -1 else None
    print(result)
    # if x< len(items) and x > -1:
    #     print(items[x])
    # else:
    #     print (None)
     


items = ["piglet", "pooh", "roo", "rabbit"]
x = 2
get_item(items, x)

items = ["piglet", "pooh", "roo", "rabbit"]
x = 5
get_item(items, x)
# Example Output:

# "roo"
# None