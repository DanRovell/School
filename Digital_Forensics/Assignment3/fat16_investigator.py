#Investigating a File System
#Author: Daniel Rovell
#CSC 443-001

import sys
from binascii import hexlify

path = sys.argv[1]
f = open(path, 'rb').read()

def findBootSectorBytes(f):
    for i in range(0, len(f)):
        x = f[i:i+2]
        if x == b'\x55\xAA':
            return i+2

def findBytesPerSector(f):
    temp = hexlify(f[11:13])
    a,b = temp[2:4], temp[0:2]
    bootSectorBytes = int((a + b), 16)
    return bootSectorBytes

def findSectorsInClusters(f):
    temp = hexlify(f[14])
    sectorsInClusters = int(temp, 16)
    return sectorsInClusters

def findReservedSectors(f):
    temp = hexlify(f[14:16])
    a,b = temp[2:4], temp[0:2]
    reservedSectors = int((a + b), 16)
    return reservedSectors

def findNumOfFATs(f):
    temp = hexlify(f[16])
    numOfFATs = int(temp, 16)
    return numOfFATs

def findMaxOfRootDir(f):
    temp = hexlify(f[17:19])
    a,b = temp[2:4], temp[0:2]
    maxOfRootDir = int((a + b), 16)
    return maxOfRootDir

def findSectorsOfFAT(f):
    temp = hexlify(f[22:23])
    a,b = temp[2:4], temp[0:2]
    sectorsOfFAT = int((a + b), 16)
    return sectorsOfFAT

bootSectorBytes = findBootSectorBytes(f)
bytesPerSector = findBytesPerSector(f)
sectorsInClusters = findSectorsInClusters(f)
reservedSectors = findReservedSectors(f)
numOfFATs = findNumOfFATs(f)
maxOfRootDir = findMaxOfRootDir(f)
sectorsOfFAT = findSectorsOfFAT(f)
firstFATOffset = bootSectorBytes + (bytesPerSector*reservedSectors)
secondFATOffset = bootSectorBytes + (bytesPerSector*reservedSectors) + (bytesPerSector*sectorsOfFAT)
firstRootDirOffset = bootSectorBytes + (bytesPerSector*reservedSectors) + (bytesPerSector*sectorsOfFAT)*2
firstDataBlockOffset = bootSectorBytes + (bytesPerSector*reservedSectors) + (bytesPerSector*sectorsOfFAT)*2 + ((maxOfRootDir*32)/bytesPerSector)
totalSize = len(f) - firstDataBlockOffset

print "The boot block ocupies", bootSectorBytes, "bytes."
print "There are", bytesPerSector, "bytes in each sector."
print "There are", sectorsInClusters, "sectors in each cluster."
print "There are", reservedSectors, "reserved sectors."
print "There are", numOfFATs, "File Allocation Tables present."
print "The Root Directory can hold", maxOfRootDir, "entries."
print "Each FAT occupies", sectorsOfFAT, "sectors."
print "Byte offset of the first FAT is %d." %firstFATOffset
print "Byte offset of the second FAT is %d." %secondFATOffset
print "Byte offset of the first Root Directory is %d." %firstRootDirOffset
print "Byte offset of the first Data Block is %d." %firstDataBlockOffset
print "Total size of the data region is %d bytes." %totalSize
