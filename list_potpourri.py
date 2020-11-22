# -*- coding: utf-8 -*-
"""
Author username(s): moenchlm
Date: 11/3/20
Assignment/problem number: P11
Assignment/problem title: List Potpourri
"""

def maximum(numbers):
    """
    PRE:
        numbers is a list containing ints
    POST:
        returns the largest element of numbers
        
    Parameters
    ----------
    numbers : list
        contains ints.

    Returns
    -------
    out : int
        max element of numbers.

    """
    out = numbers[0]
    for i in numbers:
        if i > out:
            out = i
    return out

def closest_to_zero(numbers):
    """
    PRE:
        numbers is a list of ints
    POST:
        returns the element of numbers with highest absolute value

    Parameters
    ----------
    numbers : list
        DESCRIPTION.

    Returns
    -------
    out : int
        element in numbers with smallest absolute value.

    """
    out = numbers[0]
    for i in numbers:
        if abs(i) < abs(out):
            out = i
    return out

def safe_sum(values):
    """
    PRE:
        values is a list of number types
    POST:
        returns the sum of the elements in values

    Parameters
    ----------
    values : list
        DESCRIPTION.

    Returns
    -------
    out : int or float
        sum of all elements in values.

    """
    out = 0
    for i in values:
        if type(i) == int or type(i) == float:
            out += i
    return out

def join_lists(list_of_lists):
    """
    PRE:
        list_of_lists is of type list, contians two elements, both of which
        are lists
    POST:
        returns a list containing the elements of each list in list_of_lists

    Parameters
    ----------
    list_of_lists : list
        contains two lists, which may contain any values.

    Returns
    -------
    out : list
        contains all elements of both lists in list_of_lists.

    """
    out = []
    for i in list_of_lists:
        for a in i:
            out.append(a)
    return out

def riffle(left, right):
    """
    PRE:
        left and right are of type list
    POST:
        returns one list of alternating elements from left and right

    Parameters
    ----------
    left : list
        may contain any values.
    right : list
        may contain any values.

    Returns
    -------
    out : list
        alternating elements from left and right, stitched together.

    """
    #this one is hideous
    out = []
    if len(left) > len(right):
        for i in range(len(right)):
            out.append(left[i])
            out.append(right[i])
        for i in range(len(left[len(right):])):
            out.append(left[i + len(right)])
        
    else:
        for i in range(len(left)):
            out.append(left[i])
            out.append(right[i])
        for i in range(len(right[len(left):])):
            out.append(right[i + len(left)])
    return out

def unriffle(lst):
    """
    PRE:
        lst is of type list
    POST:
        function returns tuple of unriffled lst

    Parameters
    ----------
    lst : list
        may contain any values.

    Returns
    -------
    out1 : list
         odd elements from lst.
    out2 : list
         even elements from lst.

    """
    out1 = []
    out2 = []
    for i in range(0, len(lst), 2):
        out1.append(lst[i])
    for i in range(0, len(lst) - 1, 2):
        out2.append(lst[i + 1])
    return (out1, out2)
