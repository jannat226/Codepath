# Problem 4: Sum of Digits
# Write a function sum_of_digits() that accepts an integer num and returns the sum of num's digits.

def sum_of_digits(num):
    result = 0 
    while num != 0:
        reminder = num%10
        num = num//10
        result += reminder
    print(result)
    return result
   
        
        
    
# Example Usage

num = 423
sum_of_digits(num)

num = 4
sum_of_digits(num)
# Example Output:

# 9 # Explanation: 4 + 2 + 3 = 9
# 4 