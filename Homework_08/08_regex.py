import re

a = re.compile(r'\+420\d{9}$')
b = re.compile(r'\+420\s\d{3}\s\d{3}\s\d{3}$')
c = re.compile(r'\d{9}$')
d = re.compile(r'\d{3}\s\d{3}\s\d{3}$')

def check(number: int) -> bool:
    match_a = a.match(number)
    match_b = b.match(number)
    match_c = c.match(number)
    match_d = d.match(number)
    print(any((match_a, match_b, match_c, match_d)))

check('+420721010210')
check('+420 721 010 210')
check('721010210')
check('721 010 210')
check('aaf211')
check('420721010210')
check('+420 721010210')