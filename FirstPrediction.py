# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 19:59:41 2022

@author: 
"""

from imageai.Classification import ImageClassification
import os
import pathlib
import time


execution_path = "C:\\Users\\szymon.winiarski\\PycharmProjects\\Projekt_inz_zespolowy\\PLIKI\\"

prediction = ImageClassification()
prediction.setModelTypeAsResNet50()
prediction.setModelPath(os.path.join(execution_path, "resnet50_imagenet_tf.2.0.h5"))
prediction.loadModel()


def recognize(file_path, file_name):
    # predictions, probabilities = prediction.classifyImage(os.path.join(execution_path, file_path),result_count=3 )
    predictions, probabilities = prediction.classifyImage(file_path, result_count=1 )
    # for eachPrediction, eachProbability in zip(predictions, probabilities):
    #             print("File name:", file_name, "  [", eachPrediction , " : " , eachProbability, "]")
        

fileList = []
extensions=[".jpg",".jpeg",".png",".gif",".bmp"]

start_time = time.time()
for dirpath, dirnames, filenames in os.walk("C:\\Users\\szymon.winiarski\\Downloads\\images\\images~\\500 images"):
    for filename in filenames:
        path = pathlib.Path(dirpath + '\\' + filename)
        if path.suffix.lower() in extensions:
            recognize(path, filename)
print("czas wykonania",time.time()-start_time)