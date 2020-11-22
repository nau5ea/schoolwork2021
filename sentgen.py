# -*- coding: utf-8 -*-
"""
Author username(s): moenchlm, najw
Date: 11/7/20
Assignment/problem number: P12
Assignment/problem title: Generating Random Sentences
"""

import random

def weighted_select(dictio):
    """
    PRE:
        dictio must be a dictionary containing words and associated weights
    POST:
         returns a weighted random choice from the dictionary   
         
    Parameters
    ----------
    dictio : dict
        contains words and their associated weights.

    Returns
    -------
    string
        a weighted selection from dictio.

    """
    lst = []
    for i in dictio.keys():
        for n in range(dictio[i]):
            lst.append(i)
    return random.choice(lst)
    
def bigram_count(string):
    """
    PRE:
        string is a string (with spaces!)
    POST:
        returns a dictionary containing words associated with sets of words
        with which they appear in bigrams, and how many times this occurs for
        each

    Parameters
    ----------
    string : str
        a sentence containing words.

    Returns
    -------
    a dictionary containing the frequency of bigrams in the string.

    """
    wordList = string.split()
    #print(wordList)
    maindict = {}
    for a in range(1, len(wordList)):
        lastWord = wordList[a - 1]
        thisWord = wordList[a]
        if lastWord not in maindict:
            maindict[lastWord] = {thisWord: 0}
        #print(maindict)
        #print(maindict[lastWord])
        #print(thisWord)
        if thisWord in maindict[lastWord]:
            maindict[lastWord][thisWord] += 1
            #print(maindict[lastWord][thisWord])
        if thisWord not in maindict[lastWord]:
            bigramDict = maindict[lastWord]
            bigramDict[thisWord] = 1
#        maindict[i] = wordList[i]
    return maindict

def random_sentence(dictio, start, length):
    """
    PRE:
        dictio is a dictionary containing the frequencies of bigrams in a 
        string.
        
        start is a string that appears as a key in dictio.
        
        length is a positive integer.

    Parameters
    ----------
    dictio : dict
        contains the frequencies of bigrams in a text.
    start : str
        appears at least once in dictio and is the desired starting word.
    length : int
        as long as you want! dictates the length of the output (in words).

    Returns
    -------
    str
        a pseudorandomly generated sentence based on the frequencies of bigrams
        in a given text.

    """
    start
    outlst = [start]
    newWord = weighted_select(dictio[start])
    #print(newWord)
    for i in range(length - 1):
        outlst.append(newWord)
        #print(outlst)
        newWord = weighted_select(dictio[newWord])
        #print(newWord)
    #print(outlst)
    return ' '.join(outlst)

def read_file(filename):
    textFile = open(filename, 'r', encoding = 'utf-8')
    text = textFile.read()
    textFile.close()
    return text

def main():
    text = read_file(input('Tell me the name of your file, OR ELSE.'))
    bigrams = bigram_count(text)
    start = input("Tell me the word you want to start with, OR ELSE.")
    length = int(input("""Oh, and if you would be so kind, please let me know 
                       the length of the string you want."""))
    return random_sentence(bigrams, start, length)