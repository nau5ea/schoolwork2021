# -*- coding: utf-8 -*-
"""
Code to generate the powerset of a set

File name: subsets.py
Author username(s): moenchlm
Date: 11/23/2020
"""

def subsets(sett):
    """
    Generates the powerset of the given set.
    
    pre:
        sett is a list.
    post:
        returns the set of all subsets in the given sett
    """
    out = [[]]
    if len(sett) == 0:
        return out
    for elem in sett:
        n = len(out)
        for i in range(n):
            r = out[i] + [elem]
            out.append(r)
        
    return out