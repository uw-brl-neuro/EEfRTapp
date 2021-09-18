import tkinter as tk
from tkinter import ttk
from tkinter import font as tkFont
import TestMenu

# The name of the participant
global participant_name

# Create the welcome page of this EEfRT app. The very first page that pops up when open the app
class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        subFrame = tk.Frame(master = self)
        subFrame.pack()

        lbl = tk.Label(subFrame,
                        text="TEST MODE", font=tkFont.Font(size=(master.get_font_size() - 5)),
                        fg="red")
        lbl.grid(row=0, column=0)

        lbl2 = tk.Label(subFrame,
                       text = "Welcome To EEfRT Experiment!", font = tkFont.Font(size= master.get_font_size()))
        lbl2.grid(row = 1, column = 0)


        # Button to the introductory page of the practice trial session
        btn_to_page1 = ttk.Button(subFrame,
                                  text = "Start",
                                  command = lambda : master.switch_frame(TestMenu.TestMenu))
        btn_to_page1.grid(row = 2, column = 0)


# Create the ending page of this EEfRT app. The very last page of this app. Provides option to
# restarts the experiment, which leads back to the start page
class EndPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        subFrame = tk.Frame(master=self)
        subFrame.pack()

        lbl = tk.Label(subFrame,
                       text="Congratulation, you have completed all of the trails!", font=tkFont.Font(size= master.get_font_size()))
        lbl.grid(row=0, column=0)
        lbl2 = tk.Label(subFrame,
                        text="thank you for participating", font=tkFont.Font(size= (master.get_font_size() - 5)))
        lbl2.grid(row=1, column=0)

        # Button to the start page
        btn_to_restart = ttk.Button(subFrame,
                                    text="Restart",
                                    command=lambda: master.switch_frame(StartPage))
        btn_to_restart.grid(row=2, column=0)
