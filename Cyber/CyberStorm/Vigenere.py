#Daniel Rovell
#CSC 442
#Vigenere Cypher

import sys

######## VIGENERE FUNCTION ########
def Vigenere(plaintext,key, mode):
    x = 0####Counter for key length
    for i in range(0, len(plaintext)):
        if x > (len(key)-1):
            x = 0
        if plaintext[i].islower():
            n = 97####If the letter is lowercase in the plaintext
        else:
            n = 65####If the letter is uppercase in the plaintext
        if not(plaintext[i].isalpha()):
            cyphertext[i] = chr(ord(plaintext[i]))
        else:
            if mode == '-e':####If Encoding
                cyphertext[i] = chr((((ord(plaintext[i])-n) + (ord(key[x])-97))%26)+n)
            elif mode == '-d':####If Decoding
                cyphertext[i] = chr((((ord(plaintext[i])-n) - (ord(key[x])-97))%26)+n)
            x+=1
    return cyphertext

######## MAIN ########
while True:
    mode = sys.argv[1]
    if (mode == '-h'):
        print "Format example for use: Filename.py -e yourkey\nThen enter your text to be encoded(-e) or decoded(-d)."
        sys.exit()
    elif (mode != '-e') and (mode != '-d'):
        print "Please use '-e' for encoding or '-d' for decoding. '-h' can be used for help."
        sys.exit()
    key = (sys.argv[2].lower()).replace(" ", "")
    try:
        plaintext = raw_input()
    except KeyboardInterrupt:#Handle Keyboard Interrupt
        print('\r')
        sys.exit()
    except EOFError:#Handle EOF Error
        print('\r')
        sys.exit()
    cyphertext = [0]*len(plaintext)
    cyphertext = Vigenere(plaintext, key, mode)
    cyphertext = ''.join(cyphertext)
    print cyphertext
