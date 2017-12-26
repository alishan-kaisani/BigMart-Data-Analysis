from statistics import mean

def bigmart():
	from random import randrange
	import pandas as pd
	import numpy as np

	data = pd.read_csv("train-clean.csv")

	print(data[data["Item_Type"] = "Starchy_Foods"])
	#This will give you all rows where the type is starchy foods

# Find the mean of Item_Weight for each Item_Type
type_weight_dict = {}
for itemtype in set(df["Item_Type"]):
	type_weight_dict[itemtype] = mean([x for x in df["Item_Weight"] if df["Item_Type"] == itemtype])
print(type_weight_dict)

if __name__ == "__main__":
	bigmart()