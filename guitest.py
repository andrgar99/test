import dearpygui.dearpygui as dpg
from math import sin
from PlotManager import *
from dropFunc import _axis_drop
dpg.create_context()

sindatax = []
sindatay = []
for i in range(0, 100):
    sindatax.append(i / 100)
    sindatay.append(0.5 + 0.5 * sin(50 * i / 100))





plotMan = PlotManager()

def add_plot():
    plotMan.add_plot()


with dpg.window(label="Test", width=2000, height=1200, tag="PlotWin"):
    dpg.add_button(label="Add plot", callback=add_plot)


# dpg.show_item_registry()
dpg.create_viewport(title='Custom Title', width=2000, height=1200)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()