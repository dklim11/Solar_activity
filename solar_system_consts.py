import numpy as np
import matplotlib.pyplot as plt

#Consts:
G = 6.6743  # 10**(-11) m^3/(kg*c^2)
name = ['Sun', 'Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']
mass = [1.99*10**6, 0.32, 4.87, 5.98, 0.64, 1900, 569, 87, 103, 5]              # 10**(24) kg
radius = [0, 57.9, 108.2, 149.6, 227.9, 778.6, 1433.7, 2870.4, 4491.1, 5868.9]  # 10**(9) m

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
print(mass)
print(radius)
print(name[1:])
print("power:", power)
print("min_cntr = ", min_cntr, "max_cntr = ", max_cntr)
print(mass[5]*radius[5]/np.sum(mass))








