import os,io
import time
import tensorflow as tf
import joblib
import logging
from src.utils.all_utils import get_timestamp





def create_and_save_tensorboard_callback(callbacks_dir,tensorboard_log_dir):
    unique_name= get_timestamp("tb_logs")

    tb_running_log_dir=os.path.join(callbacks_dir,unique_name)
    tensorboard_calllback = tf.keras.callbacks.TensorBoard(log_dir=tb_running_log_dir)
    
    
    tb_callback_filepath=os.path.join(callbacks_dir,"tensorboard_cb.cb")
    joblib.dump(tensorboard_calllback,tb_callback_filepath)
    logging.info(f"Tensorboard Callback is saved at {tb_callback_filepath}")






def create_and_save_checkpoint_callback(callbacks_dir,checkpoint_dir):
    checkpoint_file_path=os.path.join(checkpoint_dir,"ckpt_model.h5")
    checkpoint_callback=tf.keras.callbacks.ModelCheckpoint(
        filepath=checkpoint_file_path,
        save_best_only=True
    )

    ckpt_callback_filepath=os.path.join(callbacks_dir,"checkpoint_cb.cb")
    joblib.dump(checkpoint_callback,ckpt_callback_filepath)
    logging.info(f"Checkppoint callback is being saved at {ckpt_callback_filepath}")


def get_callbacks(callback_dir_path):
    callback_path=[os.path.join(callback_dir_path,bin_file_name) for bin_file in os.listdir(callback_dir_path) 
    if bin_file.endswith(".cb") ]

    callbacks=[
        joblib.load(path) for path in callback_path
        ]

    return callbacks