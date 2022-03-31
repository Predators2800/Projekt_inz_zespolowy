import dearpygui.dearpygui as dpg


WINDOW_HEIGHT = 600
WINDOW_WIDTH = 800
TOOLBAR_HEIGHT = 60
STATUS_PANEL_HEIGHT = 30

FONT_SIZE = 14
BUTTON_HEIGHT = 40

CURRENT_FOLDER = ""


def app_init():
    ''' 
    Main window:
    - Initialize main application window, 
    - Set display properties, 
    - Return main window object
    '''
    dpg.create_context()
    dpg.create_viewport(title="nasza aplikacja", width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
    main_window = dpg.add_window(label="okno")
    dpg.set_primary_window(main_window, True)

    main_table = dpg.add_table(
        parent=main_window, borders_innerH=True, borders_innerV=True, header_row=False
    )
    dpg.add_table_column(parent=main_table)

    return main_window, main_table


def app_setup() -> None:
    '''
    Main window:
    - TO DO 
    '''
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()


def set_default_font() -> None:
    ''' 
    Application:
    - Load font from resources folder
    - Set loaded font as default
    - Add Polish characters
    '''
    with dpg.font_registry():
        default_font = dpg.add_font("./resources/font/fira.ttf", FONT_SIZE)  # ładowanie czcionki z dysku
    dpg.bind_font(default_font)  # ustawia czcionkę jako default
    dpg.add_font_range(0x0100, 0x017D, parent=default_font)  # dodaje zakres polskich znaków


def upper_panel_init(main_table):
    '''
    Upper panel: 
    - Create toolbar's table structure
    - Set toolbar's parent to main application table (REWORK)
    - (group_u1, group_u2)
    - Returns (group_u1, group_u2)
    '''
    toolbar = dpg.add_table_row(parent=main_table, height=TOOLBAR_HEIGHT)
    toolbar_table = dpg.add_table(parent=toolbar, header_row=False)
    dpg.add_table_column(parent=toolbar_table, init_width_or_weight=3)
    dpg.add_table_column(parent=toolbar_table, init_width_or_weight=2)
    toolbar_table_row = dpg.add_table_row(parent=toolbar_table)

    group_u1 = dpg.add_group(horizontal=True, parent=toolbar_table_row)
    group_u2 = dpg.add_group(horizontal=True, parent=toolbar_table_row)

    return group_u1, group_u2


def upper_panel_layout(group_u1, group_u2, _open_folder):
    '''
    Upper panel:
    - Create toolbar buttons
    - Set on-click functions
    '''
    dpg.add_button(label="Otwórz folder", parent=group_u1, height=BUTTON_HEIGHT, callback=_open_folder)
    dpg.add_button(label="Pokaż w Eksloratorze", parent=group_u2, height=BUTTON_HEIGHT)
    dpg.add_button(label="Otwórz", parent=group_u2, height=BUTTON_HEIGHT)
    dpg.add_button(label="Kopiuj", parent=group_u2, height=BUTTON_HEIGHT)
    dpg.add_button(label="Kasuj", parent=group_u2, height=BUTTON_HEIGHT)    


def middle_panel_init(main_table):
    """
    Middle panel:
    - Initialize application's workspace
    - Set workspace's parent to main table object
    - Return workspace table and row objects
    """
    workspace = dpg.add_table_row(parent=main_table)
    workspace_table = dpg.add_table(no_host_extendY=True, resizable=True,
                                    parent=workspace, borders_innerH=False, 
                                    borders_innerV=True, header_row=True)
    workspace_table_row = dpg.add_table_row(parent=workspace_table)

    return workspace_table, workspace_table_row


def middle_panel_layout(workspace_table, workspace_table_row):
    """
    Middle panel:
    - Create workspace tables
    - Set workspace tables' parent to workspace table
    - Create file list, thumbnails and tags windows, set parent as workspace_table_row
    - Return file list and tags windows
    """
    dpg.add_table_column(parent=workspace_table, label="Pliki",init_width_or_weight=1)
    dpg.add_table_column(parent=workspace_table, label="Miniatury", init_width_or_weight=5)
    dpg.add_table_column(parent=workspace_table, label="Tagi", init_width_or_weight=1)
    file_list_window = dpg.add_child_window(parent=workspace_table_row)
    thumbnails_window = dpg.add_child_window(parent=workspace_table_row)
    tags_window = dpg.add_child_window(label="Tagi", parent=workspace_table_row)

    return file_list_window, tags_window


def workspace_on_resize(workspace_table):
    '''
    Workspace:
    - 
    '''
    WINDOW_WIDTH = dpg.get_viewport_client_width()
    WINDOW_HEIGHT = dpg.get_viewport_client_height()
    dpg.set_item_height(workspace_table, 
                        WINDOW_HEIGHT-TOOLBAR_HEIGHT-STATUS_PANEL_HEIGHT-20)


def workspace_set_viewport_resize_callback(on_resize = None):
    '''
    Workspace:
    - 
    '''
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


def lower_panel_init(main_table):
    """
    Lower panel:
    - 
    """
    status_panel = dpg.add_table_row(parent=main_table)
    status_panel_table = dpg.add_table(parent=status_panel, borders_outerH=True, 
                                       borders_outerV=True, header_row=False)
    dpg.add_table_column(parent=status_panel_table)

    status_panel_table_row = dpg.add_table_row(parent=status_panel_table, 
                                               height=STATUS_PANEL_HEIGHT)

    return status_panel_table_row


def lower_panel_layout(status_panel_table_row):
    '''
    Lower panel:
    - 
    '''
    dpg.add_slider_int(label="progressbar", default_value=30, 
                       parent=status_panel_table_row)
