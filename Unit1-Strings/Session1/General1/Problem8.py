def print_todo_list(task):
    print("Pooh's To Dos")
    if len(task) ==0 :
        return
    for i in range(len(task)):        
        print(f"{i+1}. {task[i]}")
    
# Example Usage

task = ["Count all the bees in the hive", "Chase all the clouds from the sky", "Think", "Stoutness Exercises"]
print_todo_list(task)

task = []
print_todo_list(task)
# Example Output:

# Pooh's To Dos:
# 1. Count all the bees in the hive
# 2. Chase all the clouds from the sky
# 3. Think
# 4. Stoutness Exercises

# Pooh's To Dos:
