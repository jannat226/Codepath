# Problem 2: Pirate Message Check
# Taken captive, Captain Anne Bonny has been smuggled a secret message from her crew. She will know she can trust the message if it contains all of the letters in the alphabet. Given a string message containing only lowercase English letters and whitespace, write a function can_trust_message() that returns True if the message contains every letter of the English alphabet at least once, and False otherwise.

def can_trust_message(message):
    ''' Taken captive, Captain Anne Bonny has been smuggled a secret message from her crew.
    She will know she can trust the message if it contains all of the letters in the alphabet. Given a string message containing 
    only lowercase English letters and whitespace, write a function can_trust_message() that returns True 
    if the message contains every letter of the English alphabet at least once, and False otherwise.
    '''
    char1= 'a'
    # print(chr(ord(char1)+1))

    for i in range(26):
        currentChar = chr(ord(char1)+i)
        # print(currentChar)
        if currentChar not in message:
            return False
    return True

# Example Usage:

message1 = "sphinx of black quartz judge my "
message2 = "trust me hey there"

print(can_trust_message(message1))
print(can_trust_message(message2))
# Example Output:

# True
# False