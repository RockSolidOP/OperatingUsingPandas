import pandas as pd


scores = {
    "name" : ["Aadi" , "Nivi" , "Soham" ],
    "city": [ "Thane", "Pune", "Banglore"],
    "score" : [89,78,90]
}

df = pd.DataFrame(scores)

# df["name_city"] = df["name"] + '_' + df["city"]
# print(df["name_city"])
print (df[df["score"]>81])

# print(df)