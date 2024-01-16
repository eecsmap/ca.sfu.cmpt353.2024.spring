import numpy as np
import os

current_dir = os.path.dirname(__file__)
data_file = os.path.join(current_dir, "monthdata.npz")
data = np.load(data_file)
totals = data["totals"]
counts = data["counts"]

# get the city had the lowest total precipitation over the year
print("Row with lowest total precipitation:")
print(np.argmin(np.sum(totals, axis=1)))

# get the average precipitation in these cities
print("Average precipitation in each month:")
# use the count information from counts to calculate the average precipitation
print(np.sum(totals, axis=0) / np.sum(counts, axis=0))

# get the average precipitation in each city
print("Average precipitation in each city:")
# use the count information from counts to calculate the average precipitation
print(np.sum(totals, axis=1) / np.sum(counts, axis=1))

# get the quarterly precipitation totals for each city
print("Quarterly precipitation totals:")
print(np.reshape(totals, (9, 4, 3)).sum(axis=2))
