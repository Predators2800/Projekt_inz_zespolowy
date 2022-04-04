from frontend import *
from backend import *


app_window, main_table = app_init()
set_default_font()

group_u1, group_u2 = upper_panel_init(main_table)
upper_panel_layout(group_u1, group_u2, open_folder)

workspace_table, workspace_table_row = middle_panel_init(main_table)
file_list_window, tags_window = middle_panel_layout(workspace_table, workspace_table_row)

workspace_add_photo_tags(tags_window)

status_panel = lower_panel_init(main_table)
lower_panel_layout(status_panel)

workspace_set_viewport_resize_callback(workspace_on_resize(workspace_table))
app_setup()
