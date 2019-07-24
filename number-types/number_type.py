
import divisors


class NumberType:
    def __init__(self, num):
        self.num = num
        self.is_prime = False
        self.divisors = divisors.Find(self.num)
        self.determine_type()

    def show_rundown(self):
        print("Looking at number:\t", self.num)
        print("\tDivisors:\t", self.divisors.divisors)
        print("\tProper Divisors:", self.divisors.proper_divisors)
        print("\tType:\t\t", self.type)

    def determine_type(self):
        if self.num == 0:
            self.type = "Zero"
        elif self.divisors.proper_sum == self.num:
            self.type = "Perfect"
        elif self.divisors.proper_sum > self.num:
            self.type = "Abundant"
        elif self.divisors.proper_sum < self.num:
            if self.divisors.proper_sum == 1:
                self.is_prime = True
            self.type = "Deficient"
