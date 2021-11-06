import yaml 
import os 
import pandas
import json
import logging
import time





def get_timestamp(name):
    #Timestamp creation is best this way
    timestamp= time.asctime().replace(" ","_").replace(":","_")
    #Formatting the unique name
    unique_name= f"{name}_at_{timestamp}"
    return unique_name



def read_yaml(path_to_yaml: str) -> dict:
    with open(path_to_yaml) as yaml_file:
        content = yaml.safe_load(yaml_file)
    logging.info(f"yaml file read: {path_to_yaml}  loaded successfully.")

    return content

def create_directory(dirs: list):
    for dir_path in dirs:
        os.makedirs(dir_path,exist_ok=True)
        logging.info(f"directory saved at {dir_path}")


def save_local_df(data,data_path,index_status=False):
    data.to_csv(data_path,index=index_status)
    logging.info(f"data is saved At {data_path}")



def save_reports(report: dict,reports_path: str):
    with open(reports_path,"w") as s:
        json.dump(report,s,indent=4)#indent is pretty printing
    logging.info(f"Your report {report} is saved at {reports_path}")