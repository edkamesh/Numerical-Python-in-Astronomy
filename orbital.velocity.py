from math import pi,sqrt
from astropy.constants import M_sun
from scipy.constants import G,au,year
Radius= int(input("Enter the value of radius in radians (r):"))
TimePeriod= int(input("Enter the value of timr  period in seconds (P):"))

velocity= (2*3.14*Radius)/TimePeriod
print("The velocity is",velocity,"km/s")
