'''
Purpose:    Tests for the List Potpourri assignment
Author:     Janet Davis
Date:       October 24, 2017
'''

from list_potpourri import *

def test_maximum():
    print("Testing the maximum function")
    # Common cases
    assert maximum([5, 4, 3, 17, 1, 2]) == 17
    # Boundary cases
    assert maximum([17, 1, 2, 3]) == 17
    assert maximum([1, 2, 3, 17]) == 17
    assert maximum([17]) == 17
    # Corner cases
    assert maximum([-2, 0, -1,  -4, -3]) == 0
    assert maximum([-2, -1, -4, -3]) == -1
    print("All tests pass!")

def test_closest_to_zero():
    print("Testing the closest_to_zero function")
    # Common cases
    assert closest_to_zero([2,3,1,5,4]) == 1
    assert closest_to_zero([-2, 3,-1,-5,4]) == -1
    # Boundary cases
    assert closest_to_zero([1, 5, 4, 2, 3]) == 1
    assert closest_to_zero([-2, 5, -4, 3, -1]) == -1
    assert closest_to_zero([5,3,0,1,2,4]) == 0
    assert closest_to_zero([5]) == 5
    print("All tests pass!")

def test_safe_sum():
    print("Testing the safe_sum function")
    # Common cases
    assert safe_sum([1, 'apple', 2, 3, 'banana']) == 6
    assert safe_sum([0.5, 0.01, 'q']) == 0.51
    # Corner cases
    assert safe_sum(['apple', 'banana']) == 0
    assert safe_sum([])== 0
    print("All tests pass!")

def test_join_lists():
    print("Testing the join_lists function")
    # Common cases
    assert join_lists([[1,2],[3,4,5],[6,7]]) == [1,2,3,4,5,6,7]
    # Boundary cases
    assert join_lists([[1,2,3]]) == [1,2,3]
    # Corner cases
    assert join_lists([]) == []
    assert join_lists([[],[],[]]) == []
    print("All tests pass!")
 
def test_riffle():
    print("Testing the riffle function")
    # Common cases
    assert riffle([1,2,3],['a','b','c']) == [1,'a',2,'b',3,'c']
    assert riffle([1,2,3,4,5],['a','b','c']) == [1,'a',2,'b',3,'c',4,5]
    assert riffle([1,2,3],['a','b','c','d','e']) == [1,'a',2,'b',3,'c','d','e']
    # Boundary cases
    assert riffle([1],['a']) == [1, 'a']
    assert riffle([1,2,3],[]) == [1,2,3]
    assert riffle([],['a','b','c']) == ['a','b','c']
    assert riffle([],[]) == []
    print("All tests pass!")

def test_unriffle():
    print("Testing the unriffle function")
    # Common cases
    assert unriffle([1,'a',2,'b',3,'c']) == ([1,2,3], ['a','b','c'])
    # Boundary cases
    assert unriffle([1,'a']) == ([1], ['a'])
    assert unriffle([1]) == ([1],[])
    assert unriffle([]) == ([],[])
    print("All tests pass!")

def main():
    # Uncomment lines below to enable tests
    #test_maximum()
    #test_closest_to_zero()
    #test_safe_sum()
    #test_join_lists()
    #test_riffle()
    #test_unriffle()

main()
