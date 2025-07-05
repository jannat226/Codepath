# Problem 6: Print Inventory
#
# class Villager():
#     # ... methods from previous problems
    
#     def print_inventory(self):
#         # Implement the method here
#         pass
# Example Usage:

# alice = Villager("Alice", "Koala", "guvnor")

# alice.print_inventory()

# alice.furniture = ["acoustic guitar", "ironwood kitchenette", "kotatsu", "kotatsu"]
# alice.print_inventory()
# Example Output:

# Inventory empty
# acoustic guitar: 1, ironwood kitchenette: 1, kotatsu: 2

class Villager:
    # ... methods from previous problems
    ''' Update the Villager class with a method print_inventory() that accepts no parameters except for self.

    # The method should print the name and quantity of each item in a villager’s furniture list.

    # The name and quantity should be in the format "item1: quantity, item2: quantity, item3: quantity" for
    # however many unique items exist in the villager's furniture list
    # If the player has no items, the function should print "Inventory empty".
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
    
    def print_inventory(self):
        dict = {}
        if self.furniture is None:
            print("Inventory Empty")
        else:
            for item in self.furniture:
                dict[item]= dict.get(item,0) + 1
        lst=[]
        for key,value in dict.items():
            lst.append("{key:{value}")
        print(lst)
            # print(f"{key}:{value}")
            

alice = Villager("Alice", "Koala", "guvnor")

alice.print_inventory()

alice.furniture = ["acoustic guitar", "ironwood kitchenette", "kotatsu", "kotatsu"]
alice.print_inventory()
# Example Output:

# Inventory empty
# acoustic guitar: 1, ironwood kitchenette: 1, kotatsu: 2 
                
                
            
            
        