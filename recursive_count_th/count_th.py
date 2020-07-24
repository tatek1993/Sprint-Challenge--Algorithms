'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):

    # TBC
    # If we find lowercase th in a word
    if "th" in word:
        # We return 1 and call count_th again,
        # this time with the first instance of th replaced with X
        return 1 + count_th(word.replace("th", "X", 1))
    # if we do not find a th return 0
    else:
        return 0
