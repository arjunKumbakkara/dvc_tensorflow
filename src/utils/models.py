import tensorflow as tf 
import os 
import logging
from tensorflow.python.keras.backend import flatten





def get_VGG_16_model(input_shape, model_path):
    model=tf.keras.applications.vgg16.VGG16(
        input_shape=input_shape,
        weights="imagenet",
        include_top=False
    )
    #Saving the model
    model.save(model_path)
    logging.info(f"VGG16 base model saved at {model_path}")
    return model



def prepare_model(model,CLASSES,freeze_all,freeze_till,learning_rate):
    if freeze_all:
        for layer in model.layers:
            layer.trainable= False 
    elif ((freeze_till is not None) and (freeze_till> 1 )):
        for layer in model.layers[:-freeze_till]:# Freeze_till is a number
            #Freeze-till is '-' or minus because, from the right the list we need reduce.Which means , -1 is last
            #layer and -2 will leave the extreme last and  NOT train till penultiamte. Making the last layer trainable
            layer.trainable= False

#Adding our own fully connected Layers.The real learning layeers.
    flatten_in= tf.keras.layers.Flatten()(model.output)
    prediction= tf.keras.layers.Dense(
        units=CLASSES,
        activation= "softmax"
    )(flatten_in)
#What you see above is a functional approach
#This is similar to model.add(flatten_layer) very much but thats more like an
#API or sequential approach.

    full_model = tf.keras.models.Model(
        inputs= model.input,
        outputs= prediction

    )

    #logging.info("Custom model summary")
    full_model.compile(
        optimizer = tf.keras.optimizers.SGD(learning_rate),
        loss= tf.keras.losses.CategoricalCrossentropy,
        metrics=["accuracy"]
    )

    logging.info("Custom model is compiled and is ready to be trained!")

    return model




def load_full_model(untrained_full_model_path):
    model= tf.keras.models.load_model(untrained_full_model_path)
    logging.info(f"untrained model is read from {untrained_full_model_path}")
    return model


