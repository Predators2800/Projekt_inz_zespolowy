from contextlib import contextmanager
import dearpygui.dearpygui as dpg
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


def select_image_callback(sender, widget_data, image):
    image.select()
    parent = dpg.get_item_parent(sender)
    children = dpg.get_item_children(parent)
    image_file_name = children[1][1]
    conditional_color = (0, 255, 0, 255) if image.is_selected else (255, 255, 255, 255)
    dpg.configure_item(image_file_name, color=conditional_color) 


def add_thumbnail_panel(images, parent):
    """
    Create thumbnail table with images:
    -
    """
    columns = 4

    if dpg.get_alias_id("thumbnail_table"):
        dpg.delete_item("thumbnail_table")

    with dpg.table(tag="thumbnail_table", parent=parent, header_row=False,borders_innerH=True,borders_innerV=True):
        for i in range(columns):
            dpg.add_table_column()
        counter = 0
        
        if not dpg.get_value("progress_bar"):
            dpg.set_value("progress_bar", 0.0)

        while counter < len(images):
            columnsLeft = columns if counter <= len(images)-columns else len(images) % columns
            with dpg.table_row():
                while columnsLeft > 0:
                    with dpg.group() as image_cell:
                        images[counter].show(parent=image_cell)
                        dpg.set_value("progress_bar", (counter+1)/len(images))
                        dpg.configure_item("progress_bar", overlay="Loading: " + str(round((counter+1)*100/len(images), 1)) + "%")
                        with dpg.group(horizontal=True) as bottom_group:
                            dpg.add_checkbox(user_data=images[counter], callback=select_image_callback)
                            dpg.add_text(default_value=images[counter].path.name)
                            with dpg.tooltip(parent=bottom_group):
                                dpg.add_text(default_value=images[counter].path)
                    columnsLeft -= 1
                    counter += 1
    start_time = time.time()
    dpg.configure_item("progress_bar", overlay="Loading finished")
    print("czas wyświetlania miniatur",time.time()-start_time)


def add_image_tags_list(parent):
    tags = [
        "niebo",
        "trawa",
        "plaza",
        "śnieg",
        "ludzie",
        "zwierzęta",
        "samochody",
        "czerwony",
        "czarny",
        "red",
        "green",
        "blue",
        "red",
        "green",
        "blue",
        "red",
        "green",
        "blue"
    ]

    [dpg.add_checkbox(label=tag, parent=parent) for tag in tags]