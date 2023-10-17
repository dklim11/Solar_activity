import numpy as np
import matplotlib.pyplot as plt

# Consts:
G = 6.6743  # 10**(-11) m^3/(kg*c^2)
name = ['Sun', 'Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']
mass = [1.99*10**6, 0.32, 4.87, 5.98, 0.64, 1900, 569, 87, 103, 5]              # 10**(24) kg
mass_ = [0.3329*10**6, 0.055274, 0.815005, 1, 0.012300, 0.10745, 317.83, 95.159, 14.500, 17.204, 0.0025]
radius = [0, 57.9, 108.2, 149.6, 227.9, 778.6, 1433.7, 2870.4, 4491.1, 5868.9]  # 10**(9) m (distance to sun)
radius_ = [0, 0.38710, 0.72333, 1.00001, 1.52363, 5.20441, 9.58378, 19.18722, 30.02090, 39.23107]   # a.e
e = [0, 0.20564, 0.00676, 0.01672, 0.09344, 0.04890, 0.05689, 0.04634, 0.01129, 0.24448]    # eccentricity
power = [0]*9

for i in range(9):
    power[i] = (G * mass[i+1] * mass[0]) / (radius[i+1] ** 2)

# center of mass of the planets from the Sun:
min_cntr = 0
max_cntr = 0
for i in range(9):
    if i == 4:
        min_cntr += -(mass[i+1] * radius[i+1]) / np.sum(mass)
    else:
        min_cntr += (mass[i + 1] * radius[i + 1]) / np.sum(mass)

    max_cntr += (mass[i+1] * radius[i+1]) / np.sum(mass)

print(name)
print("10**24 kg=  ", mass)
print("mass of Earth=   ", mass_)
print("distance to Sun=  ", radius)
print("distance in a.e=  ", radius_)
print("eccentricity", e)
print(name[1:])
print("power:  ", power)
print("min_cntr = ", min_cntr, "max_cntr = ", max_cntr)









