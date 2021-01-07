'''
Code from section 6.5, "Analyzing text", p. 279-287
J. Havill (2016), _Discovering Computer Science_
'''

def count1(text, target):
    """Count the number of occurences of target character in text.

    Parameters:
        text: a string object
        target: a single-character string object

    Return value: the number of occurrences of target in text
    """
    count = 0
    for character in text:
        if character == target:
            count = count + 1
    return count

def count1b(text, target):
    """Count the number of occurences of target character in text.

    Parameters:
        text: a string object
        target: a single-character string object

    Return value: the number of occurrences of target in text
    """
    count = 0
    for index in range(len(text)):
        if text[index] == target:
            count = count + 1
    return count

def find1(text, target):
    """Find the index of the first occurrence of target in text

    Parameters:
        text: a string object
        target: a single-character string object

    Return value: the index of the first occurrence of target in text
    """
    for index in range(len(text)):
        if text[index] == target:
            return index
    return -1



def count(text, target):
    """Count the number of target strings in text.

    Parameters:
        text: a string object
        target: a single-character string object

    Return value: the number of occurrences of target in text
    """
    count = 0
    for index in range(len(text)):
        if text[index:index+len(target)] == target:
            count = count + 1
    return count

