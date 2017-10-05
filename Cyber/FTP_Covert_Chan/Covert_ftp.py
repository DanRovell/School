import ftplib
import sys


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


ftp = ftplib.FTP('jeangourd.com','anonymous')

data = []
if len(sys.argv) != 2:
    ftp.cwd('7')
elif sys.argv[1] == '10':
    ftp.cwd('10')
ftp.dir(data.append)
ftp.quit()

count = 0
print len(data)
for i in range(0,len(data)):
    temp = data[i]
    temp = temp[:10]
    if temp[0] != '-' or temp[1] != '-' or temp[2] != '-':
        count +=1
    data[i] = temp
print count
num = len(data)-(count -1)

converted = [0]*(num-10)
x = 0
i = 0
while i <= len(converted):
    temp = data[i]
    print temp
    if temp[0] == '-' and temp[1] == '-' and temp[2] == '-':
        converted[x] = temp
        i+=1
        x+=1
    else:
        i+=1
print "#############"
for line in converted:
    print line
