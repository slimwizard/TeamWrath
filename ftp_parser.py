#       Written by Team Wrath:      #
#   Brian Enterkin, Jon Harris,     #
#   Daniel Kumler, Brad Raynaud,    #
# Matthew Rice, Colton Richardson,  #
#       Christopher Smith           #
# Please use Python 3.5.2 or later  #

import sys, ftplib


# Pretty self explanatory, but these are our parameters:
# HOST:                 The desired host you would like to connect to,
# USER:                 The user you wish to connect as,
# PASS:                 The password for that user,
# PORT:                 The port you wish to connect on,
# DIR:                  The target directory to search,
# BIT_ENCODING:         How many bits you want to keep,
# IGNORE_LEADING_BITS:  Ignore first 3 bits if something is present? (True/False)

HOST = "138.47.132.200"
USER = "good"
PASS = "goodGOODgood"
PORT = "8008"
DIR = "/.lookee-here/now-in-here"
BIT_ENCODING = 10
IGNORE_LEADING_BITS = True

# Connect and change to desired directory #
ftp = ftplib.FTP()
ftp.connect(HOST, PORT)
ftp.login(USER, PASS)
ftp.cwd(DIR)

# Init list and add each line output from retrlines('LIST') as entries #
files = []
ftp.retrlines('LIST', files.append)

if (BIT_ENCODING == 7 and IGNORE_LEADING_BITS == True):
    # For each item(string) in files, slice the first 3 bits off and add that result to files_seven #
    files_seven = [file[3:10] for file in files if file[:3] == "---"]
    # Next, replace each character of each item in files_seven with 1 or 0, then string.join and add that back to files_seven #
    files_seven = [''.join('1' if file[i].isalpha() else '0' for file in files_seven for i in range(BIT_ENCODING))]
    # Now the tricky part:
    # We take slices from files_seven in increments of 7 ([0:7], [8:14], etc)
    # For each of those slices, we convert the 7 binary digits to an int and then convert that int value to a character
    # Then that result gets added to a list as an item
    # Finally, we string.join that entire list and write to stdout
    sys.stdout.write(''.join([chr(int([files_seven[0][i:i+7] for i in range(0, len(files_seven[0]), 7)][j], 2)) for j in range(len([files_seven[0][k:k+7] for k in range(0, len(files_seven[0]), 7)]))]) + '\n')

# The following two elifs are the same as above, except for the initial logic (IGNORE_LEADING_BITS = True/False or use BIT_ENCODING = 10) and also
# how we slice the initial string lines read from retrlines('LIST')
elif (BIT_ENCODING == 7 and IGNORE_LEADING_BITS == False):
    files_seven = [file[3:10] for file in files]
    files_seven = [''.join('1' if file[i].isalpha() else '0' for file in files_seven for i in range(BIT_ENCODING))]
    sys.stdout.write(''.join([chr(int([files_seven[0][i:i+7] for i in range(0, len(files_seven[0]), 7)][j], 2)) for j in range(len([files_seven[0][k:k+7] for k in range(0, len(files_seven[0]), 7)]))]) + '\n')

elif BIT_ENCODING == 10:
    files_ten = [file[:10] for file in files]
    files_ten = [''.join('1' if file[i].isalpha() else '0' for file in files_ten for i in range(BIT_ENCODING))]
    sys.stdout.write(''.join([chr(int([files_ten[0][i:i+7] for i in range(0, len(files_ten[0]), 7)][j], 2)) for j in range(len([files_ten[0][k:k+7] for k in range(0, len(files_ten[0]), 7)]))]) + '\n' )
