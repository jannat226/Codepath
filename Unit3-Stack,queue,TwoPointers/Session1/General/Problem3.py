# Problem 3: Check Symmetry in Post Titles

def is_symmetrical_title(title):
    '''# As part of a new feature on your social media platform, you want to highlight post titles that are symmetrical,
    # meaning they read the same forwards and backwards when ignoring spaces, punctuation, and case. Given a post title as a string,
    # use a new algorithmic technique the two-pointer method to determine if the title is symmetrical.
    '''
    title = title.replace(' ','')
    title = title.lower()
    n = len(title) 
    if n <1:
        return None
    for i in range(len(title)):
        if title[i] != title[n-1-i]:
            return False
    return True
            
        
    print(title)
    
# Example Usage:

print(is_symmetrical_title("A Santa at NASA"))
print(is_symmetrical_title("Social Media")) 
# Example Output:

# True
# False