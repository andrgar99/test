import dearpygui.dearpygui as dpg


def _axis_drop(sender, app_data):
    dpg.add_scatter_series(app_data[0], app_data[1], label=app_data[2], parent=sender)
    us = dpg.last_item()
    dpg.add_button(label="Delete Series", user_data = us, parent=us, callback=lambda s, a, u: dpg.delete_item(u))
    dpg.add_button(label="drag", user_data = us, parent=us)
    with dpg.drag_payload(parent=dpg.last_item(), drag_data=(app_data[0], app_data[1], app_data[2]), payload_type="plotting"):
        dpg.add_text(app_data[2])
        dpg.add_simple_plot(label="", default_value=app_data[1])