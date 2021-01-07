# -*- coding: utf-8 -*-
"""
Author username(s): moenchlm
Date: 9/10/2020
Assignment/problem number: P2
Assignment/problem title: An Interesting Assignment

RESUBMIT:
    I am including this file in my resubmission of P2, but I made no changes to it.
"""

"""
Principal amount (initial investment);
Annual nominal interest rate (as a decimal);
Number of times the interest is compounded per year;
Number of years.
The program should calculate and print the final amount of the investment, with interest,
after the specified number of years have elapsed.

Note: Your program should ask for the inputs in the order specified.
Failure to following this ordering will result in some point deduction.

Hint: The formula for computing compound interest is given in exercise 2.4.4.
"""
principal = int(input("What was your loan's initial value? "))

rate = float(input("What is your annual nominal interest rate (as a decimal, not a percentage)? "))

if rate > 1:
    print("Are you sure your interest rate is", rate * 100, "?")

compoundfreq = int(input("How many times will your interest be compounded each year? "))

years = int(input("How many years has your loan been accruing interest? "))

total_loan_amt = principal * ((1 + (rate/compoundfreq)) ** (compoundfreq*years))

print("The total value of your loan is now $", total_loan_amt)