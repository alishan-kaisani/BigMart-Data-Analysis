def bigmart():
	from random import randrange
	import pandas as pd
	import numpy as np

	data = pd.read_csv("train-clean.csv")

# Bar chart for Item_Outlet_Sales vs. Outlet_Establihsment_Year

print(set(df["Outlet_Establishment_Year"]))
plt.bar(df["Outlet_Establishment_Year"], df["Item_Outlet_Sales"], align="center")

if __name__ == "__main__":
	bigmart()