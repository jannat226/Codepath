# Problem 7: Good Things Come in Threes
# Write a function make_divisible_by_3() that accepts an integer array nums. In one operation, you can add or subtract 1 from any element of nums. Return the minimum number of operations to make all elements of nums divisible by 3.

def make_divisible_by_3(nums):
    count = 0
    for num in nums :
        if num%3 != 0:
            if (num +1) % 3 == 0 or (num -1) % 3 == 0 :
                count += 1
                # print(num)
        else:
            pass
    print(count)
            
        

nums = [1, 2, 3, 4]
make_divisible_by_3(nums)

nums = [3, 6, 9]
make_divisible_by_3(nums)

# Example Output:

# 3
# 0