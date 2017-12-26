def bigmart():
	from random import randrange
	import pandas as pd
	import numpy as np

	data = pd.read_csv("train-clean.csv")

	print(data[data["Item_Type"] = "Starchy_Foods"])
	#This will give you all rows where the type is starchy foods

if __name__ == "__main__":
	bigmart()