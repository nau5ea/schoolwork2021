"""
Code to draw a Sierpinski triangle

File name: sierpinski.py
Author username(s): moenchlm
Date: 11/23/2020
"""
import turtle

def middle(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

def baseSerp(tr, p1, p2, p3):
    tr.up()
    tr.goto(p1)
    tr.down()
    tr.goto(p2)
    tr.goto(p3)
    tr.goto(p1)

def sierpinski(tr, p1, p2, p3, depth):
    '''Draws a Sierpinski triangle with corners at p1, p2, and p3.

    Preconditions:
       tr is a turtle object to use to draw with
       p1 is a tuple that is the first corner of the triangle
       p2 is a tuple that is the second corner of the triangle
       p3 is a tuple that is the third corner of the triangle
       depth is an int that is the recursion depth
   
    Postconditions: None
    '''
    assert isinstance(tr, turtle.Turtle), 'tr must be a turtle object'
    assert isinstance(p1, tuple) and len(p1) == 2, 'p1 must be a tuple with 2 elements'
    assert isinstance(p2, tuple) and len(p2) == 2, 'p2 must be a tuple with 2 elements'
    assert isinstance(p3, tuple) and len(p3) == 2, 'p3 must be a tuple with 2 elements'
    assert isinstance(depth, int) and depth >= 0, 'depth must be a non-negative int'
    
    # add your code here.
    tr.up()
    if depth == 0:
        baseSerp(tr, p1, p2, p3)
    else:
        if depth > 0:
            sierpinski(tr, p1, middle(p1, p2), middle(p1, p3), depth - 1)
            sierpinski(tr, middle(p1, p2), p2, middle(p2, p3), depth - 1)
            sierpinski(tr, middle(p1, p3), middle(p2, p3), p3, depth - 1)

        """while i < depth:
            i += 1
            sierpinski(tr, p1, middle(p1, p2), middle(p1, p3), depth - 1)
            sierpinski(tr, p2, middle(p1, p2), middle(p2, p3), depth - 1)
            sierpinski(tr, p3, middle(p3, p2), middle(p1, p3), depth - 1)"""
    # feel free to add other functions if you want

def main():
    t = turtle.Turtle()
    t.hideturtle()
    sierpinski(t, (-100, -60), (0, 100), (100, -60), 4)
    sc = t.getscreen()
    sc.exitonclick()

if __name__ == '__main__':
    main()

