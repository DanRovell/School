#File Carving Program
#Author: Daniel Rovell
#CSC 443-001

import sys
import base64

path = sys.argv[1]
f = open(path, 'r')
data = base64.b64decode(f.read())#Decode from base 64

#All of the header and footer values 
jpegHead = b'\xff\xd8\xff\xe0'           
jpegFoot = b'\xff\xd9'
pdfHead = b'\x25\x50\x44\x46'
pdfFoot = b'\x0A\x25\x25\x45\x4F\x46'
gifHead = b'\x47\x49\x46\x38\x39\x61'
gifFoot = b'\x00\x3B'
pngHead = b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A'
pngFoot = b'\x49\x45\x4E\x44\xAE\x42\x60\x82'
zipHead = b'\x50\x4B\x03\x04'

#Function to find the files
def findFile(data, head, foot):
    for i in range(0, len(data)): #For loop to find the header
        x = data[i:i+(len(head))]
        if x == head:
            index1 = i
            break
    
    if head == b'\x50\x4B\x03\x04': #Special case for the Zip file
        found = data[index1:]
    else:
        for i in range(index1, len(data)): #For loop to locate the footer after the header is found
            x = data[i:i+(len(foot))]
            if x == foot:
                index2 = i+(len(foot))
                break
        found = data[index1:index2]
    
    return found

#All of the functon executions to find the files
JPEG = findFile(data, jpegHead, jpegFoot)
PDF = findFile(data, pdfHead, pdfFoot)
GIF = findFile(data, gifHead, gifFoot)
PNG = findFile(data, pngHead, pngFoot)
ZIP = findFile(data, zipHead, 0)#no footer needed for the zip

#Writing all the files with their intended file extensions
with open('JPEG.jpg', 'wb') as f:
    f.write(JPEG)
with open('PDF.pdf', 'wb') as f:
    f.write(PDF)
with open('GIF.gif', 'wb') as f:
    f.write(GIF)
with open('PNG.png', 'wb') as f:
    f.write(PNG)
with open('ZIP.docx', 'wb') as f:
    f.write(ZIP)
