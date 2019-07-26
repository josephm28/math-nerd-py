# Polynomials: Synthetic Division
'''
Synthetic division is a method of polynomial long
division, with less writing and fewer calculations.
It generally applies to division by binomials of
the form x - r.

Use x as the variable (i.e. not y, z, etc.) and make sure to use plus "+" and minus "-" signs, not dashes.
Enter a polynomial with descending powers of x.
    E.g. x3+3x2-9x+2
Enter the binomial divisor.
    E.g. x-5 (binomials of the form 3x-5, -x+12, etc. may also be used)

'''

import math
import re


def sanitize(data):
    if data == None or data == "":
        return False
    # remove the spaces from the data
    data = data.replace(" ", "")
    return data


def get_terms(polynomial):
    # convert '-' to '+-' for easier splitting into terms
    poly_w_o_minus = re.sub(r'(\w)\-(\w)', r'\1+-\2', polynomial)
    # Split poly_w_o_minus into terms
    terms = poly_w_o_minus.split("+")
    print('Terms:', terms)
    return terms


def get_terms_powers(terms):
    powers = {}
    for term in terms:
        # print(term)
        if "x" in term:
            power = term[-1]
            if power == "x":
                power = 1
            powers[int(power)] = term
        else:
            powers[0] = term
    print('Powers', powers)
    return powers


def get_terms_coefficients(terms):
    coefs = {}
    for term in terms:
        # print(term)
        if "x" in term:
            if term[0] == "x":
                coefs[term] = 1
            else:
                parts = term.split('x')
                coefs[term] = parts[0]
        else:
            coefs[term] = term
    print('Coefficients', coefs)
    return coefs


def insert_missing_powers(terms, powers):
    power_values = [*powers]
    power_values.sort(reverse=True)
    greatest = power_values[0]
    # print(greatest)
    for power in range(greatest, 0, -1):
        # print(power)
        if power not in power_values:
            # print(power)
            powers[power] = "0x"+str(power)
    print('Complete Powers', powers)
    return powers


def determine_divisor_details(divisor):
    yield_multiplier = 1
    if divisor[0] != "x":
        divisor_x_multiplier = divisor.split('x')[0]
        if(divisor_x_multiplier == "-"):
            divisor_x_multiplier = -1
        yield_multiplier = 1 / divisor_x_multiplier
    else:
        divisor_x_multiplier = 1

    divisor_w_o_plus = re.sub(r'(\w)\+(\w)', r'\1--\2', divisor)
    # todo - make more robust
    r = int(divisor_w_o_plus.split('x')[1].replace(
        '--', '-')) / divisor_x_multiplier
    print('R', r)
    print('yield_mult', yield_multiplier)
    return r, yield_multiplier


def get_yields(coefs, r):
    divided = []
    old_coef = coefs[0]
    for i in range(1, len(coefs)):
        divided.append(old_coef)
        old_coef = coefs[i] + old_coef * 1  # r = 1?
        # print(old_coef)
    divided.append(old_coef)
    print("Divided", divided)
    return divided


def before_dividing(yields):
    count = len(yields)
    results = []
    for i in range(0, count):
        power = count-i-2
        if power > 0:
            if power == 1:
                res = str(yields[i]) + "x"
            else:
                res = str(yields[i])+"x"+str(power)
        else:
            res = str(yields[i])
        results.append(res)
    print(results)
    return results


divisor = sanitize("x-1")
r, yield_multiplier = determine_divisor_details(divisor)
print('R', r, yield_multiplier)

san = sanitize("x2+5x+6")
terms = get_terms(san)
powers = get_terms_powers(terms)
powers = insert_missing_powers(terms, powers)
coefs = get_terms_coefficients(powers.values())

power_values = [*powers]
power_values.sort(reverse=True)
# print(power_values)
#print('powers', powers)
orederCoefs = []
for power in power_values:
    #print('power', power)
    # print(powers[power])
    orederCoefs.append(int(coefs[powers[power]]))
# print(orederCoefs)
yields = get_yields(orederCoefs, r)
before_dividing(yields)


def divide_poly(yields, yield_multiplier):
    count = len(yields)
    results = []
    for i in range(0, count):
        res = ''
        power = count-i-2
        multiplier_res = yield_multiplier * yields[i]
        multiplier_res_floored = int(math.floor(multiplier_res*100)/100)
        yields_floored = int(math.floor(yields[i]*100)/100)
        if power > 0:
            if power == 1:
                if multiplier_res > 0:
                    if multiplier_res == 1:
                        if i == 0:
                            res = "x"
                        else:
                            res = " + x"
                    else:
                        res = str(multiplier_res_floored)+"x"
                else:
                    if multiplier_res == -1:
                        res = " - x"
                    else:
                        res = " - " + str(abs(multiplier_res_floored))+"x"
            else:
                if multiplier_res > 0:
                    if multiplier_res == 1:
                        if i == 0:
                            res = "x"+str(power)
                        else:
                            res = " + x"+str(power)
                    else:
                        res = str(multiplier_res_floored) + "x"+str(power)
                else:
                    if multiplier_res == -1:
                        if i == 0:
                            res = "-x"+str(power)
                        else:
                            res = " - x"+str(power)
                    else:
                        res = " - " + \
                            str(abs(multiplier_res_floored))+"x"+str(power)
        else:

            if yields[i] == yields[count - 1]:
                if yields[i] > 0:
                    res = yields_floored
                else:
                    res = " - "+str(abs(yields_floored))
            else:
                if(multiplier_res > 0):
                    res = multiplier_res_floored
                else:
                    res = " - "+str(abs(multiplier_res_floored))
        results.append(res)
    print(results)
    return results


results_divide = divide_poly(yields, yield_multiplier)

final_result = results_divide[0]
count = len(results_divide)
for i in range(1, count):
    print(results_divide[i])
    if i < count-1:  # results_divide[i] > 0:
        if i == count-1:
            final_result += " + " + \
                results_divide[i]+"/("+divisor+")"
        else:
            final_result += " + " + str(results_divide[i])
    else:
        if i == count-1:
            final_result += "   "+str(results_divide[i])+"/("+divisor+")"
        else:
            final_result += "   "+str(results_divide[i])

print(final_result)
