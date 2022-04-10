import dearpygui.dearpygui as dpg


WINDOW_HEIGHT = 600
WINDOW_WIDTH = 800
TOOLBAR_HEIGHT = 60
STATUS_PANEL_HEIGHT = 30

FONT_SIZE = 14
BUTTON_HEIGHT = 40

CURRENT_FOLDER = ""

# TEXTURE_REGISTRY = dpg.add_texture_registry(show=False)
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
    dpg.add_window(tag="main_window", label="okno")
    dpg.set_primary_window("main_window", True)

    dpg.add_table(
        tag="main_table", parent="main_window", borders_innerH=True, borders_innerV=True, header_row=False
    )
    dpg.add_table_column(tag="main_column", parent="main_table")


def app_setup() -> None:
    """
    Main window:
    - TO DO
    """

    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
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


def upper_panel_init():
    """
    Upper panel:
    - Create toolbar's table structure
    - Set toolbar's parent to main application table (REWORK)
    - (group_u1, group_u2)
    - Returns (group_u1, group_u2)
    """

    dpg.add_table_row(tag="toolbar", parent="main_table", height=TOOLBAR_HEIGHT)
    dpg.add_table(tag="toolbar_table", parent="toolbar", header_row=False)
    dpg.add_table_column(tag="toolbar_1_col", parent="toolbar_table", init_width_or_weight=3)
    dpg.add_table_column(tag="toolbar_2_col", parent="toolbar_table", init_width_or_weight=2)
    dpg.add_table_row(tag="toolbar_table_row", parent="toolbar_table")

    dpg.add_group(tag="group_toolbar_1", horizontal=True, parent="toolbar_table_row")
    dpg.add_group(tag="group_toolbar_2", horizontal=True, parent="toolbar_table_row")


def upper_panel_layout(_open_folder):
    """
    Upper panel:
    - Create toolbar buttons
    - Set on-click functions
    """

    dpg.add_button(label="Otwórz folder", parent="group_toolbar_1", height=BUTTON_HEIGHT, callback=_open_folder)
    dpg.add_button(label="Pokaż w Eksloratorze", parent="group_toolbar_2", height=BUTTON_HEIGHT)
    dpg.add_button(label="Otwórz", parent="group_toolbar_2", height=BUTTON_HEIGHT)
    dpg.add_button(label="Kopiuj", parent="group_toolbar_2", height=BUTTON_HEIGHT)
    dpg.add_button(label="Kasuj", parent="group_toolbar_2", height=BUTTON_HEIGHT)


def middle_panel_init():
    """
    Middle panel:
    - Initialize application's workspace
    - Set workspace's parent to main table object
    - Return workspace table and row objects
    """

    dpg.add_table_row(tag="workspace", parent="main_table")
    dpg.add_table(tag="workspace_table", no_host_extendY=True, resizable=True,
                  parent="workspace", borders_innerH=False, borders_innerV=True, header_row=True)
    dpg.add_table_row(tag="workspace_table_row", parent="workspace_table")


def middle_panel_layout():
    """
    Middle panel:
    - Create workspace tables
    - Set workspace tables' parent to workspace table
    - Create file list, thumbnails and tags windows, set parent as workspace_table_row
    - Return file list and tags windows
    """

    #dpg.add_table_column(parent="workspace_table", label="Pliki",init_width_or_weight=1)
    dpg.add_table_column(parent="workspace_table", label="Miniatury", init_width_or_weight=5)
    dpg.add_table_column(parent="workspace_table", label="Tagi", init_width_or_weight=1)
    #dpg.add_child_window(tag = "file_list_window",parent="workspace_table_row")
    dpg.add_child_window(tag = "thumbnails_window",parent="workspace_table_row")
    dpg.add_child_window(tag = "tags_window",label="Tagi", parent="workspace_table_row")


def workspace_on_resize():
    """
    Workspace:
    -
    """
    WINDOW_WIDTH = dpg.get_viewport_client_width()
    WINDOW_HEIGHT = dpg.get_viewport_client_height()
    dpg.set_item_height("workspace_table",
                        WINDOW_HEIGHT-TOOLBAR_HEIGHT-STATUS_PANEL_HEIGHT-20)


def workspace_set_viewport_resize_callback(on_resize = None):
    """
    Workspace:
    -
    """
    if on_resize:
        dpg.set_viewport_resize_callback(on_resize)



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


def lower_panel_init():
    """
    Lower panel:
    -
    """
    dpg.add_table_row(tag="status_panel",parent="main_table")
    dpg.add_table(tag="status_panel_table",parent="status_panel", borders_outerH=True,
                                       borders_outerV=True, header_row=False)
    dpg.add_table_column(parent="status_panel_table")

    dpg.add_table_row(tag="status_panel_table_row",parent="status_panel_table",
                                               height=STATUS_PANEL_HEIGHT)



def lower_panel_layout():
    """
    Lower panel:
    -
    """
    dpg.add_slider_int(label="progressbar", default_value=30,
                       parent="status_panel_table_row")
