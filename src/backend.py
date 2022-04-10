import dearpygui.dearpygui as dpg
import pathlib
import os
from tkinter import filedialog
from tkinter import Tk

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
    # if thumbnails_window:
    #     dpg.delete_item(thumbnails_window) #usuwa panel z miniaturami
    #     thumbnails_window = add_thumbnail_panel(*user_data)
    # else:
    #     pass

    # if texture_registry:
    #     dpg.delete_item(TEXTURE_REGISTRY)
    # TEXTURE_REGISTRY = dpg.add_texture_registry(show=False)


def add_thumbnail_panel(IMAGE_PATHS):
    """config thumnails"""
    scale = 10
    img_width = 0
    img_height = 0
    """*******"""
    print("test",dpg.get_alias_id("tags_window"))
    print("test", dpg.get_alias_id("workspace_table_row"))
    print("test", bool(dpg.get_alias_id("texture_registry")))


    if dpg.get_alias_id("texture_registry"):
        dpg.delete_item("texture_registry")

    dpg.add_texture_registry(tag = "texture_registry",show=False)
    textureList = []
    print("paths", IMAGE_PATHS)
    for path in IMAGE_PATHS:
        #print("type:",type(path))
        path= str(path)
        img_width, img_height, channels, data = dpg.load_image(path)
        texture = dpg.add_static_texture(img_width, img_height, data, parent="texture_registry")
        textureList.append(texture)

    def add_thumbnails(stuffList, columns = 3):
        #dpg.add_child_window(tag="thumbnail_window", label="Table of stuff",parent="thu")

        if dpg.get_alias_id("tableOfStuff"):
            dpg.delete_item("tableOfStuff")

        dpg.add_table(tag="thumbnail_table", parent="thumbnails_window", header_row=False,borders_innerH=True,borders_innerV=True)
        for i in range(columns):
            dpg.add_table_column(parent="thumbnail_table")
        counter = 0
        while counter < len(stuffList):
            columnsLeft = columns if counter <= len(stuffList)-columns else len(stuffList) % columns
            row = dpg.add_table_row(tag="row"+str(counter),parent="thumbnail_table")
            while columnsLeft > 0:
                grupa = dpg.add_group(tag="group"+str(counter),parent=row)
                dpg.add_image(textureList[counter], parent=grupa,width=img_width/scale,height=img_height/scale)
                grupa2 = dpg.add_group(parent=grupa, horizontal=True)
                checkbox = dpg.add_checkbox(parent=grupa2)
                dpg.add_text(parent=grupa2, default_value="nazwa zdjecia. jpg")
                #dpg.add_text(default_value=stuffList[counter], parent=grupa)
                tooltip = dpg.add_tooltip(parent=grupa2)
                dpg.add_text(parent=tooltip, default_value=IMAGE_PATHS[counter])
                columnsLeft -= 1
                counter += 1
    add_thumbnails(IMAGE_PATHS)
    print("dodano miniatury")
    #print(dpg.get_item_children("thumbnail_table"))

