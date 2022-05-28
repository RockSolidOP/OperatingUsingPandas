import pandas as pd

planets = pd.read_csv('Exercises\Files\planets.csv')

print(planets.head())

# print(planets['mass'].mean())


# print(planets['distance'].astype(int).head())
planets['year_dt'] = pd.to_datetime(planets['year'], format='%Y')

print(
  planets['year_dt'] 
)