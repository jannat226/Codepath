# Problem 1: New Horizons

class Villager:
    '''Step 1: Copy the following code into your IDE.

    Step 2: Instantiate an instance of the class Villager, which represents characters in Animal Crossing.
    Store the instance in a variable named apollo.

    The Villager object created should have the name "Apollo", the species "Eagle", and the catchphrase "pah".'''
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []
    
    def greet_player(self, player_name):
        '''Step 1: Using the Villager class from Problem 1, add the following greet_player() method to your existing code:
        Step 2: Create a second instance of Villager in a variable named bones.

        The Villager object created should have name "Bones", species "Dog", and catchphrase "yip yip".
        Step 3: Call the method greet_player() with your name and print out "Bones: Hey there, <your name>! How's it going, yip yip!". For example, if your name is Tram, "Bones: Hey there, Tram! How's it going, yip yip?" would be printed out to the console.

        '''
        return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"
apollo = Villager("Apollo","Eagle","pah")

# Instantiate your villager here
# Example Usage:

print(apollo.name)  
print(apollo.species)  
print(apollo.catchphrase) 
print(apollo.furniture) 
# Example Output:

# Apollo
# Eagle
# pah
# []

# Problem 2: Greet Player



# Example Usage:
bones = Villager("Bones","Dog","ruff it up")



print(bones.name)
print(bones.species)  
print(bones.catchphrase) 
print(bones.furniture) 
# Example Output:

# Bones
# Dog
# yip yip
# []

print(bones.greet_player("Samia"))
# Example Output:

# Bones: Hey there, Samia! How's it going, ruff it up!