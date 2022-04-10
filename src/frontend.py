import dearpygui.dearpygui as dpg
from backend import open_folder

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 800
TOOLBAR_HEIGHT = 60
STATUS_PANEL_HEIGHT = 30

FONT_SIZE = 14
BUTTON_HEIGHT = 40

CURRENT_FOLDER = ""

"""CREATE APP WINDOW"""


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
    dpg.add_texture_registry(tag = "texture_registry",show=False)

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
                            dpg.add_button(label="Otwórz folder", height=BUTTON_HEIGHT, callback=open_folder)
                        with dpg.group(tag="group_toolbar_2", horizontal=True):
                            dpg.add_button(label="Pokaż w Eksloratorze", height=BUTTON_HEIGHT)
                            dpg.add_button(label="Otwórz", height=BUTTON_HEIGHT)
                            dpg.add_button(label="Kopiuj", height=BUTTON_HEIGHT)
                            dpg.add_button(label="Kasuj", height=BUTTON_HEIGHT)
            with dpg.table_row(tag="workspace"):
                with dpg.table(tag="workspace_table", no_host_extendY=True, resizable=True, borders_innerH=False, borders_innerV=True, header_row=True):
                    dpg.add_table_column(label="Miniatury", init_width_or_weight=5)
                    dpg.add_table_column(label="Tagi", init_width_or_weight=1)
                    with dpg.table_row(tag="workspace_table_row"):
                        dpg.add_child_window(tag = "thumbnails_window")
                        dpg.add_child_window(tag = "tags_window",label="Tagi")
            with dpg.table_row(tag="status_panel"):
                with dpg.table(tag="status_panel_table", borders_outerH=True, borders_outerV=True, header_row=False):
                    dpg.add_table_column()
                    with dpg.table_row(tag="status_panel_table_row", height=STATUS_PANEL_HEIGHT):
                        dpg.add_slider_int(label="progressbar", default_value=30)


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
        default_font = dpg.add_font("./resources/font/fira.ttf", FONT_SIZE)  # ładowanie czcionki z dysku
    dpg.bind_font(default_font)  # ustawia czcionkę jako default
    dpg.add_font_range(0x0100, 0x017D, parent=default_font)  # dodaje zakres polskich znaków


def set_global_callbacks():
    """
    Initialize callbacks:
    -
    """
    dpg.set_viewport_resize_callback(workspace_viewport_resize_callback)


def workspace_viewport_resize_callback():
    """
    Initiaize viewport resize callback:
    - gets called each time window is being resized by the user
    -
    """
    WINDOW_WIDTH = dpg.get_viewport_client_width()
    WINDOW_HEIGHT = dpg.get_viewport_client_height()
    dpg.set_item_height("workspace_table",
                        WINDOW_HEIGHT-TOOLBAR_HEIGHT-STATUS_PANEL_HEIGHT-20)



def workspace_add_photo_tags(tags_window):
    """
    Workspace:
    -
    """
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
        "blue"
    ]

    [dpg.add_checkbox(label=tag, parent=tags_window) for tag in tags]
