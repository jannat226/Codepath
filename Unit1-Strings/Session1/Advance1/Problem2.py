# Tigger has developed a new programming language Tiger with only four operations and one variable tigger.

# bouncy and flouncy both increment the value of the variable tigger by 1.
# trouncy and pouncy both decrement the value of the variable tigger by 1.
# Initially, the value of tigger is 1 because he's the only tigger around! Given a list of strings operations containing a list of operations, return the final value of tigger after performing all the operations.

def final_value_after_operations(operations):
    result = 1
    for op in operations:
        if op == "bouncy" or op =="flouncy":
            result += 1
        elif op == "trouncy" or op =="pouncy":
            result -=1
        else:
            print("Invalid operation")
    print(result)
# Example Usage:

operations = ["trouncy", "flouncy", "flouncy"]
final_value_after_operations(operations)

operations = ["bouncy", "bouncy", "flouncy"]
final_value_after_operations(operations)
# Example Output:

# 2
# 4