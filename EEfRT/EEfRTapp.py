import tkinter as tk
import time
import StartEndPage
import Trial

import csv
header = ['TrialNumber', 'Probability', 'Reward', 'TaskLevel', 'CompleteStatus', 'WinningStatus']
data_collection = []

import yaml
with open('configuration.yaml', 'r') as d:
    config = yaml.safe_load(d)

width_spec = 1200
heigth_spec = 800
size_spec = f'{width_spec}x{heigth_spec}'
maximum_pratice = config["maximum_practice"]
maximum_time = config["maximum_time"]
probability = config["probability"]


class EEfRTapp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.displayed_frame = None
        self.switch_frame(StartEndPage.StartPage)
        global number_of_practice
        number_of_practice = 0

    def switch_frame(self, frame_to_display):
        global frame_has_switched
        frame_has_switched = True
        new_frame = frame_to_display(self)

        if self.displayed_frame is not None:
            self.displayed_frame.destroy()

        self.displayed_frame = new_frame
        self.displayed_frame.place(relx = .5, rely = .5, anchor = "center")

    def get_frame_swtich_status(self):
        return frame_has_switched

    def set_frame_switch_status(self, boolean):
        global frame_has_switched
        frame_has_switched = boolean

    def get_maximum_practice(self):
        return maximum_pratice

    def get_maximum_time(self):
        return maximum_time

    def get_current_time(self):
        return time.time()

    def get_probability(self):
        return probability

    def new_data(self):
        global data
        if Trial.start_collect is True:
            data = []

    def record_data(self, input):
        global data
        if Trial.start_collect is True:
            data.append(f'{input + 0}')

    def data_merge(self):
        if Trial.start_collect is True:
            data_collection.append(data)


app = EEfRTapp()
app.title("EEfRT experiment")
app.geometry(size_spec)
app.mainloop()

with open('trailResult.csv', 'w', newline = '') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data_collection)


