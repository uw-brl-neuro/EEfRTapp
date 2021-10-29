import copy
import tkinter as tk
import StartEndPage
import TestStartEndPage
import Trial
import random


# for sound generating
import platform

# for time stamp recording
import time
import datetime

# Define a csv file that collection the information of each trial
import csv
header = ['Name', 'TrialNumber', 'T-TrialStart', 'Probability', 'TaskLevel', 'T-DecisionMade', 'Reward', 'CompleteStatus', 'T-TaskComplete', 'WinningStatus']
data_collection = []

# Read a yaml file to configure the application accordingly
import yaml
import os
yaml_file_path = os.path.join(os.path.dirname(__file__), "configuration.yaml")
with open(f'{yaml_file_path}', 'r') as d:
    config = yaml.safe_load(d)

# Read and store the data if there exists a previous data file
csv_file_path = os.path.join(os.path.dirname(__file__), "trialResult.csv")
if os.path.isfile(csv_file_path) is True:
    with open(f'{csv_file_path}', 'r', newline = '') as oldf:
        reader = csv.reader(oldf)
        old_header = next(reader)
        for row in reader:
            data_collection.append(row)

# Sound data
sound_header = ['Name', 'T-Sound', 'frequency']
sound_data_collection = []
sound_csv_file_path = os.path.join(os.path.dirname(__file__), "soundData.csv")
if os.path.isfile(sound_csv_file_path) is True:
    with open(f'{sound_csv_file_path}', 'r', newline = '') as oldf_s:
        reader = csv.reader(oldf_s)
        old_header = next(reader)
        for row in reader:
            sound_data_collection.append(row)

# Define the width and height size of the window of the application
width_spec = config["width_spec"]
height_spec = config["height_spec"]
size_spec = f'{width_spec}x{height_spec}'

# Initialize variables based on configuration
maximum_pratice = config["maximum_practice"]
maximum_time = config["maximum_time"]
probability = config["probability"]
reward_lowerbound = config["reward_lowerbound"]
reward_upperbound = config["reward_upperbound"]
easy_time_limit = config["easy_time_limit"]
hard_time_limit = config["hard_time_limit"]
easy_press_level = config["easy_press_level"]
hard_press_level = config["hard_press_level"]
font_size = config["font_size"]
original_font_size = copy.deepcopy(font_size)


# Create an EEfRT application
class EEfRTapp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.displayed_frame = None
        self.switch_frame(StartEndPage.StartPage)
        global number_of_practice
        number_of_practice = 0

        def open_test(event):
            self.switch_frame(TestStartEndPage.StartPage)

        self.bind("<Control_L>t", open_test)

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

    def get_reward_lowerbound(self):
        return reward_lowerbound

    def get_reward_upperbound(self):
        return reward_upperbound

    def get_easy_time_limit(self):
        return easy_time_limit

    def get_hard_time_limit(self):
        return hard_time_limit

    def get_easy_press_level(self):
        return easy_press_level

    def get_hard_press_level(self):
        return hard_press_level

    def get_font_size(self):
        return font_size

    def get_original_font_size(self):
        return original_font_size

    def set_font_size(self, size):
        global font_size
        font_size = size

    # Create a set of new data for a trial
    # It checks if data needs to be collected in current state
    def new_data(self):
        global data
        if Trial.start_collect is True:
            data = []
            data.append(StartEndPage.participant_name)

    # Record the input data and store it in the set of new data created
    # at the beginning of each trial
    # It checks if data needs to be collected in current state
    # Input: pass an input that needs to be added to the information of current trial
    def record_data(self, input):
        global data
        if Trial.start_collect is True:
            # boolean is recorded as 0 (False) or 1 (True)
            if type(input) is bool:
                data.append(f'{input + 0}')
            else:
                data.append(f'{input}')

    # record time stamp when called
    def record_time(self):
        ts = time.time()
        self.record_data(datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))

    # Merge the data collected in this trial with the records of previous trials
    def data_merge(self):
        if Trial.start_collect is True:
            data_collection.append(data)

    # sound generating
    def sound_generating(self):
        if Trial.start_collect is True:
            sound_data = []
            sound_data.append(StartEndPage.participant_name)
            frequency = random.uniform(100, 500)
            duration = 1
            if platform.system() == 'Darwin':
                import os
                ts = time.time()
                sound_data.append(datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
                os.system('play -n synth %s sin %s' % (duration / 1000, frequency))
                sound_data.append(frequency)
            elif platform.system() == 'Windows':
                import winsound
                ts = time.time()
                sound_data.append(datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
                winsound.Beep(int(frequency), duration)
                sound_data.append(frequency)
            sound_data_collection.append(sound_data)
            if random.randint(0, 100) <= 40:
                interval_to_next = random.uniform(1000, 3000)
            else:
                interval_to_next = random.uniform(5000, 10000)
            self.after(int(interval_to_next), lambda: self.sound_generating())

# Initiate and run the app
app = EEfRTapp()
app.title("EEfRT experiment")
app.geometry(size_spec)
app.mainloop()

# Create a csv file based on the data collected throughout the experiment
with open(f'{csv_file_path}', 'w', newline ='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data_collection)

# Create a csv file based on the sound data collected throughout the experiment
with open(f'{sound_csv_file_path}', 'w', newline='') as s_f:
    writer = csv.writer(s_f)
    writer.writerow(sound_header)
    writer.writerows(sound_data_collection)







