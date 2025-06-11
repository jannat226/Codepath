# Problem 3: T-I-Double Guh-Er II
# T-I-Double Guh-Er: That spells Tigger! Write a function tiggerfy() that accepts a string word and returns a new string that removes any substrings t, i, gg, and er from word. The function should be case insensitive.

def tiggerfy(word):
    word_lower = word.lower()
    result = []
    i = 0
    while i < len(word_lower):
        if word_lower[i:i+2] =='gg':
            i+=2
        elif  word_lower[i:i+2] =='er':
            i+=2
        elif  word_lower[i] =='t':
            i+=1
        elif  word_lower[i] =='i':    
            i+=1
        else:
            result.append(word_lower[i])
            
            i+=1
    print(''.join(result))
# Example Usage:

word = "Trigger"
tiggerfy(word)

word = "eggplant"
tiggerfy(word)

word = "Choir"
tiggerfy(word)

# Example Output:
# "r"
# "eplan"
# "Chor"