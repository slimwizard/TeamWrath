import os
from stat import *
import ftplib

files = []
#Open ftp connection
ftp = ftplib.FTP('jeangourd.com','anonymous','password')
temp = ''
test = ftp.nlst()
ftp.cwd("10") #changes the current directory
line = ftp.retrlines("LIST",files.append) #appends all the files the files list

for i in range(len(files)): #formats the Files List 
    files[i] = files[i][0:10]
    
print(files)
ftp.close()