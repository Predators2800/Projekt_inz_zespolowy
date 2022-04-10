from contextlib import contextmanager
import dearpygui as dpg
import time

@contextmanager
def popup(*, connect_to):
    """
    Create a popup window and connect it to a button:
    -
    """
    variable = dpg.add_window(show=False)
    dpg.set_item_callback(connect_to, lambda: dpg.show_item(variable))
    dpg.push_container_stack(variable)
    yield variable
    dpg.pop_container_stack()


def add_thumbnail_panel(IMAGE_PATHS):
    """config thumnails"""
    scale = 10
    img_width = 0
    img_height = 0
    """*******"""
    print("test",dpg.get_alias_id("tags_window"))
    print("test", dpg.get_alias_id("workspace_table_row"))
    print("test", bool(dpg.get_alias_id("texture_registry")))


    if dpg.get_alias_id("texture_registry"):
        dpg.delete_item("texture_registry")

    dpg.add_texture_registry(tag = "texture_registry",show=False)
    textureList = []
    #print("paths", IMAGE_PATHS)
    start_time = time.time()
    for path in IMAGE_PATHS:
        #print("type:",type(path))
        path= str(path)
        img_width, img_height, channels, data = dpg.load_image(path)
        texture = dpg.add_static_texture(img_width, img_height, data, parent="texture_registry")
        textureList.append(texture)
    print("czas ladowanie do rejestru",time.time()-start_time)

    def add_thumbnails(stuffList, columns = 3):
        #dpg.add_child_window(tag="thumbnail_window", label="Table of stuff",parent="thu")

        if dpg.get_alias_id("thumbnail_table"):
            dpg.delete_item("thumbnail_table")

        dpg.add_table(tag="thumbnail_table", parent="thumbnails_window", header_row=False,borders_innerH=True,borders_innerV=True)
        for i in range(columns):
            dpg.add_table_column(parent="thumbnail_table")
        counter = 0
        print("ładuje zdjęcia")
        while counter < len(stuffList):
            columnsLeft = columns if counter <= len(stuffList)-columns else len(stuffList) % columns
            row = dpg.add_table_row(tag="row"+str(counter),parent="thumbnail_table")
            while columnsLeft > 0:
                grupa = dpg.add_group(tag="group"+str(counter),parent=row)
                dpg.add_image(textureList[counter], parent=grupa,width=img_width/scale,height=img_height/scale)
                grupa2 = dpg.add_group(parent=grupa, horizontal=True)
                checkbox = dpg.add_checkbox(parent=grupa2)
                dpg.add_text(parent=grupa2, default_value="nazwa zdjecia. jpg")
                #dpg.add_text(default_value=stuffList[counter], parent=grupa)
                tooltip = dpg.add_tooltip(parent=grupa2)
                dpg.add_text(parent=tooltip, default_value=IMAGE_PATHS[counter])
                columnsLeft -= 1
                counter += 1
                #print("counter:",counter/len(stuffList))
    start_time = time.time()
    add_thumbnails(IMAGE_PATHS)
    print("czas",time.time()-start_time)
    print("dodano miniatury")
    #print(dpg.get_item_children("thumbnail_table"))

