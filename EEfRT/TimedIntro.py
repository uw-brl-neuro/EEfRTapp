import tkinter as tk
from tkinter import ttk
from tkinter import font as tkFont
import Trial

class TimedTrialIntro(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        Trial.start_time = master.get_current_time()
        Trial.start_collect = True

        subFrame = tk.Frame(master=self)
        subFrame.pack()

        lbl = tk.Label(subFrame,
                       text = "Practice session has ended. Timed trials will now begin",
                       font= tkFont.Font(size=25))
        lbl.grid(row = 0, column = 0)

        btn_to_trial = ttk.Button(subFrame,
                                  text="Confirm",
                                  command=lambda: master.switch_frame(Trial.TrialCue))
        btn_to_trial.grid(row = 1, column=0)




