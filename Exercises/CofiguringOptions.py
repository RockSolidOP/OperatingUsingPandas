import pandas as pd


emmissions = {
    "country" : ["China", "India","US"],
    "year" : ["2018","2018","2018"],
    "co2_emmissions" : [11002012.3, 121839132.23, 23989283.2332]
}

pd.set_option('display.max_rows', 4)

pd.options.display.float_format = '{:.4f}'.format
ems = pd.DataFrame(emmissions)





print(ems)