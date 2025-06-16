def count_endangered_species(endangered_species, observed_species):
    pass
# Example Usage:

endangered_species1 = "aA"
observed_species1 = "aAAbbbb"

endangered_species2 = "z"
observed_species2 = "ZZ"

print(count_endangered_species(endangered_species1, observed_species1)) 
print(count_endangered_species(endangered_species2, observed_species2))  

# Example Output:

# 3 # `a` and `A` are endangered species. `a` appears once, and `A` twice.
# 0