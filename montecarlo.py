# -*- coding: utf-8 -*-
"""
Author username(s): moenchlm
Date: 26/9/20
Assignment/problem number: P6
Assignment/problem title: Monte Carlo and Friends
"""



def pi_est(N):
    import random
    import math
    area = 0.0
    for i in range(N):
        point = [random.random(), random.random()]
        if math.sqrt(point[0] ** 2 +  point[1] ** 2) <= 1:
            area += 4/N
    print(area)

def flip():
    import random
    x = random.randint(0, 1)
    if x == 1:
        return("H")
    else:
        return("T")

def six_heads():
    outcomes = ""
    if "HHHHHH" in outcomes == True:
        return(len(outcomes))
    else:
        while True:
            new = flip()
            outcomes.join(new)
            print(outcomes)
            if "HHHHHH" in outcomes:
                break


"""
    
def average_six():
    
def simulate_flips(n):
"""  