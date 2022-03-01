import json
import pandas as pd

# Output subset of nested dictionary in json MultiQC file
# Input:
# path_json: path to json MultiQC file
# main_dict_to_get_data_from: first subset from json file, if info is in summary table "report_general_stats_data" 
# inf_sel: list or dictionary to use for subset 
# Example of input for function in dictionary and list form 
# inf_sel={"salmon_quant":['num_processed','num_mapped','percent_mapped',"library_types"], \
#     "star_fusion":["total_reads", "uniquely_mapped", "uniquely_mapped_percent", "multimapped","multimapped_percent"]}
inf_sel=["salmon_quant","star_fusion"]
path_json='/Users/luciapenaperez/Downloads/multiqc_data.json'
main_dict_to_get_data_from='report_general_stats_data'

f = open(path_json)
 # returns JSON object as a dictionary
data = json.load(f)

# Closing data file
f.close()

# I want to output data within the general report
# The sdata is a list of dictionaries
sdata=data[main_dict_to_get_data_from]

# Gettign sample name to have it as column name on output
samp_name=list(sdata[1].keys())[0].split("_")[0]

# Empty dataframe to concat with results
outp=pd.DataFrame({samp_name : []})

# Look through the dictionary and subset information required in inf_sel
for v in sdata:
    if isinstance(inf_sel, list):
        for subsel in inf_sel:
            if subsel in v:
                outp=pd.concat([outp,pd.DataFrame.from_dict(v[subsel], orient='index',columns=[samp_name])])
    elif isinstance(inf_sel, dict):
        for key in inf_sel:
            if key in v:
                keys_to_extract=inf_sel[key]
                tempd=v[key]
                tempd = {key_ex: tempd[key_ex] for key_ex in keys_to_extract}
                outp=pd.concat([outp,pd.DataFrame.from_dict(tempd, orient='index',columns=[samp_name])])
    else:
        print("You must input a list or dictionary with the information you want out!")

print(outp)



