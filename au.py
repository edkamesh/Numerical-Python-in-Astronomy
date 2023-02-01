from math import pi,sqrt
from astropy.constants import M_sun
from scipy.constants import G,au,year

print("1 au =", au, "m")
print("1 yr =", year, "s")

radius = 10*au
print("\nradial distance = {:.1f} au".format(radius/au))

 # Kepler’s third law
period = 2*pi * sqrt(radius**3/(G*M_sun.value))
print("orbital period = {:.4f} yr".format(period/year))
velocity = 2*pi * radius/period # velocity in m/s
print("orbital velocity = {:.2f} km/s".format(1e-3*velocity))