'''
the following import is only necessary because eip.py is not in this directory
'''
import sys
import os
sys.path.append('..')
samples = sys.argv[1]
samples = int(samples)
<<<<<<< HEAD
#rate = sys.argv[2]
#rate = float(rate)
testname = sys.argv[2]
=======
rate = sys.argv[2]
rate = float(rate)
>>>>>>> b1fc1739d57a996a1a9c96ab00883ce966fa9e60
filename = sys.argv[3]

dirpath = os.getcwd()
filepath = dirpath + '\{}'.format(filename)
with open(filepath, encoding='utf-16') as f:
    taglist = f.read()
    tags = '[' + taglist.strip() + ']'

'''
We're going to log a few tag values 10
times to a CSV file
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
    now = now.strftime('%d%m%Y%H%M%S')
    with open(str(testname) + '_' + str(filename) + '_' + now + '{}'.format('.csv'), 'w') as csv_file:
        csv_file = csv.writer(csv_file, delimiter=',', lineterminator='\n', quotechar='/', quoting=csv.QUOTE_MINIMAL)
        header = tags[:] 
        header[:0] = ['utc']
        csv_file.writerow(header)
        for i in range(samples):
            now = datetime.now()
            now = now.strftime('%Y-%m-%dT%H:%M:%S.%f')
            values = comm.Read(tags)
            values = ", ".join( repr(e) for e in values)
            csv_file.writerow([now, values])

            # time.sleep(rate)
