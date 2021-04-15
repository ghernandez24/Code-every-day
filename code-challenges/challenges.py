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


# Your goal is to create a function that removes the first and last character of a string. You're given one parameter, the original string. All input strings will be two characters or longer.


def remove_char(s):
    word = s.split()
    result = ''
    for a in word:
      result += a[1:len(a) - 1] + ""
    return result


print(remove_char('eloquent'))  # -> 'loquen'
print(remove_char('country'))  # -> 'ountr'
print(remove_char('person'))  # -> 'erso'
print(remove_char('place'))  # -> 'lac'
print(remove_char('ok'))  # -> ''
print(remove_char('ooopsss'))  # -> 'oopss'


# Find the greatest common divisor of two positive integers without using a Python library. The integers may be large, so after you write a brute force solution, try to find a more efficient solution.

# The inputs x and y are always greater or equal to 1, so the greatest common divisor will always be an integer that is greater than or equal to 1.

def mygcd(x, y):
    while y:
        x, y = y, x % y
    return x


# the basics
print(mygcd(30, 12))  # -> 6
print(mygcd(8, 9), 1)  # -> 1
print(mygcd(1, 1), 1)  # -> 1

# some bigger numbers -- try these after you get the basics to work
# if your solution is Big O(N), how could you improve the time complexity?
print(mygcd(4805817, 7783376))  # -> 227
print(mygcd(6285978, 22959909))  # -> 1593
print(mygcd(15713250, 10063368))  # -> 1722
