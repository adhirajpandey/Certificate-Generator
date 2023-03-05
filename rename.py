import os

DOWNLOAD_FILEFORMAT = '.png'

#readlines from names.txt
with open('names.txt') as f:
    names = f.readlines()

#rename files
for i in range(1, len(names) + 1):
    os.rename('certs/' + str(i) + DOWNLOAD_FILEFORMAT, 'certs/' + names[i-1].strip() + DOWNLOAD_FILEFORMAT)
    print("Renamed ", i)