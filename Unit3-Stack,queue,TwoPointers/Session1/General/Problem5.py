def encode( strs):
        encoded_string = ''.join(strs)
        print(encoded_string)

def decode( strs) :
    decoded = strs.split('-')
    return decoded
lst = ['hey','there']
encoded = encode(lst)
# decoded = 
print(decode(encoded))