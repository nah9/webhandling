'''
the following import is only necessary because eip.py is not in this directory
'''
import sys
sys.path.append('..')

'''
We're going to log a tag value 10
times to a text file
'''
import csv
from pylogix import PLC
import time

with PLC() as comm:
    comm.IPAddress = '192.168.113.30'
     
    with open('31_log.csv', 'w') as csv_file:
        csv_file = csv.writer(csv_file, delimiter=',', quotechar='/', quoting=csv.QUOTE_MINIMAL)
        for i in range(100):
            value = comm.Read('Program:Winder.Wind_Pos_Step_Ref')
            csv_file.writerow([value])
            time.sleep(1)
