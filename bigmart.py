from statistics import mean

def bigmart():
	from random import randrange
	import pandas as pd
	import numpy as np

	data = pd.read_csv("train-clean.csv")

# Bar chart for Item_Outlet_Sales vs. Outlet_Establihsment_Year

print(set(df["Outlet_Establishment_Year"]))
plt.bar(df["Outlet_Establishment_Year"], df["Item_Outlet_Sales"], align="center")

print(set(df[df["Outlet_Establishment_Year"].isnull()]["Outlet_Identifier"].values))

# Find the mean of Item_Weight for each Item_Type
type_weight_dict = {}
for itemtype in set(df["Item_Type"]):
	type_weight_dict[itemtype] = mean([x for x in df["Item_Weight"] if ])
print(type_weight_dict)

if __name__ == "__main__":
	bigmart()