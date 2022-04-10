class Image():

    def __init__(self, path, image_data, width, height , is_selected=False, tags=[]):
        self.path = path
        self.image_data = image_data
        self.width = width
        self.height = height
        self.is_selected = is_selected
        self.tags = tags