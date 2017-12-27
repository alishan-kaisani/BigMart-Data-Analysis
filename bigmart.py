def bigmart():
	from random import randrange
	import pandas as pd
	import numpy as np

	data = pd.read_csv("train-clean.csv")

# Find the mean of Item_Weight for each Item_Type
type_weight_dict = {}
for itemtype in set(df["Item_Type"]):
	item_df = df[df["Item_Type"] = itemtype]
	type_weight_dict[itemtype] = item_df["Item_Weight"].mean()
print(type_weight_dict)

if __name__ == "__main__":
	bigmart()