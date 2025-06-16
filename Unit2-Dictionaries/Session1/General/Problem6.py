# Problem 6: Performances with Maximum Audience
# You are given an array audiences consisting of positive integers representing the audience size for different performances at a music festival.

# Return the combined audience size of all performances in audiences with the maximum audience size.

# The audience size of a performance is the number of people who attended that performance.

# def max_audience_performances(audiences):
#     '''You are given an array audiences consisting of positive integers representing the audience size for different performances
#      at a music festival.

#     # Return the combined audience size of all performances in audiences with the maximum audience size.
#     '''
#     count = {}
#     # maxValue = float('-inf')
#     for index,value in enumerate(audiences):
#         count[value]= count.get(value,0)+1
#         # if value > maxValue:
#             # maxValue =  value
#     maxValue = max(count, key = count.get)  
    
#     maxCount = count[maxValue]
#     result = 0
#     for i in range(maxCount):
#         result += maxValue
#     return result
def max_audience_performancesNoDict(audiences): 
    maxCount = float('-inf')
    
    for i in range(len(audiences)):
        if (audiences[i] > maxCount):
            maxCount = audiences[i]
            result = maxCount
        elif (audiences[i] == maxCount):
            result += audiences[i]
    return result
            
         
            
# Example Usage:

audiences1 = [100, 200, 200, 150, 100, 250]
audiences2 = [120, 180, 220, 150, 220]

print(max_audience_performancesNoDict(audiences1))
print(max_audience_performancesNoDict(audiences2))
# Example Output:

# 250
# 440