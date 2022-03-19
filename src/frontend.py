import dearpygui.dearpygui as dpg
dpg.create_context()
dpg.create_viewport(title='nasza aplikacja', width=800, height=510)
main_window = dpg.add_window(label='okno')
dpg.set_primary_window(main_window, True)

with dpg.font_registry():
    default_font = dpg.add_font("../resources/font/fira.ttf", 14) # ładowanie czcionki z dysku
dpg.bind_font(default_font) # ustawia czcionkę jako default
dpg.add_font_range(0x0100,0x017D, parent=default_font) # dodaje zakres polskich znaków

"""MAIN_WINDOW"""
tabela = dpg.add_table(parent=main_window, borders_innerH=True, borders_innerV=True, header_row=False)
dpg.add_table_column(parent=tabela)


"""UPPER_PANEL"""
toolbar = dpg.add_table_row(parent=tabela, height=60)
toolbar_table = dpg.add_table(parent=toolbar,header_row=False)
dpg.add_table_column(parent=toolbar_table, init_width_or_weight=4)
dpg.add_table_column(parent=toolbar_table, init_width_or_weight=1)
toolbar_table_row = dpg.add_table_row(parent=toolbar_table)

group_u1 = dpg.add_group(horizontal=True, parent=toolbar_table_row)
group_u2 = dpg.add_group(horizontal=True, parent=toolbar_table_row)

dpg.add_button(label='Otwórz folder', parent=group_u1)
dpg.add_button(label='Pokaż w Eksloratorze', parent=group_u2)
dpg.add_button(label='Otwórz', parent=group_u2)
dpg.add_button(label='Kopiuj', parent=group_u2)
dpg.add_button(label='Kasuj', parent=group_u2)


"""MIDDLE_PANEL"""
workspace = dpg.add_table_row(parent=tabela)
workspace_table = dpg.add_table(parent=workspace, borders_innerH=False, borders_innerV=True, header_row=False)
dpg.add_table_column(parent=workspace_table, init_width_or_weight=8)
dpg.add_table_column(parent=workspace_table, init_width_or_weight=1)
workspace_table_row = dpg.add_table_row(parent=workspace_table)

group_m1 = dpg.add_group(horizontal=True, parent=workspace_table_row)
view_window = dpg.add_child_window(label='podglad',width=200, height=350, parent=group_m1, menubar=True)
dpg.add_text(parent=view_window,default_value='tekst do wyswietlenia')

tags = ['red','green','blue','red','green','blue','red','green','blue','red','green','blue','red','green','blue','red','green','blue']
tags_window = dpg.add_child_window(label='tags',parent=workspace_table_row,height=350)

for tag in tags:
    dpg.add_checkbox(label=tag,parent=tags_window)




"""LOWER_PANEL"""

status_panel = dpg.add_table_row(parent=tabela,height=30)
dpg.add_slider_int(label='progressbar',parent=status_panel)







dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()