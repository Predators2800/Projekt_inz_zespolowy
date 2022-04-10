import dearpygui.dearpygui as dpg
import pathlib
import os
from tkinter import filedialog
from tkinter import Tk
from fontend_components import add_thumbnail_panel


#global THUMBNAIL_PANEL, IMAGE_PATHS
#IMAGE_PATHS = []

def get_file_list(folder, extensions=[".jpg",".jpeg",".png",".gif",".bmp"]):
    fileList = []
    for dirpath, dirnames, filenames in os.walk(folder):
        for filename in filenames:
            path = pathlib.Path(dirpath + '\\' + filename)
            if path.suffix.lower() in extensions:
                fileList.append(path)
    return fileList


# def display_file_list(fileList, file_list_window):
#     for path in fileList:
#         dpg.add_text(parent=file_list_window, default_value=path)


def open_folder(sender, app_data, user_data):
    print("w guziku",sender, app_data, user_data)
    #otwórz okno > przekarz ścieżkę do
    root = Tk()
    root.withdraw()
    CURRENT_FOLDER = filedialog.askdirectory()
    IMAGE_PATHS = get_file_list(CURRENT_FOLDER)

    add_thumbnail_panel(IMAGE_PATHS)