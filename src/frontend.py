import dearpygui.dearpygui as dpg
import os
import pathlib
from tkinter import filedialog

"""GLOBALS"""

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 800
TOOLBAR_HEIGHT = 60
STATUS_PANEL_HEIGHT = 30

FONT_SIZE = 14
BUTTON_HEIGHT = 40

CURRENT_FOLDER = ""

"""CREATE APP WINDOW"""

dpg.create_context()
dpg.create_viewport(title="nasza aplikacja", width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
main_window = dpg.add_window(label="okno")
dpg.set_primary_window(main_window, True)

with dpg.font_registry():
    default_font = dpg.add_font("./resources/font/fira.ttf", FONT_SIZE)  # ładowanie czcionki z dysku
dpg.bind_font(default_font)  # ustawia czcionkę jako default
dpg.add_font_range(0x0100, 0x017D, parent=default_font)  # dodaje zakres polskich znaków

"""MAIN_WINDOW"""

tabela = dpg.add_table(
    parent=main_window, borders_innerH=True, borders_innerV=True, header_row=False
)
dpg.add_table_column(parent=tabela)


"""UPPER_PANEL"""

toolbar = dpg.add_table_row(parent=tabela, height=TOOLBAR_HEIGHT)
toolbar_table = dpg.add_table(parent=toolbar, header_row=False)
dpg.add_table_column(parent=toolbar_table, init_width_or_weight=3)
dpg.add_table_column(parent=toolbar_table, init_width_or_weight=2)
toolbar_table_row = dpg.add_table_row(parent=toolbar_table)

group_u1 = dpg.add_group(horizontal=True, parent=toolbar_table_row)
group_u2 = dpg.add_group(horizontal=True, parent=toolbar_table_row)

def get_file_list(folder):
    fileList = []
    for dirpath, dirnames, filenames in os.walk(folder):
        for filename in filenames:
            path = pathlib.Path(dirpath + '\\' + filename)
            print(path.suffix.lower())
            if path.suffix.lower() in [".jpg",".png",".gif",".bmp"]:
                fileList.append(path)
    print(fileList)
    return fileList

def display_file_list(fileList):
    for path in fileList:
        dpg.add_text(parent=file_list_window, default_value=path)

def open_folder():
    CURRENT_FOLDER = filedialog.askdirectory()
    display_file_list(get_file_list(CURRENT_FOLDER))

dpg.add_button(label="Otwórz folder", parent=group_u1, height=BUTTON_HEIGHT, callback=open_folder)
dpg.add_button(label="Pokaż w Eksloratorze", parent=group_u2, height=BUTTON_HEIGHT)
dpg.add_button(label="Otwórz", parent=group_u2, height=BUTTON_HEIGHT)
dpg.add_button(label="Kopiuj", parent=group_u2, height=BUTTON_HEIGHT)
dpg.add_button(label="Kasuj", parent=group_u2, height=BUTTON_HEIGHT)


"""MIDDLE_PANEL"""

workspace = dpg.add_table_row(parent=tabela)
workspace_table = dpg.add_table(no_host_extendY=True, resizable=True,
    parent=workspace, borders_innerH=False, borders_innerV=True, header_row=True
)
dpg.add_table_column(parent=workspace_table, label="Pliki",init_width_or_weight=1)
dpg.add_table_column(parent=workspace_table, label="Miniatury", init_width_or_weight=5)
dpg.add_table_column(parent=workspace_table, label="Tagi", init_width_or_weight=1)
workspace_table_row = dpg.add_table_row(parent=workspace_table)

"""MIDDLE_PANEL_FILE_LIST"""

file_list_window = dpg.add_child_window(parent=workspace_table_row)

"""MIDDLE_PANEL_THUMBNAILS"""

thumbnails_window = dpg.add_child_window(parent=workspace_table_row)

tags = [
    "niebo",
    "trawa",
    "plaza",
    "śnieg",
    "ludzie",
    "zwierzęta",
    "samochody",
    "czerwony",
    "czarny",
    "red",
    "green",
    "blue",
    "red",
    "green",
    "blue",
    "red",
    "green",
    "blue",
]
tags_window = dpg.add_child_window(label="Tagi", parent=workspace_table_row)

for tag in tags:
    dpg.add_checkbox(label=tag, parent=tags_window)


"""LOWER_PANEL"""

status_panel = dpg.add_table_row(parent=tabela)
status_panel_table = dpg.add_table(
    parent=status_panel, borders_outerH=True, borders_outerV=True, header_row=False
)
dpg.add_table_column(parent=status_panel_table)
status_panel_table_row = dpg.add_table_row(parent=status_panel_table, height=STATUS_PANEL_HEIGHT)
dpg.add_slider_int(label="progressbar", default_value=30, parent=status_panel_table_row)

def on_resize():
    WINDOW_WIDTH = dpg.get_viewport_client_width()
    WINDOW_HEIGHT = dpg.get_viewport_client_height()
    dpg.set_item_height(workspace_table, WINDOW_HEIGHT-TOOLBAR_HEIGHT-STATUS_PANEL_HEIGHT-20)
    print(WINDOW_HEIGHT, WINDOW_WIDTH)

dpg.set_viewport_resize_callback(on_resize)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()