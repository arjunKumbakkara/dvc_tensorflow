from src.utils.all_utils import create_directory, read_yaml
import argparse
import pandas as pd
#import sys
import os


def get_data(config_path):
    config = read_yaml(config_path)
    remote_data_path=config["data_source"]
    #print(config)
    df = pd.read_csv(remote_data_path, sep=";")
    #print(df.head)
#Save dataset in the local directory
#create a path local one for using
    artifacts_dir= config["artifacts"]['artifacts_dir']
    raw_local_dir= config["artifacts"]['raw_local_dir']
    raw_local_file= config["artifacts"]['raw_local_file']

    raw_local_dir_path=os.path.join(artifacts_dir,raw_local_dir)
    raw_local_file_path=os.path.join(raw_local_dir_path,raw_local_file)
    print(raw_local_file_path)

    #Creating the path
    create_directory(dirs=[raw_local_dir_path])
    raw_local_file_path=os.path.join(raw_local_dir_path,raw_local_file)
    print(raw_local_file_path)

    df.to_csv(raw_local_file_path,sep=",",index=False)


if __name__ == '__main__':
    args = argparse.ArgumentParser()

    args.add_argument("--config","-c",default="config/config.yaml")
    
    parsed_args =args.parse_args()


    get_data(config_path=parsed_args.config)