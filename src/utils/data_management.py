from typing import ValuesView
import tensorflow as tf
import logging





def train_valid_generator(data_dir,IMAGE_SIZE,BATCH_SIZE,do_data_augmentation):
    datagenerator_kwargs = dict(
       rescale = 1./255 , 
       validation_split=0.20 
    )

    dataflow_kwargs = dict(
        target_size= IMAGE_SIZE,
        batch_size= BATCH_SIZE,
        #interpolation means rescaling or resizing of the images ie, 720*128 then we need it as 255*255
        interpolation= 'bilinear'

    ) 

    #**dataflow_kwargs means the dict or structure is passed into this method as an argument.
    valid_datagenerator=tf.keras.preprocessing.image.ImageDataGenerator(**datagenerator_kwargs)
    valid_generator = valid_datagenerator.flow_from_directory(
        directory = data_dir,
        subset="validation",
        shuffle=False,
        **dataflow_kwargs
        #above line is same as writing the values seperately
        #target_size= IMAGE_SIZE,
        #batch_size= BATCH_SIZE,
        #interpolation= 'bilinear'

    )

    if do_data_augmentation:
        train_datagenerator=tf.keras.preprocessing.image.ImageDataGenerator(
            rotation_range=40,
            horizontal_flip=True,
            width_shift_range=0.2,
            height_shift_range=0.2,
            shear_range=0.2,
            zoom_range=0.2,**datagenerator_kwargs
        )
        logging.info("Data Augmentation is done for training")
    else:
        train_datagenerator=valid_datagenerator
        logging.info("Data Augmentation is NOT done for training")
    train_generator= train_datagenerator.flow_from_directory(
        directory=data_dir,
        subset="training",
        shuffle=True,
        **dataflow_kwargs

    )

    logging.info("Training and Validation generators are created")
    return train_generator,valid_generator


