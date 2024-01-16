import pandas as pd
import os

current_dir = os.path.dirname(__file__)
data_file = os.path.join(current_dir, "totals.csv")
totals = pd.read_csv(data_file).set_index(keys=["name"])
data_file = os.path.join(current_dir, "counts.csv")
counts = pd.read_csv(data_file).set_index(keys=["name"])

print("City with lowest total precipitation:")
print(totals.sum(axis=1).idxmin())

print("Average precipitation in each month:")
print(totals.sum(axis=0) / counts.sum(axis=0))

print("Average precipitation in each city:")
print(totals.sum(axis=1) / counts.sum(axis=1))
