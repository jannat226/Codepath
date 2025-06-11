# Problem 5: Container with Most Honey
# Christopher Robin is helping Pooh construct the biggest hunny jar possible. Help his write a function that accepts an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most honey.

# Return the maximum amount of honey a container can store.

# Notice that you may not slant the container.

def most_honey(height):
    max = 0
    for i in range(len(height)):
        if (height[i]>max):
            max = height[i]
        
    return 
# Bar graph showing heights of lines in Example 1, with blue section between lines with height 8 and 7

# Example Usage

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
most_honey(height)

height = [1, 1]
most_honey(height)
# Example Output:

# 49
# 1