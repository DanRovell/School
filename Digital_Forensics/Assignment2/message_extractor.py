#Message Extractor
#Author: Daniel Rovell
#CSC 443-001

from PIL import Image

def decode_binary_string(s): #decode binary string
        return ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))

def ExtractMessage(carrier): #function to extract message
    c_image = Image.open(carrier)
    width, height = c_image.size
    new_array = []
    extracted = []

    for h in range(height):
        for w in range(width):
            ip = c_image.getpixel((w,h))
            new_array.append(ip[1])

    for i in range(len(new_array)): 
        new_array[i] = "{0:b}".format(int(new_array[i]))

    for i in range(len(new_array)):
        x = new_array[i]
        extracted.append(x[len(x)-1:])

    extracted = ''.join(extracted)
    extracted = decode_binary_string(extracted)

    with open('watermark.txt', 'wb') as f:
        f.write(extracted)
    
ExtractMessage('DCIM_2837.png')