#Steg Program

import sys
import os

def convertBinary(data, bitnum, length):
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

####################   Retrieve Byte ################
ByteArray = []
Sentinal = ['\0x00','\0xff','\0x00','\0x00','\0xff','\0x00']
def RetrieveByte(offset, interval, wrapper):
    wrapper = open(wrapper, 'rb')
    extracted = []
    try:
        byte = wrapper.read(1)
        while byte != "":
            ByteArray.append(byte)
            byte = wrapper.read(1)
    finally:
        wrapper.close()
    i = offset
    check = []
    while i < len(ByteArray):
        if len(check) == 6:
            check = []
        check.append(ByteArray[i])
        if check == Sentinal:
            break
        extracted.append(ByteArray[i])
        i+=interval
    extracted = ''.join(extracted)
    print extracted
######################   Retrieve Bit   ##############################
BitArray = []
Sentinal = ['00000000','11111111','00000000','00000000','11111111','00000000']
Sentinal = ''.join(Sentinal)
def RetrieveBit(offset, interval, wrapper):
    wrapper = open(wrapper, 'rb')
    extracted = []
    try:
        byte = wrapper.read(1)
        while byte != "":
            BitArray.append(byte)
            byte = wrapper.read(1)
    finally:
        wrapper.close()
    for i in range(len(BitArray)):
        temp = bin(ord(BitArray[i]))
        BitArray[i] = temp[2:]
    i = offset
    check = []
    while i < len(BitArray):
        if len(check) == len(Sentinal):
            temp = check
            check = ''.join(check)
            if check == Sentinal:
                break
            else:
                check = temp[1:]
        byte = BitArray[i]
        bit = byte[(len(byte)-1):]
        check.append(bit)
        extracted.append(bit)
        i+=interval
    extracted = ''.join(extracted[:(len(extracted)-len(Sentinal))])
    extracted = convertBinary(extracted, 8, len(extracted))

    print extracted

###################   STORE BYTE   ################################
WrapBA = []
HiddenBA = []
Sentinal = ['\0x00','\0xff','\0x00','\0x00','\0xff','\0x00']
def StoreByte(offset, interval, wrapper, hidden):
    new = []
    wrapper = open(wrapper, 'rb')
    try:
        byte = wrapper.read(1)
        while byte != "":
            WrapBA.append(byte)
            byte = wrapper.read(1)
    finally:
        wrapper.close()

    hidden = open(hidden, 'rb')
    try:
        byte = hidden.read(1)
        while byte != "":
            HiddenBA.append(byte)
            byte = hidden.read(1)
    finally:
        hidden.close()

    i = 0
    while i < len(HiddenBA):
        WrapBA[offset] = HiddenBA[i]
        offset+=interval
        i+=1

    i = 0
    while i < len(Sentinal):
        WrapBA[offset] = Sentinal[i]
        offset+=interval
        i+=1

    new = ''.join(WrapBA)
    print new






###################   PARSING   ###################################
args = sys.argv[1:]
method = ''
sor = ''
offset = ''
interval = ''
wrapper = ''
hidden = ''

if args[0] == '-b':
    method = 'byte'
elif args[0] == '-B':
    method = 'Byte'
else:
    print "Expected -b or -B for argument 1.\n"

if args[1] == '-s':
    sor = 'store'
elif args[1] == '-r':
    sor == 'retrieve'
else:
    print "Expected -s or -r for argument 2.\n"

third = args[2]
if third[:2] == '-o':
    offset = int(third[2:])

fourth = args[3]
if fourth[:2] == '-i':
    interval = int(fourth[2:])

fifth = args[4]
if fifth[:2] == '-w':
    wrapper = fifth[2:]
    if not os.path.exists(wrapper):
        print "File does not exist.\n"

if len(args)>5:
    sixth = args[5]
    if sixth[:2] == '-h':
        hidden = sixth[2:]
        if not os.path.exists(hidden):
            print "File does not exist.\n"
###################################################################


RetrieveByte(offset, interval, wrapper)
#RetrieveBit(offset, interval, wrapper)
#StoreByte(offset, interval, wrapper, hidden)
