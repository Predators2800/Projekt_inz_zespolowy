import dearpygui.dearpygui as dpg
import pathlib
import os
from tkinter import filedialog


def get_file_list(folder, extensions=[".jpg",".jpeg",".png",".gif",".bmp"]):
    fileList = []
    for dirpath, dirnames, filenames in os.walk(folder):
        for filename in filenames:
            path = pathlib.Path(dirpath + '\\' + filename)
            if path.suffix.lower() in extensions:
                fileList.append(path)
    return fileList


def display_file_list(fileList, file_list_window):
    for path in fileList:
        dpg.add_text(parent=file_list_window, default_value=path)


def open_folder():
    CURRENT_FOLDER = filedialog.askdirectory()
    display_file_list(get_file_list(CURRENT_FOLDER))
