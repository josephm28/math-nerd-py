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

import divisors
import terms
import utils


class PolynomialDivision:

    def __init__(self, polynomial, divisor, verbose=True):
        # santize the input - remove spaces
        self.polynomial = utils.sanitize(polynomial)
        self.divisor = utils.sanitize(divisor)
        self.verbose = verbose

        if "x" not in self.polynomial:
            self.throw_no_x("polynomial")
        elif "x" not in self.divisor:
            self.throw_no_x("divisor")

        self.log_work("\n-----")
        self.log_work("Input:")
        self.log_work("\tPolynomial:\t", self.polynomial)
        self.log_work("\tDivisor:\t", self.divisor)
        self.log_work("Processing:")
        # get the coefficients of the polynomial
        orderedCoefs = self.process_polynomial()
        # divide the polynomial through long division
        results_divide = self.process_divisor(orderedCoefs)
        self.quotient, self.remainder = self.combine_result(results_divide)
        self.log_work("Result:")
        self.log_work("\tQuotient:\t", self.quotient)
        self.log_work("\tRemainder:\t", self.remainder)
        self.log_work("-----")

    def log_work(self, *args, **kwargs):
        if(self.verbose):
            print(*args, **kwargs)

    def throw_no_x(self, which):
        print('>>>> ERROR')
        print('There is no x term in the '+which +
              '. Please make sure to use x as the variable')
        print('<<<<')
        raise ValueError('There is no x term in the '+which + '.')

    def process_polynomial(self):
        poly_terms = terms.get(self.polynomial)
        self.log_work("\tTerms:\t\t", poly_terms)
        powers = terms.get_powers(poly_terms)
        self.log_work("\tPowers Present:\t", [*powers.keys()])
        powers = terms.insert_missing_powers(poly_terms, powers)
        power_keys = [*powers.keys()]
        power_keys.sort(reverse=True)
        self.log_work("\tComplete Powers:", *power_keys, sep='\t')
        coefs = terms.get_coefficients(powers.values())
        orderedCoefs = terms.order_coefficients(coefs, powers)
        self.log_work("\tCoefficients:\t", *orderedCoefs, sep='\t')
        return orderedCoefs

    def process_divisor(self, orderedCoefs):
        r, yield_multiplier = divisors.get_r_and_yeild_multiplier(self.divisor)
        self.log_work('\tR:\t\t', r)
        yields = divisors.get_yields(orderedCoefs, r)
        self.log_work("\tYields:\t\t", *yields, sep='\t')
        # divisors.before_dividing(yields)
        self.log_work("\tYield mult.:\t", yield_multiplier)
        results_divide = divisors.divide_poly(yields, yield_multiplier)
        self.log_work("\tQuotient Terms:\t", *results_divide, sep='\t')
        return results_divide

    def combine_result(self, results_divide):
        # combine the new terms into the quotient and the remainder
        quotient = results_divide[0]
        remainder = ''
        count = len(results_divide)
        for i in range(1, count):
            if i < count-1:
                # if i == count-1 and results_divide[i] != "":
                #     quotient += " + " + \
                #         results_divide[i]+"/("+self.divisor+")"
                # else:
                quotient += " + " + str(results_divide[i])
            else:
                if i == count-1 and results_divide[i] != "":
                    remainder = str(
                        results_divide[i])+"/("+self.divisor+")"
                else:
                    remainder = str(results_divide[i])
        return quotient, remainder
