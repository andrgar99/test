import dearpygui.dearpygui as dpg

from test import Person

from math import cos, sin

from PlotManager import *


dpg.create_context()




plotMan = PlotManager()

def add_plot2():
    plotMan.add_plot()

def delete_plot():
    plotMan.delete_plot()

def add_series():
    plotMan.add_line_series()

with dpg.window(label="Button panel", tag="win", height=100, width=200):
    dpg.add_button(label="Add Line Series", callback=add_series)
    dpg.add_button(label="add plot", callback=add_plot2)

    dpg.add_button(label="Delete plot", callback=delete_plot)
 
with dpg.window(label="Plot Window", tag="plots", height=1000, width=1300,pos=(200,0)):
    pass


dpg.create_viewport(title="Plotter", height=1000, width=1500)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()

















