from src.utils.all_utils import create_directory, read_yaml
from src.utils.models import get_VGG_16_model, prepare_model 
from src.utils.callbacks import create_and_save_checkpoint_callback,create_and_save_tensorboard_callback
import argparse
import pandas as pd
#import sys
import os
import shutil
from tqdm import tqdm
import logging
import os
import io

logging_str= "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"
log_dir= "logs" #This is us mentioning that we need a logs folder inside the project.
#not working
#create_directory([log_dir])
os.makedirs(log_dir,exist_ok=True)
logging.basicConfig(filename=os.path.join(log_dir,"running_logs.log"),level=logging.INFO,format=logging_str,filemode='a')
full_final_model=None


def prepare_callbacks(config_path,params_path):
    config=read_yaml(config_path)
    params=read_yaml(params_path)
    artifacts= config["artifacts"]
    artifacts_dir= artifacts["ARTIFACTS_DIR"]
    tensorboard_log_dir= os.path.join(artifacts_dir, artifacts["TENSORBOARD_ROOT_LOG_DIR"])
    checkpoint_dir=os.path.join(artifacts_dir,artifacts["CHECKPOINT_DIR"])
    callbacks_dir=os.path.join(artifacts_dir,artifacts["CALLBACKS_DIR"])
    #Creating them
    create_directory([tensorboard_log_dir,checkpoint_dir,callbacks_dir])

    #Methods to Create the Callbacks
    create_and_save_tensorboard_callback(callbacks_dir,tensorboard_log_dir)
    create_and_save_checkpoint_callback(callbacks_dir,checkpoint_dir)


if __name__ == '__main__':
    args = argparse.ArgumentParser()

    args.add_argument("--config","-c",default="config/config.yaml")
    args.add_argument("--params","-p",default="params.yaml")
    
    parsed_args =args.parse_args()

    try:
        logging.info(" >>>  Starting: Stage 03 prepare model Callbacks")
        prepare_callbacks(config_path=parsed_args.config,params_path=parsed_args.params)
        logging.info("Ended: Stage03 Completed and Callbacks stored as binary in artifacts>>>>")
    except Exception as e:
        logging.exception(e)
        raise e
