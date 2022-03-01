import json
import pandas as pd


def extracting_info_json_MultiQC(path_json, main_dict_to_get_data_from, inf_sel):
    """
    Output subset of nested dictionary in json MultiQC file
    Input:
    @param path_json: path to json MultiQC file
    @param main_dict_to_get_data_from: first subset from json file, if info is in summary table "report_general_stats_data" 
    @param inf_sel: list or dictionary to use for subset 
    Example of input for function: 
    inf_sel={"salmon_quant":['num_processed','num_mapped','percent_mapped',"library_types"],
    "star_fusion":["total_reads", "uniquely_mapped", "uniquely_mapped_percent", "multimapped","multimapped_percent"]}
    """

    f = open(path_json)
    # returns JSON object as a dictionary
    data = json.load(f)
    # Closing data file
    f.close()
    # The sdata is a list of dictionaries
    sdata=data[main_dict_to_get_data_from]
    # Getting sample name to have it as column name on output
    samp_name=list(sdata[1].keys())[0].split("_")[0]
    # Empty dataframe to concat with results
    df_subs_json=pd.DataFrame({samp_name : []})
    
    # Look through the dictionary and subset information required in inf_sel
    for dict_list in sdata:
        if isinstance(inf_sel, list):
            for subsel in inf_sel:
                if subsel in dict_list:
                    df_subs_json=pd.concat([df_subs_json,pd.DataFrame.from_dict(dict_list[subsel], orient='index',columns=[samp_name])])
        elif isinstance(inf_sel, dict):
            for key in inf_sel:
                if key in dict_list:
                    keys_to_extract=inf_sel[key]
                    tempd=dict_list[key]
                    tempd = {key_ex: tempd[key_ex] for key_ex in keys_to_extract}
                    df_subs_json=pd.concat([df_subs_json,pd.DataFrame.from_dict(tempd, orient='index',columns=[samp_name])])
        else:
            print("You must input a list or dictionary with the information you want out!")
    return df_subs_json




inf_sel=["salmon_quant","star_fusion"]
path_json='/Users/luciapenaperez/Downloads/multiqc_data.json'
main_dict_to_get_data_from='report_general_stats_data'
inf_sel={"salmon_quant":['num_processed','num_mapped','percent_mapped',"library_types"], \
    "star_fusion":["total_reads", "uniquely_mapped", "uniquely_mapped_percent", "multimapped","multimapped_percent"]}

df_out=extracting_info_json_MultiQC(path_json=path_json, main_dict_to_get_data_from=main_dict_to_get_data_from, inf_sel=inf_sel)

print(df_out)

