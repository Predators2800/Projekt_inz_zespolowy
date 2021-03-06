import dearpygui.dearpygui as dpg
from backend import get_file_list, load_images, delete_selected_files, analyze_images
from frontend_components import popup, add_image_category_list, add_thumbnail_panel
from tkinter import filedialog
from tkinter import Tk
from Image import Image
import subprocess
import shutil
from subprocess import check_call
import sys

WINDOW_HEIGHT = 720
WINDOW_WIDTH = 1280
TOOLBAR_HEIGHT = 60
STATUS_PANEL_HEIGHT = 30
FONT_SIZE = 18
BUTTON_HEIGHT = 40
IS_TEXTURE_REGISTRY_VISIBLE = False


def app_init() -> None:
    """
    Main window:
    - Initialize main application window,
    - Set display properties,
    - Return main window object
    """

    dpg.create_context(tag="context")
    set_default_font()
    dpg.create_viewport(title="nasza aplikacja", width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
    dpg.add_texture_registry(tag = "texture_registry",show=IS_TEXTURE_REGISTRY_VISIBLE)


def interface_init():    
    """
    Initialize interface:
    """
    with dpg.window(tag="main_window", label="okno"):
        dpg.set_primary_window("main_window", True)
        with dpg.table(tag="main_table", borders_innerH=True, borders_innerV=True, header_row=False):
            dpg.add_table_column(tag="main_column")
            with dpg.table_row(tag="toolbar", height=TOOLBAR_HEIGHT):
                with dpg.table(tag="toolbar_table", header_row=False):
                    dpg.add_table_column(tag="toolbar_1_col", init_width_or_weight=3)
                    dpg.add_table_column(tag="toolbar_2_col", init_width_or_weight=2)
                    with dpg.table_row(tag="toolbar_table_row"):
                        with dpg.group(tag="group_toolbar_1", horizontal=True):
                            dpg.add_button(label="Otwórz folder", height=BUTTON_HEIGHT, callback=open_folder_callback)
                            dpg.add_button(label="Analizuj", height=BUTTON_HEIGHT, callback=analyze_callback)
                        with dpg.group(tag="group_toolbar_2", horizontal=True):
                            dpg.add_button(label="Pokaż w Eksloratorze", height=BUTTON_HEIGHT, callback=show_in_explorer_callback)
                            dpg.add_button(label="Otwórz", height=BUTTON_HEIGHT,callback=open_in_default_callback)
                            dpg.add_button(label="Zaznacz wszystko", height=BUTTON_HEIGHT,callback=select_all_callback)
                            dpg.add_button(label="Kopiuj", height=BUTTON_HEIGHT, callback=copy_callback)
                            dpg.add_button(label="Kasuj", height=BUTTON_HEIGHT, callback=delete_selected_callback)
                            dpg.add_checkbox(tag="przyklad",label="test")
            with dpg.table_row(tag="workspace"):
                with dpg.table(tag="workspace_table", no_host_extendY=True, resizable=True, borders_innerH=False, borders_innerV=True, header_row=True):
                    dpg.add_table_column(label="Miniatury", init_width_or_weight=5)
                    dpg.add_table_column(label="Kategorie", init_width_or_weight=1)
                    with dpg.table_row(tag="workspace_table_row"):
                        dpg.add_child_window(tag="thumbnails_window",)
                        dpg.add_child_window(tag="tags_window", label="Okno-kategorii")
                        add_image_category_list("tags_window")


            with dpg.table_row(tag="status_panel"):
                with dpg.table(tag="status_panel_table", borders_outerH=True, borders_outerV=True, header_row=False):
                    dpg.add_table_column(tag="kolumna")
                    with dpg.table_row(tag="status_panel_table_row", height=STATUS_PANEL_HEIGHT):
                        dpg.add_progress_bar(label="progressbar", overlay="progress", tag="progress_bar")


def app_run() -> None:
    """
    Main window:
    - Set dearpygui and runs main program loop
    """

    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()


def app_cleanup():
    dpg.destroy_context()


def set_default_font() -> None:
    """
    Application:
    - Load font from resources folder
    - Set loaded font as default
    - Add Polish characters
    """

    with dpg.font_registry():
        default_font = dpg.add_font("../resources/font/fira.ttf", FONT_SIZE)  # ładowanie czcionki z dysku
    dpg.bind_font(default_font)  # ustawia czcionkę jako default
    dpg.add_font_range(0x0100, 0x017D, parent=default_font)  # dodaje zakres polskich znaków


def workspace_viewport_resize_callback():
    """
    Initiaize viewport resize callback:
    - gets called each time window is being resized by the user
    -
    """
    WINDOW_HEIGHT = dpg.get_viewport_client_height()
    dpg.set_item_height("workspace_table", WINDOW_HEIGHT-TOOLBAR_HEIGHT-STATUS_PANEL_HEIGHT-20)


def set_global_callbacks():
    dpg.set_viewport_resize_callback(workspace_viewport_resize_callback)


def ask_for_directory():
    root = Tk()
    root.withdraw()
    path = filedialog.askdirectory()
    return path


def clear_texture_registry():
    dpg.delete_item("texture_registry")
    dpg.add_texture_registry(tag="texture_registry", show=IS_TEXTURE_REGISTRY_VISIBLE)


def show_in_explorer_callback():
    for image in Image.SELECTED_IMAGES:
        subprocess.Popen(r'explorer /select,"' + str(image.path) + '"')


def show_in_explorer_callback2():
    path = ""
    select_path = "/select,"
    for image in Image.SELECTED_IMAGES:
        select_path + str(image.path)
    subprocess.Popen(r'explorer' + select_path + '"')


def copy_to_clipboard():
    for image in Image.SELECTED_IMAGES:
        subprocess.check_call(str(image.path))

def clear_images():
    if Image.IMAGES:
        Image.IMAGES.clear()
        Image.IMAGES_TO_SHOW.clear()
        Image.SELECTED_IMAGES.clear()
        Image.SELECTED_CATEGORIES.clear()
        Image.CATEGORIES_TO_SHOW.clear()
def open_folder_callback(sender, app_data, user_data):
    path = ask_for_directory()
    image_paths = get_file_list(path)
    clear_texture_registry()
    clear_images()
    load_images(image_paths)
    add_thumbnail_panel(parent="thumbnails_window")

    
def open_in_default_callback(): 
    for image in Image.SELECTED_IMAGES:
        paintPath= {'linux':'xdg-open',
                                  'win32':'explorer',
                                  'darwin':'open'}[sys.platform]
        subprocess.Popen('%s "%s"' % (paintPath, str(image.path)))   


def select_all_callback():
    dpg.set_value("przyklad",True)

    if Image.SELECTED_IMAGES:
       Image.SELECTED_IMAGES.clear() 
    for image in Image.IMAGES_TO_SHOW:
        Image.SELECTED_IMAGES.append(image)


def delete_selected_callback(sender, app_data, user_data):
    if Image.SELECTED_IMAGES:
        delete_selected_files()
        add_thumbnail_panel(parent="thumbnails_window")
    else:
        print("Nie ma czego usunac")
        pass    # We can add popup to tell user there is nothing to delete


def analyze_callback():
    analyze_images()

def copy_callback(clip = False):
    path = ask_for_directory()
    for i in Image.SELECTED_IMAGES:
        shutil.copy2(str(i.path),dst=str(path))