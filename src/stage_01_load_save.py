from src.utils.all_utils import create_directory, read_yaml
import argparse
import pandas as pd
#import sys
import os
import shutil
from tqdm import tqdm


#Data Copy Util

def copy_file(source_download_dir,local_data_dir):
    list_of_files=os.listdir(source_download_dir)
    N= len(list_of_files)
    for file in tqdm(list_of_files,total=N,desc="Copying files",colour="green"):
        src=os.path.join(source_download_dir,file )
        dest=os.path.join(local_data_dir,file)
        shutil.copy(src,dest) 




def get_data(config_path):
    config = read_yaml(config_path)
    remote_data_path=config["data_source"]
    source_download_dirs = config["source_download_dirs"]
    local_data_dirs = config["local_data_dirs"]

    for source_download_dir,local_data_dir in tqdm(zip(source_download_dirs,local_data_dirs),total=2,desc= "Iterating over list of folders",color="red"):
        create_directory([local_data_dir])
        copy_file(source_download_dir,local_data_dir)





if __name__ == '__main__':
    args = argparse.ArgumentParser()

    args.add_argument("--config","-c",default="config/config.yaml")
    
    parsed_args =args.parse_args()


    get_data(config_path=parsed_args.config)