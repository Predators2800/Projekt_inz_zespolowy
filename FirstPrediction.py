# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 19:59:41 2022

@author: 
"""

from imageai.Classification import ImageClassification
import os
import pathlib


execution_path = "C:\\Users\\lukas\\IPZ\\Projekt_inz_zespolowy"

prediction = ImageClassification()
prediction.setModelTypeAsResNet50()
prediction.setModelPath(os.path.join(execution_path, "resnet50_imagenet_tf.2.0.h5"))
prediction.loadModel()


def recognize(file_path, file_name):
    # predictions, probabilities = prediction.classifyImage(os.path.join(execution_path, file_path),result_count=3 )
    predictions, probabilities = prediction.classifyImage(file_path, result_count=3 )
    for eachPrediction, eachProbability in zip(predictions, probabilities):
                print("File name:", file_name, "  [", eachPrediction , " : " , eachProbability, "]")
        

fileList = []
extensions=[".jpg",".jpeg",".png",".gif",".bmp"]
for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    for filename in filenames:
        path = pathlib.Path(dirpath + '\\' + filename)
        if path.suffix.lower() in extensions:
            recognize(path, filename)

