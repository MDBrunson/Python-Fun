
# Takes starting and ending heights, travel distance, and time to compute the angle to launch at. Also uses mass to give impulse. Assume point mass and neglect air resistance.

from pint import UnitRegistry
import numpy
import time

units = UnitRegistry()
second = units.second
meter = units.meter
foot = units.foot
mile = units.mile
degree = units.degree
radian = units.radian
arctan = numpy.arctan
pi = numpy.pi

wall_start_time = time.time()
process_start_time = time.process_time()

# parameters
mass = 1000 * units.kilogram
xf = (10 * meter)
y0 = 1 * meter
yf = 2000 * meter
ay = -9.8 * meter/second**2
t = .2 * second
# 

# dist from sun to earth: 92.96 million miles
dES = (92960000 * mile).to(meter)
yf = dES


viy = ((-y0 + yf) - .5 * ay * t**2) / t
vix = xf / t
angle = (arctan(viy/vix)).to(degree)
print ('Launch angle: ')
print(angle)

v0 = numpy.sqrt((vix**2 + viy**2))
change_in_momentum = v0 * mass
print("Starting velocity:")
print (v0)
print ("Change in 2d momentum: ")
print(change_in_momentum)
mach = v0.magnitude/343
print('Mach: ')
print(mach)
v0sol = (v0.magnitude/299792458)
print('Fraction of speed of light: ')
print((v0sol))

earth_velocity_shift = change_in_momentum/((6*10**24)*units.kilogram)
print('Earth change in velocity: ')
print(earth_velocity_shift)

wall_end_time = time.time()
wall_time = wall_start_time - wall_end_time
print(wall_time)

process_end_time = time.process_time()
process_time = process_start_time - process_end_time
print(process_time)

