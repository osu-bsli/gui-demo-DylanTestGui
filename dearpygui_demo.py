import dearpygui.dearpygui as gui

gui.create_context()
gui.create_viewport(title='dearpygui demo')

with gui.window(label="dearpygui demo"):
    gui.add_text("Hello, world!")
    gui.add_button(label="Button")
    gui.add_input_text(label="string", default_value="Quick brown fox")
    gui.add_slider_float(label="float", default_value=0.273, max_value=1)

gui.show_imgui_demo()
gui.show_implot_demo()
gui.show_style_editor()

gui.setup_dearpygui()
gui.show_viewport()
gui.maximize_viewport()
gui.start_dearpygui()
gui.destroy_context()