# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



#Collecting data
building_width = int(input("Enter building width in meters:"))
building_length = int(input("Enter building height in meters:"))
pv_width = int(input("Enter panel width in milimeters:"))
pv_height = int(input("Enter panel height in milimeters:"))
pv_power = int(input("Enter PV peak power per unit area:"))
roof_angle = int(input("Enter roof angle in degrees:"))


#Building area in meters
building_area = building_width * building_length
#Panel area in millimetres
panel_area = pv_width * pv_height / 1000000


#Panel peak capacity
peak_capacity = pv_power * panel_area

#Maximum number of panels theoretically possible
panel_number = building_area / panel_area

#Peak power possible for the building
peak_power_possible = panel_number * peak_capacity

print(building_area)
print(panel_area)
#########print(peak_capacity)
print(panel_number)
print(peak_power_possible)

#Calculating roof angle
import numpy as np
#Run is half of the total width of the building
run = building_width / 2
roof_angle = run / np.cos(roof_height)
print(f"The angle of the roof is " + str(roof_height) + " degrees.")


#roof_angle (deg)