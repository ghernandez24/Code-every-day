# Simple: given a string of words, return the length of the shortest word(s). String will never be empty, and you do not need to account for different data types.

def shortest_word(string):
    word = map(len, string.split())
    return min(word)
print(shortest_word("I don't think that word means what you think it means"))
# should return: 1

# Given a 2D list of size m * n, your task is to find the sum of the minimum value in each row.

def sum_of_minimums(list):

    return(sum(row[0] for row in list))
    
my_list = [
    [1, 2, 3, 4, 5],  # minimum value of row is 1
    [5, 6, 7, 8, 9],  # minimum value of row is 5
    [20, 21, 34, 56, 100]  # minimum value of row is 20
]

print(sum_of_minimums(my_list))
# should return 26

# Given a string, complete the function so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore('_').

## solved by 
def split_strings(s):
    split = []
    if len(s) % 2 !=0:
        s+="_"

    for i in range(0, len(s), 2):
        split.append(f"{s[i]}{s[i+1]}")
    return split

print(split_strings('abc'))
# should return ['ab', 'c_']

print(split_strings('abcdef'))
# should return ['ab', 'cd', 'ef']
