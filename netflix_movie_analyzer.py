import pandas as pd
dataset=pd.read_csv("C:\\Users\\sushm\\OneDrive\\Desktop\\Pandas\\netflix_titles.csv")
print(dataset)
# show the datasets structure
dataset.info()
# to show the first 10 rows
print("The first 10 rows are\n",dataset.head(10))
# to count movie and tv shows
dataset["type"].value_counts()
movies=dataset[dataset["type"]=="Movie"]
print("The moivie are\n",movies)
# the movies which are released after 2021
dataset[dataset["release_year"] > 2021]
print("Release year after 2021 is:\n",dataset)
dataset[dataset["country"]=="United States"]
print("The movies released by united states are:\n",dataset)
dataset.drop(["description"],axis=1)
print("Drop the null values or descriptions\n",dataset)
dataset.to_csv("After making modifications to the netflix_analyzer the data becomes")
print("After making modifications to the netflix_analyzer the data becomes",dataset)



