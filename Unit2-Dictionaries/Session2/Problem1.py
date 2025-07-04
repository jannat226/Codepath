def most_endangered(species_list):
    '''Imagine you are working on a wildlife conservation database. Write a function named most_endangered() that 
    returns the species with the highest conservation priority based on its population.

    The function should take in a list of dictionaries named species_list as a parameter. 
    Each dictionary represents data associated with a species, including its name, habitat, and wild population. 
    The function should return the name of the species with the lowest population.

    If there are multiple species with the lowest population, return the species with the lowest index.'''
    minVal = float('inf')
    lowestIndex = -1
    name = ''
    for index,item in enumerate(species_list):
        if item["population"] < minVal :
            minVal = item["population"]
            
            lowestIndex = index
            name = item["name"]
    # print(name)        
    return name          
# Example Usage:

species_list = [
    {"name": "Amur Leopard",
     "habitat": "Temperate forests",
     "population": 84
    },
    {"name": "Javan Rhino",
     "habitat": "Tropical forests",
     "population": 72
    },
    {"name": "Vaquita",
     "habitat": "Marine",
     "population": 10
    }
]

print(most_endangered(species_list))
# Example Output:

# Vaquita