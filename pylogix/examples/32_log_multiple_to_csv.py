'''
the following import is only necessary because eip.py is not in this directory
'''
import sys
sys.path.append('..')

'''
We're going to log a few tag values 10
times to a CSV file

For the first row, we'll write tag names,
then log each set of values with each read
'''
import csv
from pylogix import PLC
import time

with PLC() as comm:
    comm.IPAddress = '192.168.113.30'

    tags = ['Winder_Accum_length', 'WInder_BuildUpRatio', 'Winder_BuildUpRatioRec', 'Winder_CalcEnblThresh_FPM', 'WInder_CalcUpdate_Rev', 'WInder_Constant_RPMperFPM', 'WInder_DiamCalc_in', 'Winder_Diameter_KPP', 'Winder_Diameter_KPS', 'Winder_Diameter_WLDP', 'Winder_Diameter_WLDS', 'Winder_DiamFR_in', 'WInder_DiamMeas_in', 'Winder_DiamMinEC_in', 'Winder_DiamRate_inRev', 'Winder_FR_Position_Feedback', 'Winder_GearRatio', 'Winder_IP_Output', 'Winder_Jog_AccDec_Rate', 'Winder_JogFwd_Reference', 'Winder_JogRev_Reference', 'Winder_KPP_Array', 'Winder_KPs_Array', 'Winder_Length_Cal', 'Winder_Line_speed_Ref', 'Winder_Norm_AccDec_Rate', 'Winder_Position_Loop_Error', 'Winder_Position_Vernier', 'Winder_RadiusCalc_ft', 'Winder_Ramped_speed_FPM', 'Winder_Ramped_speed_FPS', 'Winder_Scaled_FPM', 'Winder_ServoOutput', 'Winder_spd_FB', 'Winder_SpeedMotor_RPM', 'Winder_Tension_Loop_Error', 'Winder_Tension_Vernier', 'Winder_Total_length', 'Winder_WLDP_Array', 'Winder_WLDS_Array', 'Winder_Wound_length'] 

    with open('32_log.csv', 'w') as csv_file:
        csv_file = csv.writer(csv_file, delimiter=',', lineterminator='\n', quotechar='/', quoting=csv.QUOTE_MINIMAL)
        csv_file.writerow(tags)
        for i in range(10):
            values = comm.Read(tags)
            csv_file.writerow(values)
            time.sleep(.25)
