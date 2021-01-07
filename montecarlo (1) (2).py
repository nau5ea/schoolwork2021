# -*- coding: utf-8 -*-
"""
Author username(s): moenchlm
Date: 10/2/20
Assignment/problem number: P6
Assignment/problem title: Monte Carlo and Friends
"""
"""
This file contains several small functions which produce random outcomes,
using the random and math standard libraries.
"""

import random
import math

def pi_est(N):
    """This function estimates pi.

    Parameters
    ----------
    N : int
        determines the accuracy level of the estimation of pi, based on the
        number of times the function iterates.

    Returns
    -------
    A float estimation of pi.

    """
    area = 0
    for i in range(N):
        x = random.random()
        y = random.random()
        dist = math.sqrt(x**2 + y**2)
        if dist <= 1:
            area += 1
    return((area/N) * 4)

def flip():
    """This function simulates an even coin toss.

    Returns
    -------
    string
        "H" is for heads, while "T" is for tails.

    """
    return random.choice(["H", "T"])

def six_heads():
    """This function simulates a series of coin tosses, ceasing when heads
    is obtained six times in a row.
    

    Returns
    -------
    The int length of the list which ultimately contained six heads in a row.

    """
    
    outcomes = []
    for i in range(6):
        outcomes.append(flip())
    while outcomes[-6:] != ["H", "H", "H", "H", "H", "H"]:
        outcomes.append(flip())
    return(len(outcomes))
    
def average_six(n):
    """This function finds the average number of coins which had to
    be flipped in order to obtain six heads in a row.
    

    Parameters
    ----------
    n : int
        determines the number of trials the average of 
        whose length will be found.

    Returns
    -------
    int
        the average number of flips it took to obtain 6 heads in a row,
        of n trials.

    """
    
    results = 0
    for i in range(n):
        results += six_heads()
    return results/n

def hhh():
    """
    This function determines the number of flips it took to obtain 3 heads in
    a row.

    Returns
    -------
    The number of flips it took to obtain 3 heads in a row.

    """
    
    outcomes = []
    for i in range(3):
        outcomes.append(flip())
    while outcomes[-3:] != ["H", "H", "H"]:
        outcomes.append(flip())
    return(len(outcomes))

def hht():
    """
    This function determines the number of flips it took to obtain 2 heads
    followed by one tail.

    Returns
    -------
    The number of flips it took to obtain 2 heads followed by one tail.

    """
    
    outcomes = []
    for i in range(3):
        outcomes.append(flip())
    while outcomes[-3:] != ["H", "H", "T"]:
        outcomes.append(flip())
    return(len(outcomes))

def simulate_flips(n):
    """
    This function simulates both the average number of flips it took to 
    obtain 2 heads followed by one tail and the average number of flips it took 
    to obtain 3 heads in a row.

    Parameters
    ----------
    n : int
        determines the accuracy of the average by means of the number of 
        iterations the function undertakes.

    Returns
    -------
    Prints a string which tells the average number of flips in n trials
    after which HHH was obtained, and after which HHT was obtained.

    """
    
    numhhh = 0
    numhht = 0
    for i in range(n):
        numhhh += hhh()
        numhht += hht()
    print("Average number of trials to return hht: " + str(numhht/n), "Average number of trials to return hhh: " + str(numhhh/n))
    