import math

n=int(input("Enter the value of N (0-364): "))
theta=360/365.24
e_not=math.radians(23.44)

delta= -math.asin(math.sin(e_not)*math.cos(theta*(n+10)))
print("THE DECLINATION OF SUN IS ","{:.2f}".format(delta),"degrees")

