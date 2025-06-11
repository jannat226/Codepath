# Problem 6: Acronym
# Given an array of strings words and a string s, implement a function is_acronym() that returns True if s is an acronym of words and returns False otherwise.

# The string s is considered an acronym of words if it can be formed by concatenating the first character of each string in words in order. For example, "pb" can be formed from ["pooh"", "bear"], but it can't be formed from ["bear", "pooh"].

def is_acronym(words, s):
    acr = ''.join(word[0] for word in words)
    print(acr == s)
# Example Usage

words = ["christopher", "robin", "milne"]
s = "crm"
is_acronym(words, s)
# Example Output:

# True