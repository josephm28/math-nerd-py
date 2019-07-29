#
# Functions for processing the terms of a polynomial
# Getting terms, powers, and coefficients
#
import re


def get(polynomial):
    # Get the terms of a polynomial
    # convert '-' to '+-' for easier splitting into terms
    poly_w_o_minus = re.sub(r'(\w)\-(\w)', r'\1+-\2', polynomial)
    # Split poly_w_o_minus into terms
    terms = poly_w_o_minus.split("+")
    return terms


def get_powers(terms):
    # Get the x power associated with each term
    powers = {}
    for term in terms:
        if "x" in term:
            power = term[-1]
            if power == "x":
                power = 1
            powers[int(power)] = term
        else:
            powers[0] = term
    return powers


def insert_missing_powers(terms, powers):
    # For processing a polynomial, each term should be present
    # Fill in the missing powers down to x^0
    power_values = [*powers]
    power_values.sort(reverse=True)
    # start with the greatest power
    greatest = power_values[0]
    # need to go all the way to 0 as a power, so range -1
    for power in range(greatest, -1, -1):
        # add the power if it's not there already
        if power not in power_values:
            powers[power] = "0x"+str(power)
    return powers


def get_coefficients(terms):
    # get the coefficient of each term, i.e. what is before the x in the term
    coefs = {}
    for term in terms:
        if "x" in term:
            if term[0] == "x":
                coefs[term] = 1
            else:
                parts = term.split('x')
                coefs[term] = parts[0]
        else:
            coefs[term] = term
    return coefs


def order_coefficients(coefs, powers):
    # order the coefficients by power descending
    power_values = [*powers]
    power_values.sort(reverse=True)
    orderedCoefs = []
    for power in power_values:
        orderedCoefs.append(float(coefs[powers[power]]))
    return orderedCoefs
