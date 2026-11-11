import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("weather.csv")
df.plot(x="City", y="Temperature", kind="bar")
plt.show()
