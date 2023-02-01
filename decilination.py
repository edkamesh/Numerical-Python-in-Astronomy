import math
x=int(input("Enter the value of N: "))
i=1
theta=360/365.24
e_not=math.radians(23.44)
print("Day\t Declination\n")
for i in range(0,364):
    if i<x:
        i=i+1
        d=(-math.asin(math.sin(e_not)*math.cos(theta*(i+10))))
        print(i,"\t""{:.3f}".format(d))
 
