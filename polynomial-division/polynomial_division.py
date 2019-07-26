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
    print(terms)
    return terms


def get_terms_powers(terms):
    powers = []
    for term in terms:
        print(term)
        if "x" in term:
            power = term[-1]
            if power == "x":
                power = 1
            powers.append(int(power))
    powers.sort(reverse=True)
    print(powers)
    return powers


def insert_missing_powers(terms, powers):

    for power in powers


'''
//
  $t = 0;
  $higherx = $sums[0];
  $lowerx = $sums[1];
  $c = count($sums) - 1;
  //print_r($terms);
  while ($t<$sums[0]-1){
    if (($higherx-$lowerx)!=1){
      $x_pow  = $higherx-1;
      array_splice($terms, $t+1, 0, "0x$x_pow");
      $higherx = $x_pow;
      $lowerx = $sums[1];
    } else {
      $higherx = $lowerx;   
      $lowerx = $sums[$t+2]; 
    }  
    $t++;
  }

'''

san = sanitize("x3+3x2-9x+2")
terms = get_terms(san)
get_terms_powers(terms)
