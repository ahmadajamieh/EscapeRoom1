import numpy as np

#Room 4: Supervised Learning - Machine Failure Prediction

def classify_failure(temp, pressure):
    
    if temp > 75 or pressure > 120:
        return "Fail"
    else:
        return "Operational"

temperature = float(input("Enter the temperature: "))
pressure = float(input("Enter the pressure: "))

result = classify_failure(temperature, pressure)

print(f"The machine's status is: {result}")