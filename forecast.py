import pandas as pd

data = {"City": ["Pune", "Kochi", "Jaipur"], "Temperature": [29, 31, 26]}
df = pd.DataFrame(data)
print(df)
print("Average Temperature:", df["Temperature"].mean())
