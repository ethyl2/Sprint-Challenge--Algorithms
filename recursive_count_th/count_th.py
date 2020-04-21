'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    # Base case
    if len(word) < 2:
        return 0
    # Recurse toward base case:
    elif word[:2] == 'th':
        # Found a 'th' so increment the count and continue the recursion on rest of the word
        return count_th(word[1:]) + 1
    else:
        # Didn't find a th, but continue the recursion on rest of the word
        return count_th(word[1:])

# A couple of tests

# print(count_th('ththth'))
# print(count_th('bigonotation'))
