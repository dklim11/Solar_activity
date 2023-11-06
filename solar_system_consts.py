import numpy as np
import csv
import matplotlib.pyplot as plt

# give angle of turn a planet around Earth, t = sidereal period of a planet, n - current cycle(T_act - time of cycle)
def turn(t, n, T_act):
    turns = (n*T_act / (t/(t - 1)))   # current of turns a planet around Earth
    phi = 2 * np.pi * turns
    return phi


# Consts:
G = 6.6743  # 10**(-11) m^3/(kg*c^2)
name = ['Sun', 'Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']
mass = [1.989*10**6, 0.33022, 4.869, 5.9742, 0.64191, 1898.8, 568.5, 86.625, 102.78, 0.015]              # 10**(24) kg
mass_ = [0.3329*10**6, 0.055274, 0.815005, 1, 0.10745, 317.83, 95.159, 14.500, 17.204, 0.0025]  # in mass of Earth
radius = [0, 57.9, 108.2, 149.6, 227.9, 778.6, 1433.7, 2870.4, 4491.1, 5868.9]  # 10**(9) m (distance to sun)
radius_ = [0, 0.38710, 0.72333, 1.00001, 1.52363, 5.20441, 9.58378, 19.18722, 30.02090, 39.23107]   # a.e
e = [0, 0.20564, 0.00676, 0.01672, 0.09344, 0.04890, 0.05689, 0.04634, 0.01129, 0.24448]    # eccentricity
t = [0, 0.240846, 0.615, 1, 1.881, 11.86, 29.46, 84.01, 164.8, 248.1]   # sidereal period in julian years
power = [0]*9   # gravity power between sun and planet
power_ = [0]*9  # power in earth power:


# center of mass of the planets from the Sun:
min_cntr = 0    # all planets except Jupiter on one hand and Jupiter on another
max_cntr = 0    # all planet on one hand
power[2] = (G * mass[2+1] * mass[0]) / (radius[2+1] ** 2)   # next we divide by it
for i in range(9):
    power[i] = (G * mass[i+1] * mass[0]) / (radius[i+1] ** 2)
    power_[i] = power[i] / power[2]
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
print("power in earth power: ", power_)


# characteristic dependence current sunspots (that we see) in max.activity(depend only on Sun)
# at configuration between Earth and Jupiter
number_turn = [0]*100
activity = [0]*100
num = [0]*100   # numer of cycle (11 years)
for j in range(100):
    num[j] = j
    number_turn[j] = (j*11)/(11.86/10.86)
    number_turn[j] = int(number_turn[j]*100) % 100
    if number_turn[j] >= 50:
        number_turn[j] = 100 - number_turn[j]
    activity[j] = 50 - number_turn[j]


#plt.plot(num, number_turn, '.')
plt.plot(num, activity, 'o')
plt.show()

# more accuracy
sun_act = 15    # some constant that characterize current of sunspots in maximum of solar activity
T_act = 11.03   # period of solar activity, time change of main dipolar magnetic field
n = 30  # current T_act
# angle of turn planet around Earth (in the beginning all angle = 0)
turn_mercury = [0]*n
turn_venus = [0]*n
turn_jupiter = [0]*n
turn_saturn = [0]*n
activity = [0]*n    # current of sunspots
year = [0]*n    # our year
step = 90   # for change phase in the beginning
for j in range(-20, 10):
    turn_mercury[j] = turn(t[1], j+step, T_act)
    turn_venus[j] = turn(t[2], j + step, T_act)
    turn_jupiter[j] = turn(t[5], j + step, T_act)
    turn_saturn[j] = turn(t[6], j+step, T_act)
    activity[j] = (sun_act + 1 + 11.73*np.cos(turn_jupiter[j]) + 0.36*np.cos(turn_mercury[j])
                   + 1.56 * np.cos(turn_venus[j]) + 1.04*np.cos(turn_saturn[j])) * 260/25
    year[j] = 1960 + T_act*j

# graph data and our calculation
X = []
Y = []
with open('SN_ms_tot_V2.0.csv', 'r') as datafile:
    plotting = csv.reader(datafile, delimiter=';')

    for ROWS in plotting:
        X.append(float(ROWS[2]))
        Y.append(float(ROWS[3]))

plt.plot(X, Y)
plt.title('Sunspots')
plt.xlabel('year')
plt.ylabel('current')
plt.plot(year, activity, 'o')
plt.show()








