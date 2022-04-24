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
        self._prediction = ImageClassification()
        self._prediction.setModelTypeAsResNet50()
        self._prediction.setModelPath("resnet50_imagenet_tf.2.0.h5")
        self._prediction.loadModel()

    def recognize(self, image_data):
        predictions, probabilities = self._prediction.classifyImage(image_data, input_type='array')
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
    if not dpg.get_value("progress_bar"):
        dpg.set_value("progress_bar", 0)
    start_time = time.time()
    for path in image_paths:
        img_width, img_height, channels, img_data = dpg.load_image(path.as_posix())
        texture = dpg.add_static_texture(img_width, img_height, img_data, parent="texture_registry")
        Image.IMAGES.append(Image(path, img_data, img_width, img_height, texture_id=texture))
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
