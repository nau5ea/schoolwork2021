# -*- coding: utf-8 -*-
"""
Author username(s): moenachlm
Date: 10/14/2020
Assignment/problem number: p9
Assignment/problem title: Hamming Distance
"""

def hamming(s1, s2):
    """
    

    Parameters
    ----------
    s1 : string
        the first set of binary digits which will be compared to the second.
    s2 : string
        the second set of binary digits which will be compared to the first.

    Returns
    -------
    total : int
        the Hamming Distance between s1 and s2 as binary digits.

    """
    total = 0
    if len(s1) > len(s2):
        for i in range(len(s2)):
            if s2[i] != s1[i]:
                total += 1
                total += len(s1) - len(s2)
    else:
        for i in range(len(s1)):
            if s2[i] != s1[i]:
                total += 1
                total += len(s2) - len(s1)
    return total

def main():
    """
    reads in the first line from each of two files, f1 nad f2,to two variables,
    s1 and s2, then returns the hamming distance of s1 and s2.

    Returns
    -------
    int
        the hamming distance between the two lines.

    """
    f1 = open(input("Enter the file name of your first string: "), 'r', 
              encoding = "utf-8")
    f2 = open(input("Enter the file name of your second string: "), 'r', 
              encoding = "utf-8")
    s1 = f1.readline()
    s2 = f2.readline()
    out1 = ''
    out2 = ''
    for i in range(len(s1)):
        if ord(s1[i]) != 32 and s1[i] not in "n" and s1[i] not in "\s":
            out1 += s1[i]
    for i in range(len(s2)):
        if ord(s2[i]) != 32 and s2[i] not in "n" and s2[i] not in "\s":
            out2 += s2[i]
    
    
    print(hamming(out1, out2))
    return hamming(out1, out2)