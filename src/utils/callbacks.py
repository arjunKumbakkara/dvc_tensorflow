import os,io
import time
import tensorflow as tf
import joblib
import logging





def create_and_save_checkpoint_callback(callbacks_dir,tensorboard_log_dir):
    unique_name= get_timestamp("tb_logs")

    tb_running_log_dir=os.path.join(callbacks_dir,unique_name)
    tensorboard_calllback = tf.keras.callbacks.TensoBoard(log_dir=tb_running_log_dir)
    
    
    tb_callback_filepath=os.path.join(callbacks_dir,"tensorboard_cb.cb")
    joblib.dump(tensorboard_calllback,tb_callback_filepath)
    logging.info(f"Tensorboard Callback is saved at {tb_callback_filepath}")






def create_and_save_tensorboard_callback(callbacks_dir,checkpoint_dir):
    pass