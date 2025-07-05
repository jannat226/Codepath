# roblem 1: Post Format Validator
# You are managing a social media platform and need to ensure that posts are properly formatted. Each post must have balanced and correctly nested tags, such as () for mentions, [] for hashtags, and {} for links. You are given a string representing a post's content, and your task is to determine if the tags in the post are correctly formatted.

# A post is considered valid if:

# Every opening tag has a corresponding closing tag of the same type.
# Tags are closed in the correct order.
def is_valid_post_format(posts):
    valid = {')':'(',']':'[','{':'}'}
    stack = []
    for char in posts:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not  stack:
                return False
            last_char = stack.pop()
            if last_char != valid[char]:
                return False
    return True
            
# Example Usage:

print(is_valid_post_format("()"))
print(is_valid_post_format("()[]{}")) 
print(is_valid_post_format("(]"))
# Example Output:

# True
# True
# False