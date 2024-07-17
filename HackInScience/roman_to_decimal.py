"""
I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, and M = 1000.
"""

def value(v):
    if (v == 'I'):
        return 1
    if (v == 'V'):
        return 5
    if (v == 'X'):
        return 10
    if (v == 'L'):
        return 50
    if (v == 'C'):
        return 100
    if (v == 'D'):
        return 500
    if (v == 'M'):
        return 1000
    return -1

def from_roman_numeral(roman_numeral):
    res = 0
    i = 0
 
    while (i < len(roman_numeral)):
 
        # Getting value of symbol s[i]
        s1 = value(roman_numeral[i])
 
        if (i + 1 < len(roman_numeral)):
 
            # Getting value of symbol s[i + 1]
            s2 = value(roman_numeral[i + 1])
 
            # Comparing both values
            if (s1 >= s2):
 
                # Value of current symbol is greater
                # or equal to the next symbol
                res = res + s1
                i = i + 1
            else:
 
                # Value of current symbol is greater
                # or equal to the next symbol
                res = res + s2 - s1
                i = i + 2
        else:
            res = res + s1
            i = i + 1
 
    return res




print(from_roman_numeral('XX'))
print(from_roman_numeral('CD'))