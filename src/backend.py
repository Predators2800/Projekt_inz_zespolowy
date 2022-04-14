import dearpygui.dearpygui as dpg
import pathlib
import os
import time
from Image import Image
from PIL import Image as pil_image
import numpy as np
from imageai.Classification import ImageClassification

def image_to_dpg_image(image):
    """
    Converst PIL image format to dpg image format
    """
    image.putalpha(255)
    dpg_image = np.frombuffer(image.tobytes(), dtype=np.uint8) / 255.0
    return dpg_image

def image_load(file_path):
    """
    Loads image in PIL format from file path
    Can be used by Predictor class to recognize image.
    """
    image = pil_image.open(file_path)
    return image

class Predictor():
    """
    Predictor class used for recognizing images.
    """
    def __init__(self):
        self._prediction = ImageClassification()
        self._prediction.setModelTypeAsResNet50()
        self._prediction.setModelPath("resnet50_imagenet_tf.2.0.h5")
        self._prediction.loadModel()

    def recognize(self, file_path):
        predictions, probabilities = self._prediction.classifyImage(file_path, input_type='array' )
        return predictions, probabilities


def get_file_list(folder, extensions=[".jpg",".jpeg",".png",".gif",".bmp"]):
    """
    Returns list of files in folder with given extensions.
    """
    fileList = []
    for dirpath, dirnames, filenames in os.walk(folder):
        for filename in filenames:
            path = pathlib.Path(dirpath + '\\' + filename)
            if path.suffix.lower() in extensions:
                fileList.append(path)
    return fileList


def load_images(image_paths):
    images = []
    start_time = time.time()
    for path in image_paths:
        img_width, img_height, channels, img_data = dpg.load_image(path.as_posix())
        texture = dpg.add_static_texture(img_width, img_height, img_data, parent="texture_registry")
        images.append(Image(path, img_data, img_width, img_height, texture_id=texture))
    print("czas ladowania do rejestru",time.time()-start_time)

    return images
