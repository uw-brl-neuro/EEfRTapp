import tkinter as tk
from tkinter import ttk
from tkinter import font as tkFont
import PracticeIntro


class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        subFrame = tk.Frame(master = self)
        subFrame.pack()

        PracticeIntro.number_of_practice = 0

        lbl = tk.Label(subFrame,
                       text = "Welcome To EEfRT Experiment!", font = tkFont.Font(size=25))
        lbl.grid(row = 0, column = 0)
        lbl2 = tk.Label(subFrame,
                        text = "thank you for participating", font  = tkFont.Font(size = 20))
        lbl2.grid(row = 1, column = 0)

        btn_to_page1 = ttk.Button(subFrame,
                                  text = "Next Page",
                                  command = lambda : master.switch_frame(PracticeIntro.PracticeIntro))
        btn_to_page1.grid(row = 2, column = 0)

class EndPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        subFrame = tk.Frame(master=self)
        subFrame.pack()

        lbl = tk.Label(subFrame,
                       text="Congratulation, you have completed all of the trails!", font=tkFont.Font(size=25))
        lbl.grid(row=0, column=0)
        lbl2 = tk.Label(subFrame,
                        text="thank you for participating", font=tkFont.Font(size=20))
        lbl2.grid(row=1, column=0)

        btn_to_restart = ttk.Button(subFrame,
                                    text="Restart",
                                    command=lambda: master.switch_frame(StartPage))
        btn_to_restart.grid(row=2, column=0)
