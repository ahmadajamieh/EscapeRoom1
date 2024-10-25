import numpy as np

#Room 10: Discover the Hidden Algorithm - Classify the New Machine


data = np.array([[2, 4], [4, 6], [5, 9], [7, 10]])
labels = ['Normal', 'Warning', 'Maintenance Needed', 'Fault']

new_machine = np.array([5, 8])

distances = np.linalg.norm(data - new_machine, axis=1)

nearest_index = np.argmin(distances)

classification = labels[nearest_index]

print(f"The new machine is classified as: {classification}")
