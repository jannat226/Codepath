# Problem 7: NaNaNa Batman!
# Write a function nanana_batman() that accepts an integer x and prints the string "nanana batman!" where "na" is repeated x times. Do not use the * operator.

def nanana_batman(x):
    na=''
    for i in range(0,x,1):
        na +='na'
    print(f"{na} batman!")
        
        
# Example Usage

x = 6
nanana_batman(x)

x = 0
nanana_batman(x)
# Example Output:

# "nananananana batman!"
# "batman!"