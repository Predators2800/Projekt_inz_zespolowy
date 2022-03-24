# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 19:59:41 2022

@author: 
"""



# from imageai.Detection import ObjectDetection
# import os
# execution_path = os.getcwd()
# detector = ObjectDetection()
# detector.setModelTypeAsYOLOv3()
# detector.setModelPath( os.path.join(execution_path , "yolo.h5"))
# detector.loadModel()
# detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , "asd123.jpg"), output_image_path=os.path.join(execution_path , "imagenew.jpeg"),minimum_percentage_probability=30)

# for eachObject in detections:
#    print(eachObject["name"] , " : ", eachObject["percentage_probability"], " : ",eachObject["box_points"] )
#    print("--------------------------------")




""" from imageai.Classification.Custom import CustomImageClassification
import os

execution_path = os.getcwd()

predictor = CustomImageClassification()
predictor.setModelPath(model_path=os.path.join(execution_path, "idenprof_resnet.h5"))
predictor.setJsonPath(model_json=os.path.join(execution_path, "idenprof.json"))
predictor.setModelTypeAsResNet50()
predictor.loadModel(num_objects=10)

predictor2 = CustomImageClassification()
predictor2.setModelPath(model_path=os.path.join(execution_path, "idenprof_inception_0.719500.h5"))
predictor2.setJsonPath(model_json=os.path.join(execution_path, "idenprof.json"))
predictor2.setModelTypeAsInceptionV3()
predictor2.loadModel(num_objects=10)

results, probabilities = predictor.classifyImage(image_input=os.path.join(execution_path, "zd1.png"), result_count=5)
print(results)
print(probabilities)


#results2, probabilities2 = predictor3.classifyImage(image_input=os.path.join(execution_path, "zd1.png"),
#                                                       result_count=5)
#print(results2)
#print(probabilities2)
print("-------------------------------") """







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
        
        
        
nam = input('Enter your name:')    

print(recognize(nam)) 
        
        
""" from imageai.Prediction import ImageClassification
import os
import threading

execution_path = os.getcwd()

prediction = ImageClassification()
prediction.setModelTypeAsResNet()
prediction.setModelPath( os.path.join(execution_path, "resnet50_imagenet_tf.2.0.h5"))

picturesfolder = os.environ["USERPROFILE"] + "\\Pictures\\"
allfiles = os.listdir(picturesfolder)

class PredictionThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        prediction.loadModel()
        for eachPicture in allfiles:
            if eachPicture.endswith(".png") or eachPicture.endswith(".jpg"):
                predictions, percentage_probabilities = prediction.predictImage(picturesfolder + eachPicture, result_count=1)
                for prediction, percentage_probability in zip(predictions, probabilities):
                    print(prediction , " : " , percentage_probability)

predictionThread = PredictionThread ()
predictionThread.start()    """