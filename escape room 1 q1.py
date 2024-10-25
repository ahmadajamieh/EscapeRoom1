import numpy as np

#Room 1: Sensor Data and Basic Operations

temperatures = [23.5 , 25.0 , 22.0 , 26.5 , 24.5]
average_temperatures = sum(temperatures) / len(temperatures)
print(f"The average temperature is: {average_temperatures:.2f}")