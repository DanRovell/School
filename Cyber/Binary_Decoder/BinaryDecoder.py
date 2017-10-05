#Daniel Rovell
#CSC 442
#Binary Decoder

import sys

###### CONVERT BINARY #######
def convertBinary(data, bitnum):
    x = 0
    converted = [0]*(length/bitnum)

    for i in range(0,length, bitnum):
        temp = data[i:i+bitnum]
        temp = str(temp)
        converted[x] = temp
        x += 1

    for i in range(0, len(converted)):
        converted[i] = int(converted[i], 2)
        converted[i] = str(unichr(converted[i]))

    converted = ''.join(converted)
    return converted

###### MAIN ################
data = sys.stdin.readlines()
bitnum = "null"
data = str(data)
converted = [0]
data = data[2:(len(data) -4)]
length = len(data)
print length

if (length%7 == 0 and length%8  == 0):# check if 8 bit or 7 bit #
    bitnum = "both"
elif (length%7 == 0):
    bitnum = 7
elif (length%8 == 0):
    bitnum = 8

if bitnum == "both":# if 8 and 7 bit, convert and print both #
    bitnum = 8
    converted1 = convertBinary(data, bitnum)
    bitnum = 7
    converted2 = convertBinary(data, bitnum)
    print "8bit: ", converted1, ", 7bit: ", converted2
elif bitnum == 8:# if 8 bit, convert and print #
    converted = convertBinary(data, bitnum)
    print converted
elif bitnum == 7:# if 7 bit, convert and print #
    converted = convertBinary(data, bitnum)
    print converted
