from polynomial_division import PolynomialDivision

pd1 = PolynomialDivision("x2+5x+6", "x-1")

pd2 = PolynomialDivision("x3+3x2-9x+2", "2x-5")
'''
-----
Input:
        Polynomial:      x3+3x2-9x+2
        Divisor:         2x-5
Processing:
        Terms:           ['x3', '3x2', '-9x', '2']
        Powers Present:  [3, 2, 1, 0]
        Complete Powers:        3       2       1       0
        Coefficients:           1.0     3.0     -9.0    2.0
        R:               2.5
        Yields:                 1.0     5.5     4.75    13.875
        Yield mult.:     0.5
        Quotient Terms:         0.5x2   2.75x   2.375   13.875
Result:
        Quotient:        0.5x2 + 2.75x + 2.375
        Remainder:       13.875/(2x-5)
-----
'''
pd3 = PolynomialDivision("x3+3x4+2", "2x-5", False)
print(pd3.quotient, pd3.remainder)

# pd4 = PolynomialDivision("6x", "2")
# print(pd4)
