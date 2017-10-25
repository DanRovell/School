#Password Cracker
#Author: Daniel Rovell
#CSC 443-001

import sys, hashlib
from itertools import product
from string import ascii_lowercase

keywords = [''.join(i) for i in product(ascii_lowercase, repeat = 5)] #list of all 5 letter permutations

pword1 = '9aeaed51f2b0f6680c4ed4b07fb1a83c'
pword2 = '172346606e1d24062e891d537e917a90'
pword3 = 'fa5caf54a500bad246188a8769cb9947'

for i in range(0, len(keywords)): #iterate through the keywords and compare their hash to the password hashes
    found = 0
    if pword1 == hashlib.md5(keywords[i]).hexdigest():
        found1 = keywords[i]
        found = found +1
    elif pword2 == hashlib.md5(keywords[i]).hexdigest():
        found2 = keywords[i]
        found = found +1
    elif pword3 == hashlib.md5(keywords[i]).hexdigest():
        found3 = keywords[i]
        found = found +1
    if found == 3:
        break

print(found1, found2, found3)
passwords = ['troll', 'lolol', 'polar'] #the passwords

