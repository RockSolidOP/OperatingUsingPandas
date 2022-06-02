import pandas as pd

iris = pd.read_csv('OperatingUsingPandas\Exercises\Files\iris.csv')


# view top 5 by defualt using head 
print("---------view top 5 by defualt using head ----------\n")

print(iris.head())

# view bottom 3 values using tails


print("---------# view bottom 3 values using tails----------\n")
print (iris.tail(3))


# show data types in the dataframe
print("---------show data types in the dataframe----------\n")
print (iris.dtypes)


# subset using loc index
print("--------subset using loc index-----------\n")

print (iris.loc[0:0])

# returns row using the column name
print("---------returns row using the column name----------\n")

print (iris.loc[0 ,'sepal_length'])


# iloc returns row using the column index
print("--------iloc returns row using the column index-----------\n")

print (iris.iloc[0 ,2])