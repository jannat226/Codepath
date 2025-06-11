def sum_honey(hunny_jars):
    sum = 0
    for i in range(len(hunny_jars)):
        sum += hunny_jars[i]
    print (sum)
# Example Usage

hunny_jars = [2, 3, 4, 5]
sum_honey(hunny_jars)

hunny_jars = []
sum_honey(hunny_jars)
# Example Output:

# 14
# 0