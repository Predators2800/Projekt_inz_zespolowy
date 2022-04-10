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


class Image():
    def __init__(self, path, category, texture, dpg_image):
        self.path = path
        self.category = category
        self.texture = texture
        self.dpg_image = dpg_image

    def __repr__(self) -> str:
        return f"{self.path}, {self.category}"

    def show(self, parent):
        self.dpg_image = dpg.add_image(self.texture, parrent=parent)
        return self.dpg_image

    def remove(self):
        dpg.delete_item(self.dpg_image)

with dpg.window():
    dpg.add_button(label="show_popup", tag="show_popup")

with popup(connect_to="show_popup"):
    dpg.add_text(default_value="POPUP!")
    dpg.add_button(label="added without a parrent")
    
categories = ["cat1","cat2","cat3","cat4"]

from random import choice

images = {}

for o in range(1_0):
    image = Image(o,choice(categories))
    if image.category not in images:
        images[image.category] = [image]
    images[image.category].append(image)
print("finished creating objects")

print(images)



dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()