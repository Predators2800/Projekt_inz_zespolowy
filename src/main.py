from frontend import *
from backend import *

app_init()
upper_panel_init()
upper_panel_layout(open_folder)

middle_panel_init()
middle_panel_layout()

lower_panel_init()
lower_panel_layout()

workspace_set_viewport_resize_callback(workspace_on_resize())
app_setup()
