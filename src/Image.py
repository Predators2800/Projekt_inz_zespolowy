import dearpygui.dearpygui as dpg


class Image:
    IMAGES = []
    SELECTED_IMAGES = []
    
    def __init__(self, path, image_data, width, height, is_selected=False, tags=[],
                 category=None, texture_id=None, dpg_image_id=None, parent=None, dpg_image=None):
        self.path = path
        self.width = width
        self.height = height
        self.image_data = image_data
        self.tags = tags
        self.category = category
        self.texture_id = texture_id
        self.dpg_image_id = dpg_image_id
        self.is_selected = is_selected
        self.parent = parent
        self.dpg_image = dpg_image

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
        self.parent = parent
        return self.dpg_image

    def remove(self):
        dpg.delete_item(self.texture_id)
        dpg.delete_item(self.parent)
        Image.IMAGES.remove(self)

    def select(self):
        self.is_selected = not self.is_selected
        if self.is_selected:
            Image.SELECTED_IMAGES.append(self)
        else:
            Image.SELECTED_IMAGES.remove(self)
