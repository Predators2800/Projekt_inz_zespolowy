import dearpygui.dearpygui as dpg
class Image():

    def __init__(self, path, image_data, width, height , is_selected=False, tags=[]):
        self.path = path
        self.image_data = image_data
        self.width = width
        self.height = height
        self.is_selected = is_selected
        self.tags = tags
    def wyswietl(self):
        dpg.add_button(callback=delete,user_data=self)

def delete(obiektimage):
    obiektimage.path