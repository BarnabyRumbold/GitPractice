# A little data exploration project to practice git
# First import packages
import pandas as pd

# Then import the data itself
path = r"C:\Users\Barna\Downloads\Top 1000 IMDB movies (1).csv"
data = pd.read_csv(path)

# Inspect the data set
print(data.head())
print(data.columns)

# Let's see if there is a correlation between year of release and movie rating

years = data["Year of Release"].unique()
yearly_rating = {}

years = {}
for i in data["Year of Release"].unique():
    year_seg = data[data["Year of Release"] == i]
    rating = year_seg["Movie Rating"]
    years[i] = rating

# Now we have made a dictionary of years and their respective ratings, lets create an average rating per year

avgDict = {}
for k,v in years.items():
    avgDict[k] = sum(v)/ float(len(v))

print(avgDict)
import matplotlib.pyplot as plt
plt.hist(avgDict)
plt.show()