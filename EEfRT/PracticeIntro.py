import tkinter as tk
from tkinter import ttk
from tkinter import font as tkFont
import StartEndPage
import Trial

global number_of_practice

class PracticeIntro(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        subFrame = tk.Frame(master=self)
        subFrame.pack()

        Trial.start_collect = False
        Trial.trial_number = 0 - master.get_maximum_practice()

        lbl = tk.Label(subFrame,
                       text = f"Before we officially begin, you would play {master.get_maximum_practice()} practice trials",
                       font= tkFont.Font(size=25))
        lbl.grid(row = 0, column = 1)
        lbl2 = tk.Label(subFrame,
                        text = "[Detailed Explanation To Be Inserted]", font = tkFont.Font(size=15))

        lbl2.grid(row = 1, column = 1)

        btn_to_startpage = ttk.Button(subFrame,
                                      text = "Previous Page",
                                      command = lambda : master.switch_frame(StartEndPage.StartPage))
        btn_to_startpage.grid(row = 2, column = 0)

        btn_to_trial = ttk.Button(subFrame,
                                  text="Next Page",
                                  command=lambda: master.switch_frame(PracticeTrial))
        btn_to_trial.grid(row= 2, column=2)

class PracticeTrial(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        global number_of_practice
        number_of_practice += 1

        subFrame = tk.Frame(master=self)
        subFrame.pack()

        lbl = tk.Label(subFrame,
                       text = f"Pratice Trial {number_of_practice}",
                       font= tkFont.Font(size=25))
        lbl.grid(row = 0, column = 1)

        btn_to_PracticeIntro = ttk.Button(subFrame,
                                          text="Previous Page",
                                          command=lambda: master.switch_frame(PracticeIntro))
        btn_to_PracticeIntro.grid(row=2, column=0)

        btn_to_trial = ttk.Button(subFrame,
                                  text="Confirm",
                                  command=lambda: master.switch_frame(Trial.TrialCue))
        btn_to_trial.grid(row=2, column=2)


