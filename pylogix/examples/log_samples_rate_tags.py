'''
the following import is only necessary because eip.py is not in this directory
'''
import sys
import os
sys.path.append('..')
samples = sys.argv[1]
samples = int(samples)
rate = sys.argv[2]
rate = float(rate)
filename = sys.argv[3]

dirpath = os.getcwd()
filepath = dirpath + '\{}'.format(filename)
with open(filepath, encoding='utf-16') as f:
    taglist = f.read()
    tags = '[' + taglist.strip() + ']'

'''
We're going to log a few tag values 10
times to a CSV file

For the first row, we'll write tag names,
then log each set of values with each read
'''

import csv
from pylogix import PLC
import time
from datetime import datetime
import ast

with PLC() as comm:
    comm.IPAddress = '192.168.113.30'

    tags = ast.literal_eval(tags)
    print(filename)

    now = datetime.now()
    now = now.strftime('%d_%m_%Y %H_%M_%S')
    with open(str(filename) + ' ' + now + '{}'.format('.csv'), 'w') as csv_file:
        csv_file = csv.writer(csv_file, delimiter=',', lineterminator='\n', quotechar='/', quoting=csv.QUOTE_MINIMAL)
        csv_file.writerow(tags)
        for i in range(samples):
            now = datetime.now()
            now = now.strftime('%d-%m-%Y %H:%M:%S.%f')
            values = comm.Read(tags)
            values = ", ".join( repr(e) for e in values)
            csv_file.writerow([now, values])
            time.sleep(rate)

