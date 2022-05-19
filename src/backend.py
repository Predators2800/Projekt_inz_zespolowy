import dearpygui.dearpygui as dpg
import pathlib
import os
import time
from Image import Image
from PIL import Image as pil_image
import numpy as np
from imageai.Classification import ImageClassification
from frontend_components import refresh_image_category


def image_to_dpg_image(image):
    """
    Converts PIL image format to dpg image format
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


class Predictor:
    """
    Predictor class used for recognizing images.
    """
    def __init__(self):
        self.actual_path = str(pathlib.Path('.').resolve().parent)
        model_path = os.path.join(self.actual_path, "resnet50_imagenet_tf.2.0.h5")
        self._prediction = ImageClassification()
        self._prediction.setModelTypeAsResNet50()
        self._prediction.setModelPath(model_path)
        self._prediction.loadModel()

    def recognize(self, image_data):
        predictions, probabilities = self._prediction.classifyImage(image_data, input_type='array')
        return predictions, probabilities


    def recognise_path(self,file_path):
        predictions, probabilities = self._prediction.classifyImage(file_path, result_count=1)
        return predictions, probabilities

def get_file_list(folder, extensions=[".jpg", ".jpeg", ".png", ".gif", ".bmp"]):
    """
    Returns list of files in folder with given extensions.
    """
    file_list = []
    for dirpath, dirnames, filenames in os.walk(folder):
        for filename in filenames:
            path = pathlib.Path(dirpath + '\\' + filename)
            if path.suffix.lower() in extensions:
                file_list.append(path)
    return file_list


def load_images(image_paths):
    counter = 1
    ratio = 4
    h=100
    if not dpg.get_value("progress_bar"):
        dpg.set_value("progress_bar", 0)
    start_time = time.time()
    for path in image_paths:
        pil_image = image_load(path)
        width = pil_image.size[0]
        height = pil_image.size[1]
        image_data = image_to_dpg_image(pil_image)
        texture = dpg.add_static_texture(width, height, image_data, parent="texture_registry")
        Image.IMAGES.append(Image(path, pil_image, h*(width/ratio), h, texture_id=texture))
        dpg.set_value("progress_bar", counter / len(image_paths))
        dpg.configure_item("progress_bar", overlay="Loading: " + str(round(counter * 100 / len(image_paths), 1)) + "%")
        counter += 1
    print("czas ladowania do rejestru", time.time()-start_time)


def delete_file(image: Image):
    os.remove(image.path)
    image.remove()


def delete_selected_files():
    for i in Image.SELECTED_IMAGES:
        delete_file(i)
    Image.SELECTED_IMAGES.clear()


def analyze_images():
    predictor = Predictor()
    counter = 0
    Image.CATEGORIES_TO_SHOW.clear()

    for image in Image.IMAGES:
        counter +=1
        dpg.set_value("progress_bar", (counter + 1) / len(Image.IMAGES))
        dpg.configure_item("progress_bar",
                           overlay="Analyzing: " + str(round((counter + 1) * 100 / len(Image.IMAGES), 1)) + "%")
        predictions, probabilities = predictor.recognise_path(image.path)
        image.set_category(predictions.copy()) #nadanie tagu
    dpg.configure_item("progress_bar", overlay="Analysing finished")
    counter = 0
    for image in Image.IMAGES:
        counter+=1
        print(counter,"category = ",image.category,"tags=",image.tags)
    refresh_image_category()
