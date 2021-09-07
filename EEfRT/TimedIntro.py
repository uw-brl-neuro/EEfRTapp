import tkinter as tk
from tkinter import ttk
from tkinter import font as tkFont
import Trial
import PracticeIntro

# Create the intro page to the timed trial session
# Provides option to redo the last practice trial, thereby giving the user one more practice trial
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
        lbl.grid(row = 0, column = 1)


        btn_to_PracticeTrial = ttk.Button(subFrame,
                                          text="One More Practice",
                                          command=lambda: self.one_more_practice(master))
        btn_to_PracticeTrial.grid(row=2, column=0)

        btn_to_trial = ttk.Button(subFrame,
                                  text="Confirm",
                                  command=lambda: master.switch_frame(Trial.TrialCue))
        btn_to_trial.grid(row = 2, column=2)

    # Redo the last practice trial
    def one_more_practice(self, master):
        PracticeIntro.number_of_practice -= 1
        Trial.trial_number -= 1
        master.switch_frame(PracticeIntro.PracticeTrial)




