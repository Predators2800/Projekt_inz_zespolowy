import dearpygui.dearpygui as dpg

class Image():
    
    def __init__(self, path, image_data, width, height , is_selected=False, tags=[], category=None, texture_id=None, dpg_image_id=None):
        self.path = path
        self.width = width
        self.height = height
        self.image_data = image_data
        self.tags = tags
        self.category = category
        self.texture_id = texture_id
        self.dpg_image_id = dpg_image_id
        self.is_selected = is_selected

    def __repr__(self) -> str:
        return f"path: {self.path}\n\
                width: {self.width}\n\
                height: {self.height}\n\
                tags: {self.tags}\n\
                category: {self.category}\n\
                texture_id: {self.texture_id}\n\
                dpg_image_id: {self.dpg_image_id}\n\
                is_selected: {self.is_selected}"

    def show(self, parent):
        self.dpg_image = dpg.add_image(self.texture_id, parent=parent)
        return self.dpg_image

    def remove(self):
        dpg.delete_item(self.dpg_image)
