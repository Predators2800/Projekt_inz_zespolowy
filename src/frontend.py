import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(width=800, height=510)
main_window = dpg.add_window(label="okno")
dpg.set_primary_window(main_window, True)

from contextlib import contextmanager
@contextmanager
def popup(*, connect_to):
    variable = dpg.add_window(show=False)
    dpg.set_item_callback(connect_to, lambda: dpg.show_item(variable))
    dpg.push_container_stack(variable)
    yield variable
    dpg.pop_container_stack()





def fn():
    dpg.delete_item("test")
    with dpg.window(tag="test") as w:
        dpg.add_text(f"okno 2, parent={w}")


with dpg.window(tag="test") as w:
    dpg.add_text(f"okno 1, parent={w}")
    dpg.add_button(label="add_window",callback=fn)
    dpg.add_button(label="show_popup", tag="show_popup")

with popup(connect_to="show_popup") as name:
    dpg.add_text(default_value="POPUP!")
    dpg.add_button(label="added without a parrent")
    







dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()