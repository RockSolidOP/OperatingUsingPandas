import pandas as pd


emmissions = {
    "country" : ["China", "India","US"],
    "year" : ["2018","2018","2018"],
    "co2_emmissions" : [11002012.3, 121839132.23, 23989283.23]
}

pd.set_option('display.max_rows', 4)

pd.set_option()
pd.options.display.float_format = '{:,.2f}'.format
ems = pd.DataFrame(emmissions)





print(ems)