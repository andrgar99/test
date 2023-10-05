import dearpygui.dearpygui as dpg
from math import sin

dpg.create_context()

sindatax = []
sindatay = []
for i in range(0, 100):
    sindatax.append(i / 100)
    sindatay.append(0.5 + 0.5 * sin(50 * i / 100))



def _axis_drop(sender, app_data):
    dpg.add_scatter_series(app_data[0], app_data[1], label=app_data[2], parent=sender)
    us = dpg.last_item()
    dpg.add_button(label="Delete Series", user_data = us, parent=us, callback=lambda s, a, u: dpg.delete_item(u))
    dpg.add_button(label="drag", user_data = us, parent=us)
    with dpg.drag_payload(parent=dpg.last_item(), drag_data=(app_data[0], app_data[1], app_data[2]), payload_type="plotting"):
        dpg.add_text(app_data[2])
        dpg.add_simple_plot(label="", default_value=app_data[1])


with dpg.window(label="Test", width=400, height=400):
    with dpg.plot(label="Test Plot", height=400, width=-1, crosshairs=True):
        dpg.add_plot_legend(payload_type="plotting", outside=False)
        dpg.add_plot_axis(dpg.mvXAxis, label="x")

 
        dpg.add_plot_axis(dpg.mvYAxis, label="y1", drop_callback=_axis_drop, payload_type="plotting")     
        dpg.add_plot_axis(dpg.mvYAxis, label="y2", drop_callback=_axis_drop, payload_type="plotting")

        dpg.add_stem_series(sindatax, sindatay, label="y2 stem", parent=dpg.last_item(), tag = "lol", user_data=(sindatax, sindatay))


        us = dpg.last_item()
        dpg.add_button(label="drag", user_data = us, parent=us)
        with dpg.drag_payload(parent=dpg.last_item(), drag_data=(dpg.get_item_user_data(us)[0],dpg.get_item_user_data(us)[1] , dpg.get_item_label(us)), payload_type="plotting"):
            dpg.add_text(dpg.get_item_label(us))
            dpg.add_simple_plot(label="", default_value=dpg.get_item_user_data(us)[1])

    with dpg.plot(label="Test Plot2", height=400, width=-1, crosshairs=True):
        dpg.add_plot_legend(payload_type="plotting", outside=False)
        dpg.add_plot_axis(dpg.mvXAxis, label="x")
        dpg.add_plot_axis(dpg.mvYAxis, label="y1", drop_callback=_axis_drop, payload_type="plotting")
        dpg.add_plot_axis(dpg.mvYAxis, label="y2", drop_callback=_axis_drop, payload_type="plotting")

dpg.show_item_registry()
dpg.create_viewport(title='Custom Title', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()