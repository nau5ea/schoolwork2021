# -*- coding: utf-8 -*-
"""
Author username(s): moenchlm
Date: 20/9/20
Assignment/problem number: P4
Assignment/problem title: Playful Polygons
"""
import turtle
    
#this function chews up side numbers, spits out angles between them
def calc_angle(n_sides):
    return 360/n_sides


def draw_polygon(tortoise, n_sides, side_length):
    angle = calc_angle(n_sides)
    for i in range(n_sides):
        tortoise.left(angle)
        tortoise.forward(side_length)


def spin_polygon(tortoise, n_sides, side_length, angle, n_copies):
    for i in range(n_copies):
        draw_polygon(tortoise, n_sides, side_length)
        tortoise.left(angle)
        
def scale_polygon(tortoise, n_sides, side_length, scale_factor, n_copies):
    for i in range(n_copies):
        draw_polygon(tortoise, n_sides, side_length)
        side_length *= scale_factor
        
def main():
    tortoise = turtle.Turtle()
    # testing calc_angle()
    calc_angle(4)
    # testing draw_polygon()
    draw_polygon(tortoise, 9, 70)
    # testing spin_polygon()
    spin_polygon(tortoise, 4, 50, 30, 5)
    # testing scale_polygon()
    scale_polygon(tortoise, 5, 10, 2, 4)