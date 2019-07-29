import re
import math


def get_r_and_yeild_multiplier(divisor):
    # take apart the divisor to get the
    # r factor (for calculating the division yields) and
    # the yield multiplier (for calculating the new-term coefficients)
    divisor_w_o_plus = re.sub(r'(\w)\+(\w)', r'\1--\2', divisor)
    split_by = "x-" if "x-" in divisor_w_o_plus else "x"
    divisor_parts = divisor_w_o_plus.split(split_by)

    # check the divisor, if the first char is not x,
    if divisor[0] != "x":
        # get the x coefficient; e.g. 5x-2 => [5,-2] => 5
        divisor_x_multiplier = float(divisor_parts[0])
        # if the x coefficient is simply "-", then set to -1; e.g. -x-4 => [-, -4] => - => -1
        if(divisor_x_multiplier == "-"):
            divisor_x_multiplier = -1
        yield_multiplier = 1 / int(divisor_x_multiplier)
    else:
        # leads with "x", so no coefficient
        divisor_x_multiplier = 1
        yield_multiplier = 1

    # 5x-10 => [5, -10] => -10 => -10/5 => -2
    if len(divisor_parts) > 1 and divisor_parts[1] != "":
        divisor_num = float(divisor_parts[1])
    else:
        divisor_num = 0
    r = float(divisor_num / divisor_x_multiplier)
    return r, yield_multiplier


def get_yields(coefs, r):
    # get the coefficient yeilds when multiplying by r and adding across
    # the "upside down" division
    yields = []
    old_coef = coefs[0]
    for i in range(1, len(coefs)):
        yields.append(old_coef)
        old_coef = coefs[i] + old_coef * r  # r = 1?
    yields.append(old_coef)
    return yields


# def before_dividing(yields):
#     count = len(yields)
#     results = []
#     for i in range(0, count):
#         power = count-i-2
#         if power > 0:
#             if power == 1:
#                 res = str(yields[i]) + "x"
#             else:
#                 res = str(yields[i])+"x"+str(power)
#         else:
#             res = str(yields[i])
#         results.append(res)
#     return results


def divide_poly(yields, yield_multiplier):
    # divide the yeilds to get the new coefficients and powers
    count = len(yields)
    results = []
    for i in range(0, count):
        term = ''
        # because the last two entries in the yeilds list are [count] = remainder; [count-1] = x^0
        # use i because it decreases to the right
        power = count-i-2
        #print(yield_multiplier, "*", yields[i])
        # multiply the yield by the yield multiplier to get the new coefficient
        multiplier_res = str(abs(round(yield_multiplier * yields[i], 3)))
        # use if this is the remainder
        remainder = str(abs(round(yields[i], 3)))
        # if the term has an x component
        if power > 0:
            # create the term
            sign = "" if float(multiplier_res) > 0 else "-"
            multiplier = "" if float(multiplier_res) == 1 else multiplier_res
            term = sign + multiplier + "x"
            if (power != 1):
                term += str(power)
        else:
            # Remainder - the last yield
            if yields[i] == yields[count - 1]:
                if abs(yields[i]) != 0:
                    # if the yield is not zero
                    term = "" if yields[i] > 0 else "-"
                    term += remainder
                else:
                    # If the yield is zero, there is no remainder
                    term = ""
            else:
                term = "" if float(multiplier_res) > 0 else "-"
                term += multiplier_res
        results.append(term)
    return results
