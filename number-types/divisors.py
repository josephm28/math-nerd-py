#
# Get and work with the divisors of a number
#
import math


class Find:
    def __init__(self, num):
        self.num = num
        self.find_divisors()
        self.proper_sum = sum(self.proper_divisors)

    def find_divisors(self):
        # get divisors
        divisors = []
        sqrt = math.sqrt(self.num)
        be_inclusive = sqrt+1
        be_int = math.floor(be_inclusive)
        for x in range(2, be_int):
            quotient = self.num/x
            if quotient.is_integer():
                divisors.append(int(quotient))
                if x != quotient:
                    divisors.append(x)
        if self.num != 1:
            divisors.append(1)
        # sort by smallest to greatest
        divisors.sort()
        # Proper divisors do not include the number itself
        self.proper_divisors = divisors
        # Divisors include the number itself
        self.divisors = divisors.copy()
        self.divisors.append(self.num)
