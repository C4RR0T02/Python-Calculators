'''
Pseudocode:
Input: Radius and height of cylinder,vaue of pi
Processing: Substitute values into the formula
Output: Area of Cylinder
'''


#Import Modules

import math

#User input

radius = float(input("Radius of cylinder: "))
height = float(input("Height of cylinder: "))
units = str(input("Unit of length: "))

#Formula to calculate Surface Area of Cylinder

A = (2*math.pi*radius*height) + (2*math.pi*(radius**2))

#rounding off of values to 2d.p.
round_A = round(A,2)

#Output

print ("Surface area of cylinder is ",round_A,units,"square when the radius is ",radius,units," and the height is ",height,units,".")
