import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sas
# Fundamentals of Data Analytics Lab 02
# Arch Patel - N01598909


# Loading DataSet for URL
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
titanic = pd.read_csv(url)

# Checking DataFrame
print(titanic)

# Dropping the Columns : Name,Ticket And Cabin
titanic.drop('Name', axis=1, inplace=True)
titanic.drop('Ticket', axis=1, inplace=True)
titanic.drop('Cabin', axis=1, inplace=True)

# Checking Column Are Drop or Not
print(titanic)

print("-------------------------------------------------------------------------")

# Index 5 is Null Value
print(titanic['Age'][5])

# Filling Null value in Age's with Median of Age
titanic['Age'] = titanic['Age'].fillna(titanic['Age'].median())

# Checking if Null at index 5 is fill or not
print(titanic['Age'][5])

print("-------------------------------------------------------------------------")

# Index 61 is Null Value in Embarked
print(titanic['Embarked'][61])

# Filling Null value in Embarked with mode
titanic['Embarked'] = titanic['Embarked'].fillna(titanic['Embarked'].mode()[0])

# Checking if Null at index 61 is fill or not
print(titanic['Embarked'][61])

print("-------------------------------------------------------------------------")

# Plotting Histogram with value of Age Column
plt.hist(titanic['Age'], bins=30, alpha=0.4, color='blue')

# Label of X-Axis
plt.xlabel("Passenger Age")

# Label of Y-Axis
plt.ylabel("Number of Passenger")

# Title for Histogram
plt.title("Distribution of Passenger's Age")

# Save in the Graph
plt.savefig("Histogram")

# -------------------------------------------------------------------------

# Clear Plot
plt.clf()

plt.scatter(titanic['Age'], titanic['Fare'])

# Label of X-Axis
plt.xlabel("Passenger Age")

# Label of Y-Axis
plt.ylabel("Passenger Fare")

# Title for Scatter Plot
plt.title("Distribution of Fare Based on Passenger's Age")

# Save in the Graph
plt.savefig("ScatterPlot")

# -------------------------------------------------------------------------

# Clear Plot
plt.clf()

# Creating Sub Plot for Different Color Bar Graph
fig, ax = plt.subplots()

# Plotting Bar Graph
ax.bar(titanic['Pclass'].value_counts(sort=True).keys().values, titanic['Pclass'].value_counts(sort=True).values, color=['red', 'blue', 'green'])

# Label of X-Axis
plt.xlabel("Passenger Class")

# Label of Y-Axis
plt.ylabel("Number of Passenger")

# Title for Bar Graph
plt.title("Distribution of Passengers in Each Passenger Class")

# Save in the Graph
plt.savefig("BarGraph")

# -------------------------------------------------------------------------

# Clear Plot
plt.clf()

# Plotting Bar plot using seaborn package
sas.boxplot(x="Pclass", y="Age", data=titanic)

# Label of X-Axis
plt.xlabel("Passenger Class")

# Label of Y-Axis
plt.ylabel("Age of Passenger")

# Title for BoxPlot(Seaborn)
plt.title("Distribution of Age of Passengers in Each Passenger Class")

# Save in the Graph
plt.savefig("BoxPlot(Seaborn)")


# -------------------------------------------------------------------------

# Clear Plot
plt.clf()

# Sort DataFrame on Fare Column
titanic = titanic.sort_values("Fare").reset_index()

# Plotting Line Chart Values
plt.plot(titanic["Fare"], titanic["PassengerId"])

# Labeling X Axis
plt.xlabel("Fare")

# Labeling Y Axis
plt.ylabel("PassengerId")

# Title for Line Chart
plt.title("Fare Against PassengerId")

# Save in the Graph
plt.savefig("LineChart")


