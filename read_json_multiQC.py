import json
import pandas as pd

# Dictionary you want to get informaiton from
inf_sel=["salmon_quant","star_fusion"]

# Opening JSON file
f = open('/Users/luciapenaperez/Downloads/multiqc_data.json')
 
# returns JSON object as a dictionary
data = json.load(f)

# I want to output data within the general report
# The sdata is a list of dictionaries
sdata=data['report_general_stats_data']

# Look through the list and select the dictionary to get data from
for v in sdata:
    if isinstance(v, dict):
        for subsel in inf_sel:
            if subsel in v:
                #print(v)
                d3=v[subsel]
                print(type(d3))
               # print(d3.keys())
                print(d3)
                d4=pd.DataFrame.from_dict(d3, orient='index',columns=[])
                print(d4)


