import tkinter as tk
import time
import StartEndPage
import Trial

# Define a csv file that collection the information of each trial
import csv
header = ['TrialNumber', 'Probability', 'Reward', 'TaskLevel', 'CompleteStatus', 'WinningStatus']
data_collection = []

# Read a yaml file to configure the application accordingly
import yaml
import os
file_path = os.path.join(os.path.dirname(__file__), "configuration.yaml")
with open(f'{file_path}', 'r') as d:
    config = yaml.safe_load(d)

# Define the width and height size of the window of the application
width_spec = 1200
heigth_spec = 800
size_spec = f'{width_spec}x{heigth_spec}'

# Initialize variables based on configuration
maximum_pratice = config["maximum_practice"]
maximum_time = config["maximum_time"]
probability = config["probability"]


# Create an EEfRT application
class EEfRTapp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.displayed_frame = None
        self.switch_frame(StartEndPage.StartPage)
        global number_of_practice
        number_of_practice = 0

    # Allows the EEfRT app to switch from one frame to another
    def switch_frame(self, frame_to_display):
        global frame_has_switched
        frame_has_switched = True
        new_frame = frame_to_display(self)

        if self.displayed_frame is not None:
            self.displayed_frame.destroy()

        self.displayed_frame = new_frame
        # Centered the content of the frame
        self.displayed_frame.place(relx = .5, rely = .5, anchor = "center")

    # Return if the app has switched the frame or not
    # The default setting is True every time the frame is switched
    # When needed to track if current frame has been switched,
    # manually turned this variable to False
    def get_frame_swtich_status(self):
        return frame_has_switched

    # Allow the user to manually change frame switched status
    # Boolean: pass True/False to change the status of frame switch
    def set_frame_switch_status(self, boolean):
        global frame_has_switched
        frame_has_switched = boolean

    # Obtain the maximum practice allowed given by the configuration
    def get_maximum_practice(self):
        return maximum_pratice

    # Obtain the duration of the timed trial
    def get_maximum_time(self):
        return maximum_time

    # Get current time given by the system of which this computer is run on
    # Be careful that if duration calculation is needed,
    # make sure the system time does not change during the process
    def get_current_time(self):
        return time.time()

    # Get the combination of probability that the app can choose from
    # based on the configuration given for the winning probability of each trial
    def get_probability(self):
        return probability

    # Create a set of new data for a trial
    # It checks if data needs to be collected in current state
    def new_data(self):
        global data
        if Trial.start_collect is True:
            data = []

    # Record the input data and store it in the set of new data created
    # at the beginning of each trial
    # It checks if data needs to be collected in current state
    # Input: pass an input that needs to be added to the information of current trial
    def record_data(self, input):
        global data
        if Trial.start_collect is True:
            data.append(f'{input + 0}')

    # Merge the data collected in this trial with the records of previous trials
    def data_merge(self):
        if Trial.start_collect is True:
            data_collection.append(data)

# Initiate and run the app
app = EEfRTapp()
app.title("EEfRT experiment")
app.geometry(size_spec)
app.mainloop()

# Create a csv file based on the data collected throughout the experiment
with open('trailResult.csv', 'w', newline = '') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data_collection)


