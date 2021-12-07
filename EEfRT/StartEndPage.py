import tkinter as tk
from tkinter import ttk
from tkinter import font as tkFont
import PracticeIntro
import Trial

# The name of the participant
global participant_name

# Create the welcome page of this EEfRT app. The very first page that pops up when open the app
class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        subFrame = tk.Frame(master = self)
        subFrame.pack()

        lbl = tk.Label(subFrame,
                       text = "Welcome To EEfRT Experiment!", font = tkFont.Font(size= master.get_font_size()))
        lbl.grid(row = 0, column = 0)
        lbl2 = tk.Label(subFrame,
                        text = "thank you for participating", font  = tkFont.Font(size = (master.get_font_size() - 5)))
        lbl2.grid(row = 1, column = 0)

        global name_entry
        name_entry = tk.Entry(subFrame)
        name_entry.grid(row = 2, column = 0)

        # Button to the introductory page of the practice trial session
        btn_to_page1 = ttk.Button(subFrame,
                                  text = "Confirm (Enter Key)",
                                  command = lambda : self.confirm_name(master, name_entry))
        btn_to_page1.grid(row = 3, column = 0)

        lbl_empty = tk.Label(subFrame,
                             text = "")
        lbl_empty.grid(row = 4, column = 0)

        lbl_empty2 = tk.Label(subFrame,
                             text="")
        lbl_empty2.grid(row=5, column=0)

        btn_font_size_up = ttk.Button(subFrame, text = "+ (Up Key)",
                                      command = lambda: self.font_size_up(master))
        btn_font_size_up.grid(row = 6, column = 0)

        def font_size_up_up(event):
            master.set_font_size(master.get_font_size() + 1)
            master.switch_frame(StartPage)

        global font_size_up
        font_size_up = master.bind("<Up>", font_size_up_up)

        def font_size_down_down(event):
            master.set_font_size(master.get_font_size() - 1)
            master.switch_frame(StartPage)

        global font_size_down
        font_size_down = master.bind("<Down>", font_size_down_down)


        lbl_font = tk.Label(subFrame,
                       text= f"{self.font_size_display(master)}", font=tkFont.Font(size= (master.get_font_size() - 10)))
        lbl_font.grid(row=7, column=0)
        btn_font_size_down = ttk.Button(subFrame, text="- (Down Key)",
                                        command = lambda: self.font_size_down(master))
        btn_font_size_down.grid(row = 8, column = 0)


        def confirm_name_enter(event):
            global participant_name
            participant_name = name_entry.get()
            master.switch_frame(PracticeIntro.ExperimentIntro)
            master.unbind("<Return>", confirm_enter)
            master.unbind("<Up>", font_size_up)
            master.unbind("<Down>", font_size_down)


        global confirm_enter
        confirm_enter = master.bind("<Return>", confirm_name_enter)

    def font_size_up(self, master):
        master.set_font_size(master.get_font_size() + 1)
        master.switch_frame(StartPage)

    def font_size_down(self, master):
        master.set_font_size(master.get_font_size() - 1)
        master.switch_frame(StartPage)

    def font_size_display(self, master):
        if master.get_font_size() == master.get_original_font_size():
            return f"Font Size Setting: {master.get_font_size()} (Default)"
        else:
            return f"Font Size Setting: {master.get_font_size()}"


    # When confirm button is hit, store the name entered by the participant
    def confirm_name(self, master, entry):
        global participant_name
        participant_name = entry.get()
        master.switch_frame(PracticeIntro.ExperimentIntro)

# Create the ending page of this EEfRT app. The very last page of this app. Provides option to
# restarts the experiment, which leads back to the start page
class EndPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        Trial.start_collect = False

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
                                    text="Restart (Right Key)",
                                    command=lambda: master.switch_frame(StartPage))
        btn_to_restart.grid(row=2, column=0)

        def switch_to_startpage(event):
            master.switch_frame(StartPage)
            master.unbind("<Right>", to_startpage_right)

        global to_startpage_right
        to_startpage_right = master.bind("<Right>", switch_to_startpage)


