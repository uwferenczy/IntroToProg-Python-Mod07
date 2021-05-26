# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Pickling and Error Handling in Python
# ChangeLog (Who,When,What):
# DFerenczy,05.25.2021,Created script
# DFerenczy,05.25.2021,Added pickling code
# DFerenczy,05.25.2021,Added exception code
# ---------------------------------------------------------------------------- #

import pickle
import sys
import datetime

strFileName = input("Please input the name of the .dat file you want to pickle: ")  # The name of the data file
dicStatusCode = {'Status':'Complete', 'Timestamp':str(datetime.datetime.now())}  # A dictionary containing status and timestamp

try:
    assert strFileName[-4:].lower() == '.dat'
except AssertionError:
    print('\nYou did not specify a valid .dat file')
else:
    outfile = open(strFileName, 'wb')
    pickle.dump(dicStatusCode, outfile)
    outfile.close()
    print('\nStatus and timestamp dictionary was successfully pickled to '+strFileName)

try:
    infile = open(strFileName,'rb')
except FileNotFoundError:
    print('Therefore the file cannot be pickled')
else:
    dicUnpickledStatusCode = pickle.load(infile)
    infile.close()
    print('Status and timestamp dictionary was successfully unpickled from ' + strFileName)

try:
    print(f'Pre-Pickled Dictionary: {dicStatusCode}, Pickled then Unpickled Dictionary: {dicUnpickledStatusCode}')
except NameError:
    print('Or re-loaded and compared')

input('\nPress Enter to Quit')