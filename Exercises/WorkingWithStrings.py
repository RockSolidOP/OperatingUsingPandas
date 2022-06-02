import pandas as pd


names = pd.Series(['  Pomray, Cody','Wagnerl; JErry','smith, RaY ' ])

print(names)


# names2 = pd.Series([i[::-1] for i in names])
# names = names.str.replace(';',',')

# names = names.str.strip()

names = names.str.split(',')

# names = names.str.lower()

# names = names.str.
print(names)
