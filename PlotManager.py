import dearpygui.dearpygui as dpg
import numpy as np

import random

from dropFunc import _axis_drop

class PlotManager:
    def __init__(self) -> None:
        pass


    def __init__(self):
        self.plot_id = []
        self.yaxis_id = []

    def generate_random_dataset(self, num_points):
        x_values = np.linspace(0, 0.001, num_points)  # Generate x values evenly spaced between 0 and 10
        random_frequency = random.uniform(1000, 100000)  # Generate a random frequency between 1 and 10
        y_values = np.sin(2 * np.pi * random_frequency * x_values)
        # Calculate y values using a sine wave with the random frequency and add some random noise

        return x_values, y_values


    def add_line_series(self):
        if self.yaxis_id:
            x, y = self.generate_random_dataset(10000)

            # dpg.push_container_stack(dpg.add_line_series(x, y, label=f"{random.uniform(1,100)}", parent=self.yaxis_id[-1]))
            # dpg.pop_container_stack()
            dpg.add_line_series(x, y, label=f"{random.uniform(1,100)}", parent=self.yaxis_id[-1])


    def delete_plot(self):
        if self.plot_id:
            dpg.delete_item(self.plot_id[-1])
            self.plot_id.pop()
            self.yaxis_id.pop()




    def add_plot(self):
        yaxis_id = dpg.generate_uuid()
        plot_id = dpg.generate_uuid()

        self.plot_id.append(plot_id)
        self.yaxis_id.append(yaxis_id)

        x, y = self.generate_random_dataset(10000)
   
        dpg.push_container_stack(dpg.add_plot(label="Line Series", height=400, width=-1, parent="PlotWin", anti_aliased=True, tag=plot_id))
        dpg.add_plot_legend()   
        dpg.add_plot_axis(dpg.mvXAxis, label="x")
        dpg.add_plot_axis(dpg.mvYAxis, label="y1", tag=yaxis_id, payload_type="plotting", drop_callback=_axis_drop)
        dpg.add_plot_axis(dpg.mvYAxis, label="y2", tag=dpg.generate_uuid(), payload_type="plotting", drop_callback=_axis_drop)
        dpg.add_line_series(x, y, label="Random Freq", parent=yaxis_id, tag=dpg.generate_uuid())
        us = dpg.last_item()
        dpg.add_button(label="drag", user_data = us, parent=us)


        with dpg.drag_payload(parent=dpg.last_item(), drag_data=(x,y , "fag"), payload_type="plotting"):
            dpg.add_text(dpg.get_item_label(us))
            dpg.add_simple_plot(label="", default_value=y)


        dpg.pop_container_stack()
     