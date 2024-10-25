import numpy as np

#Room 9: Data Normalization - Prepare Sensor Data for Comparison

def transform(data):
    min_val = min(data)
    max_val = max(data)
    
    
    normalized_data = [(x - min_val) / (max_val - min_val) for x in data]
    
    return normalized_data

sensor_data = [500, 1200, 3000, 8000]

normalized_data = transform(sensor_data)

print(f"Normalized data: {normalized_data}")