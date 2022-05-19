from contextlib import contextmanager
import dearpygui.dearpygui as dpg
import time
from Image import Image
from dict_key_tags import categories


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


def select_image_callback(sender, widget_data, image):
    image.select()
    parent = dpg.get_item_parent(sender)
    children = dpg.get_item_children(parent)
    image_file_name = children[1][1]
    conditional_color = (0, 255, 0, 255) if image.is_selected else (255, 255, 255, 255)
    dpg.configure_item(image_file_name, color=conditional_color)


def add_thumbnail_panel(parent):
    """
    Create thumbnail table with images:
    -
    """
    columns = 4

    if dpg.get_alias_id("thumbnail_table"):
        dpg.delete_item("thumbnail_table")

    with dpg.table(tag="thumbnail_table", parent=parent, header_row=False, borders_innerH=True, borders_innerV=True):
        for i in range(columns):
            dpg.add_table_column()
        counter = 0
        
        if not dpg.get_value("progress_bar"):
            dpg.set_value("progress_bar", 0.0)

        while counter < len(Image.IMAGES_TO_SHOW):
            columns_left = columns if counter <= len(Image.IMAGES_TO_SHOW)-columns else len(Image.IMAGES_TO_SHOW) % columns
            with dpg.table_row():
                while columns_left > 0:
                    with dpg.group() as image_cell:
                        Image.IMAGES_TO_SHOW[counter].show(parent=image_cell)
                        dpg.set_value("progress_bar", (counter+1)/len(Image.IMAGES_TO_SHOW))
                        dpg.configure_item("progress_bar", overlay="Loading: " + str(round((counter+1)*100/len(Image.IMAGES_TO_SHOW), 1)) + "%")
                        with dpg.group(horizontal=True) as bottom_group:
                            dpg.add_checkbox(user_data=Image.IMAGES_TO_SHOW[counter], callback=select_image_callback)
                            dpg.add_text(default_value=Image.IMAGES_TO_SHOW[counter].path.name)
                            with dpg.tooltip(parent=bottom_group):
                                dpg.add_text(default_value=Image.IMAGES_TO_SHOW[counter].path)
                                dpg.add_text(default_value=Image.IMAGES_TO_SHOW[counter].tags)
                    columns_left -= 1
                    counter += 1
    start_time = time.time()
    dpg.configure_item("progress_bar", overlay="Loading finished")
    print("czas wyświetlania miniatur", time.time()-start_time)


def refresh_image_to_show():
    Image.IMAGES_TO_SHOW.clear()
    for img in Image.IMAGES:
        for cat in img.category:
            if Image.SELECTED_CATEGORIES.count(cat):
                Image.IMAGES_TO_SHOW.append(img)
    #print(len("wyswietlam obrazkow:",Image.IMAGES_TO_SHOW))


def tag_checkbox_callback(sender, widget_data, image):
    Image.selected_tag(self=None, category=dpg.get_item_label(sender))
    refresh_image_to_show()
    add_thumbnail_panel(parent="thumbnails_window")


def add_image_category_list(parent):
    cats = categories
    cats.sort()
    cats.append('inne')

    [dpg.add_checkbox(label=category, parent=parent,callback=tag_checkbox_callback) for category in cats]


def refresh_image_category():
    print(len(Image.CATEGORIES_TO_SHOW))
    print(Image.CATEGORIES_TO_SHOW)
    dpg.delete_item("tags_window")
    dpg.add_child_window(tag="tags_window", label="Okno-kategorii",parent="workspace_table_row")
    [dpg.add_checkbox(label=category, parent="tags_window", callback=tag_checkbox_callback) for category in Image.CATEGORIES_TO_SHOW]