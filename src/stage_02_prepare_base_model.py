from src.utils.all_utils import create_directory, read_yaml
from src.utils.models import get_VGG_16_model
import argparse
import pandas as pd
#import sys
import o
import shutil
from tqdm import tqdm
import logging

logging_str= "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"
log_dir= "logs" #This is us mentioning that we need a logs folder inside the project.
#not working
#create_directory([log_dir])
os.makedirs(log_dir,exist_ok=True)
logging.basicConfig(filename=os.path.join(log_dir,"running_logs.log"),level=logging.INFO,format=logging_str,filemode='a')
 


def get_VGG_16_model(input_shape: list, base_model_path):


def prepare_base_model(config_path,params_path):
    config = read_yaml(config_path)
    params= read_yaml(params_path)

    artifacts = config["artifacts"]
    params= read_yaml(params_path)
    artifacts_dir= artifacts["ARTIFACTS_DIR"]
    base_model_dir = artifacts["BASE_MODEL_DIR"]
    base_model_name=artifacts["BASE_MODEL_NAME"]
    #Path to be created
    base_model_dir_path=os.path.join(artifacts_dir,base_model_dir)

    create_directory([base_model_dir_path])

    base_model_path=os.path.join(base_model_dir_path,base_model_name)
    model=get_VGG_16_model(input_shape=params["IMAGE_SIZE"],model_path= base_model_path)





if __name__ == '__main__':
    args = argparse.ArgumentParser()

    args.add_argument("--config","-c",default="config/config.yaml")
    args.add_argument("--params","-p",default="params.yaml")
    
    parsed_args =args.parse_args()

    try:
        logging.info(" >>>  Starting: Stage 02 prepareStarted")
        prepare_base_model(config_path=parsed_args.config,params_path=parsed_args.params)
        logging.info("Ended: Stage02 Completed and base model created.>>>>")
    except Exception as e:
        logging.exception(e)
        raise e