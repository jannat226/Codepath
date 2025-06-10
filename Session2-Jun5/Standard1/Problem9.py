# Problem 9: Merge Strings Alternately
# Write a function merge_alternately() that accepts two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.

def merge_alternately(word1, word2):
    res = ''
    len1 = len(word1)
    len2 = len(word2)
    minlen = min(len1,len2)
   
    for i in range(minlen):
        res += word1[i]
        res+= word2[i]
    res += word1[minlen:] + word2[minlen:]
    print(res)

word1 = "wol"
word2 = "oze"
merge_alternately(word1, word2)

word1 = "hfa"
word2 = "eflump"
merge_alternately(word1, word2)

word1 = "eyre"
word2 = "eo"
merge_alternately(word1, word2)

# Example Output:

# "woozle"
# "heffalump"
# "eeyore"

