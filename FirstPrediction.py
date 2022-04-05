# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 19:59:41 2022

@author: 
"""

from imageai.Classification import ImageClassification
import os


execution_path = os.getcwd()

prediction = ImageClassification()



prediction.setModelTypeAsResNet50() #( resnet50_imagenet_tf.2.0.h5 )
#prediction.setModelTypeAsMobileNetV2() # mobilenet_v2.h5
#prediction.setModelTypeAsInceptionV3() # inception_v3_weights_tf_dim_ordering_tf_kernels.h5


#prediction.setModelPath(os.path.join(execution_path, "mobilenet_v2.h5"))
prediction.setModelPath(os.path.join(execution_path, "resnet50_imagenet_tf.2.0.h5"))
#prediction.setModelPath(os.path.join(execution_path, "inception_v3_weights_tf_dim_ordering_tf_kernels.h5"))
prediction.loadModel()


def recognize(name):

   predictions, probabilities = prediction.classifyImage(os.path.join(execution_path, name),result_count=3 )
   for eachPrediction, eachProbability in zip(predictions, probabilities):
              print(eachPrediction , " : " , eachProbability)
        
        

while(1):

    nam = input('Enter your name:')    

    print(recognize(nam)) 
        
        
