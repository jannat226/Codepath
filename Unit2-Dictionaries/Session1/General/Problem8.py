def num_popular_pairs(popularity_scores):
    ''' Given an array of integers popularity_scores representing the popularity scores of songs in a music festival playlist,          
    # return the number of popular song pairs.

    # A pair (i, j) is called popular if the songs have the same popularity score and i < j.
    # Hint: number of pairs = (n x n-1)/2'''
    # count ={}
    # Pair = 0
    # for value in popularity_scores:
    #     count[value] = count.get(value,0)+1
    # for key, value in count.items():
    #     if count[key]>1:
    #         Pair += (value * value-1)//2
    # return Pair
    pair = 0
    count ={}
    for value in popularity_scores:
        count[value] = count.get(value,0)+1
    for key,value in count.items():
        pair +=  (value * (value - 1)) // 2
   
    return pair
        
        
    
        
    
    
# Example Usage:

popularity_scores1 = [1, 2, 3, 1, 1, 3]
popularity_scores2 = [1, 1, 1, 1]
popularity_scores3 = [1, 2, 3]

print(num_popular_pairs(popularity_scores1))
print(num_popular_pairs(popularity_scores2))
print(num_popular_pairs(popularity_scores3)) 
# Example Output:

# 4
# 6
# 0