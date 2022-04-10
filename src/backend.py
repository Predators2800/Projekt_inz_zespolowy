import dearpygui.dearpygui as dpg
import pathlib
import os
import time
from tkinter import filedialog
from tkinter import Tk
from fontend_components import add_thumbnail_panel
from Image import Image

def get_file_list(folder, extensions=[".jpg",".jpeg",".png",".gif",".bmp"]):
    fileList = []
    for dirpath, dirnames, filenames in os.walk(folder):
        for filename in filenames:
            path = pathlib.Path(dirpath + '\\' + filename)
            if path.suffix.lower() in extensions:
                fileList.append(path)
    return fileList


def ask_for_directory():
    root = Tk()
    root.withdraw()
    path = filedialog.askdirectory()
    return path

def load_images(image_paths):
    images = []
    start_time = time.time()
    for path in image_paths:
        img_width, img_height, channels, img_data = dpg.load_image(path.as_posix())
        texture = dpg.add_static_texture(img_width, img_height, img_data, parent="texture_registry")
        images.append(Image(path, img_data, img_width, img_height, texture_id=texture))
    print("czas ladowanie do rejestru",time.time()-start_time)

    return images


def open_folder(sender, app_data, user_data):
    path = ask_for_directory()
    image_paths = get_file_list(path)
    images = load_images(image_paths)
    add_thumbnail_panel(images, "thumbnails_window")