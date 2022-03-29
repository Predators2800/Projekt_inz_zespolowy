from tkinter import Widget
from dearpygui import dearpygui as dpg
from typing import List

class texture:
    def __init__(self, width, height, texture):
        self.width = width
        self.height = height
        self.texture = texture

dpg.create_context()
dpg.create_viewport(title="App",width=700, height=700)
dpg.setup_dearpygui()


primary_window = dpg.add_window()
dpg.set_primary_window(primary_window, True)


texture_registry = dpg.add_texture_registry()
width, height, chanels, data =  dpg.load_image("a.jpg")

textures: List[texture] = []
images = []

def add_texture():
    tex = dpg.add_static_texture(width, height, data, parent=texture_registry)
    textures.append(texture(width, height, tex))
    images.append(dpg.add_image(textures[-1].texture, parent=primary_window))

def delete_texture():
    dpg.delete_item(textures.pop().texture)
    dpg.delete_item(images.pop())

dpg.add_button(parent=primary_window ,label="add",callback=add_texture)
dpg.add_button(parent=primary_window ,label="delete",callback=delete_texture)


dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()