# math-nerd-py

A collection of math problems solved by Python scripting.

1. Number Types
2. Polynomial Division

### Requirements

```
Python (I use 3.7.4)
```

Know-how on running a python script

### Usage

Each sub-project has an examples file which runs several example function on how to utilize the various scripts. Start there, and ask questions!

### Problem Solving

#### Number Types

Example: Find numbers by type in range

```
find_by_type(0, 100, "Prime")
```

Result:

```
Looking at Prime from 0 to 100 : [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
```

Example: Find perfect numbers and show details for numbers in range

```
def find_perfects(start, end):
    for x in range(start, end):
        test = NumberType(x)
        if(test.type == "Perfect"):
            test.show_rundown()
find_perfects(0, 10000)
```

Result:

```
Looking at number:       6
        Divisors:        [1, 2, 3, 6]
        Proper Divisors: [1, 2, 3]
        Type:            Perfect
Looking at number:       28
        Divisors:        [1, 2, 4, 7, 14, 28]
        Proper Divisors: [1, 2, 4, 7, 14]
        Type:            Perfect
Looking at number:       496
        Divisors:        [1, 2, 4, 8, 16, 31, 62, 124, 248, 496]
        Proper Divisors: [1, 2, 4, 8, 16, 31, 62, 124, 248]
        Type:            Perfect
Looking at number:       8128
        Divisors:        [1, 2, 4, 8, 16, 32, 64, 127, 254, 508, 1016, 2032, 4064, 8128]
        Proper Divisors: [1, 2, 4, 8, 16, 32, 64, 127, 254, 508, 1016, 2032, 4064]
        Type:            Perfect
```

#### Polynomial Division

Example: Polynomial: x3+3x2-9x+2; Divisor: 2x-5

```
PolynomialDivision("x3+3x2-9x+2", "2x-5")
```

Output:

```
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
```

### License

This code is distributed under the MIT license. See [LICENSE.md](LICENSE.md)
for more details.
