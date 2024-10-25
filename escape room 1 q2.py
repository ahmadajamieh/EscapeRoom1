import numpy as np

#Room 2: Control System Simulation
pressure = int(input("Enter pressure: "))

if pressure < 20:
    print("Pressure is too low! Increasing pressure.")
elif pressure > 80:
    print("Pressure is too high! Reducing pressure.")
else:
    print("Pressure is within the acceptable range. Maintaining current pressure.")