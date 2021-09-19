import tkinter as tk
from tkinter import ttk
from tkinter import font as tkFont
import TestMenu
import time
import datetime
import random
import StartEndPage
import TestTrial


class Autotest(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        # subFrame = tk.Frame(master=self)
        # subFrame.pack()
        #
        # # Generate a reward based on the range given by the configuration
        # def reward_generator(master):
        #     global current_reward
        #     current_reward = random.uniform(master.get_reward_lowerbound(), master.get_reward_upperbound()).__round__(2)
        #     return current_reward
        #
        # # Generate the probability of winning the current trial based on the configuration
        # def probability_generator(master):
        #     global probability_to_win
        #     probability_to_win = random.choice(master.get_probability())
        #     return probability_to_win
        #
        # lbl = tk.Label(subFrame,
        #                text="TEST MODE", font=tkFont.Font(size=(master.get_font_size() - 5)),
        #                fg="red")
        # lbl.grid(row=0, column=0)
        #
        # progress = ttk.Progressbar(subFrame,
        #                            orient=tk.HORIZONTAL, length=500, maximum = TestMenu.number_of_entry + 1,
        #                            mode='determinate')
        # progress.grid(row=1, column=0)
        #
        StartEndPage.participant_name = "T-Admin"

        # for i in range(TestMenu.number_of_entry):
        #     master.new_data()
        #     master.record_data(i + 1)
        #     ts = time.time()
        #     master.record_data(datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
        #     master.record_data(probability_generator(master))
        #     task_level = random.choice([0, 1])
        #     master.record_data(task_level)
        #     if task_level == 0:
        #         master.record_data(1)
        #     else:
        #         master.record_data(reward_generator(master))
        #     master.record_data(random.choice([0, 1]))
        #     master.record_data(random.choice([0, 1]))
        #     master.data_merge()
        #     progress.step(1)


        if TestTrial.trial_number == TestMenu.number_of_entry:
            self.after(0, lambda: master.switch_frame(StartEndPage.EndPage))
        else:
            self.after(0, lambda: master.switch_frame(TestTrial.TrialCue))
            progress.step(1)


