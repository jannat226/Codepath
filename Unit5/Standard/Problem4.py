# Problem 4: Set Character
#
class Villager:
    ''' In the previous exercise, we accessed and modified a player’s catchphrase attribute directly.
    Instead of allowing users to update their player directly, it is common to create setter methods
    that users can call to update class attributes. 
    This has a few different benefits, including allowing us to validate data before updating our class instance.

    # Update your Villager class with a method set_catchphrase() that takes in one parameter new_catchphrase.

    # If new_catchphrase is valid, it should update the villager's catchphrase attribute to have value
    # new_catchphrase and print "Catchphrase updated".
    # Otherwise, it should print out "Invalid catchphrase".
    # Valid catchphrases are less than 20 characters in length. They must all contain only alphabetic and
    # whitespace characters.
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
            
        # if " " in new_catchphrase and len(new_catchphrase) < 20 :
            
        #     new_catchphrase2 = new_catchphrase.replace(" ","")
        #     if  new_catchphrase2.isalpha() :
        #         self.catchphrase = new_catchphrase
        #         print("catchphrase updated!")
        # else:
        #     print("Invalid Catchphrase!")
                
# Example Usage:

alice = Villager("Alice", "Koala", "guvnor")

alice.set_catchphrase("sweet dreams")
print(alice.catchphrase)
alice.set_catchphrase("#?!")
print(alice.catchphrase)
# Example Output:

# Example 1:
# Catchphrase Updated!
# sweet dreams
# Invalid catchphrase
# sweet dreams
