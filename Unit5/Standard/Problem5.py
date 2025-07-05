# Problem 5: Add Furniture

class Villager:
    # ... methods from previous problems
    '''Players and villagers in Animal Crossing can add furniture to their inventory to decorate their house.

    Update the Villager class with a new method add_item() that takes in one parameter, item_name.

    The method should validate the item_name.

    If the item is valid, add item_name to the player’s furniture attribute.
    The method does not need to return any values.
    item_name is valid if it has one of the following values: "acoustic guitar", "ironwood kitchenette", 
    "rattan armchair", "kotatsu", or "cacao tree".
    '''
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []

    def set_catchphrase(self, new_catchphrase):
        # for loop for alpha or whitespace
        if len(new_catchphrase)  < 20 : 
            for char in new_catchphrase:
                if char.isalpha() or char == " ":
                    pass
                else:
                    print("Invalid Catchphrase")
                    return
            self.catchphrase = new_catchphrase
            print("catchphrase updated!")
            
        else:
            print("Invalid Catchphrase")
        return
    # New method
    def add_item(self, item_name):
        valid_items = ["acoustic guitar", "ironwood kitchenette",  "rattan armchair", "kotatsu",  "cacao tree"]
        if item_name in valid_items:
            self.furniture.append(item_name)
        else:
            # print("Invalid item name")
            pass
# Example Usage:

alice = Villager("Alice", "Koala", "guvnor")
print(alice.furniture)

alice.add_item("acoustic guitar")
print(alice.furniture)

alice.add_item("cacao tree")
print(alice.furniture)

alice.add_item("nintendo switch")
print(alice.furniture)
# Example Output:

# []
# ["acoustic guitar"]
# ["acoustic guitar", "cacao tree"]
# ["acoustic guitar", "cacao tree"]
