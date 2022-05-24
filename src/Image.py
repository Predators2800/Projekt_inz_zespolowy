import dearpygui.dearpygui as dpg
from dict_key_tags import mapped_tags, k_mapped_tags


class Image:
    IMAGES = []
    IMAGES_TO_SHOW = set()
    SELECTED_IMAGES = []
    SELECTED_CATEGORIES = []
    CATEGORIES_TO_SHOW = set()
    
    def __init__(self, path, image_data, width, height, is_selected=False, tags=[],
                 category=[], texture_id=None, dpg_image_id=None, parent=None, dpg_image=None):
        self.path = path
        self.width = width
        self.height = height
        self.image_data = None
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
        height_to_show_image=150
        self.dpg_image = dpg.add_image(self.texture_id, parent=parent,height=height_to_show_image,width=int(height_to_show_image*self.width/self.height))
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

    def set_category(self,tags):
        cat_set = []
        tag_set = []
        for t in tags:
            print("ustawiam kategorie dla tagu", t)
            if k_mapped_tags.count(t):
                if isinstance(mapped_tags[t],list):
                    for i in mapped_tags[t]:
                        cat_set.append(i)
                        self.CATEGORIES_TO_SHOW.add(i)
                else:
                    cat_set.append(mapped_tags[t])
                    self.CATEGORIES_TO_SHOW.add(mapped_tags[t])
                tag_set.append(t)
            else:
                cat_set.append('inne')
                self.CATEGORIES_TO_SHOW.add('inne')
                tag_set.append(t)
        self.category = cat_set.copy()
        self.tags = tag_set.copy()

    def selected_tag(self, category):
        if Image.SELECTED_CATEGORIES.count(category) <= 0:
            Image.SELECTED_CATEGORIES.append(category)
        else:
            Image.SELECTED_CATEGORIES.remove(category)


