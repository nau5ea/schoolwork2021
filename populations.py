# -*- coding: utf-8 -*-
"""
Author username(s): moenchlm
Date: 23/9/20
Assignment/problem number: P5
Assignment/problem title: Plotting Populations
"""


# this function models the population growth rate of Tribbles.
    
def tribble_table(initial_pop, n_days):
    print("Day | Population")
    print("-----------------")
    for i in range(n_days):
        print("{0:>3d} |{1:>11d}".format(i, initial_pop))
        initial_pop = int(initial_pop * 1.10)
              
              #"  " + str(i + 1) + " |        " + str(initial_pop)")

# This function plots the data from above.

def tribble_plot(initial_pop, n_days):
    import matplotlib.pyplot as plt
    init_tribbles = [initial_pop]
    days = [0]
    for i in range(n_days):
        initial_pop = int(initial_pop*1.10)
        init_tribbles.append(initial_pop)
        days.append(i + 1)
   # print(init_tribbles, days)
    plt.plot(days, init_tribbles)


#Each night, the vampires will turn a number of humans equal to half the vampires.
# She can destroy nightly_kill vampires per night. For purposes of the calculations,
#assume that the vampires are destroyed after they have preyed upon the humans.

# this function models the human population level over time of a town with a
# virulent vampire infestation.

def vampire_table(initial_humans, initial_vampires, nightly_kill, n_days):
    print(" Day |  Humans | Vampires")
    print("-------------------------")
    for i in range(n_days + 1):
        print("{0:>4d} |{1:>8d} |{2:>9d} ".format(i, initial_humans, initial_vampires))
        initial_humans -= int(initial_vampires/2)
        initial_vampires += int(initial_vampires/2)
        initial_vampires -= nightly_kill


# This function plots the data from above.

def vampire_plot(initial_humans, initial_vampires, nightly_kill, n_days):
    import matplotlib.pyplot as plt
    humans = [initial_humans]
    days = [0]
    for i in range(n_days + 1):
        initial_humans -= int(initial_vampires/2)
        initial_vampires += int(initial_vampires/2)
        initial_vampires -= nightly_kill
        humans.append(initial_humans)
        days.append(i)
    plt.plot(days, humans)


# what do you get when you 3-way cross a human, a vampire, and a tribble?

def a_and_b(tribbles, vampires, humans):
    