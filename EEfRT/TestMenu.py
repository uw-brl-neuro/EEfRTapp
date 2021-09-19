import tkinter as tk
from tkinter import ttk
from tkinter import font as tkFont
import Trial
import TestAutotest

# keep track of how many practice trials have passed
global number_of_entry

# Create the introductory page to the practice trial session
class TestMenu(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        subFrame = tk.Frame(master=self)
        subFrame.pack()

        lbl = tk.Label(subFrame,
                       text="TEST MODE", font=tkFont.Font(size=(master.get_font_size() - 5)),
                       fg="red")

        lbl.grid(row=0, column=0)

        # Collect data from the trial at this phase
        Trial.start_collect = True

        global number_of_entry
        number_entry = tk.Entry(subFrame)
        number_entry.grid(row=3, column=0)

        lbl2 = tk.Label(subFrame,
                       text=f"Test Menu",
                       font=tkFont.Font(size=master.get_font_size()))
        lbl2.grid(row=1, column=0)

        lbl3 = tk.Label(subFrame,
                        text=f"How many auto test do you want to run?",
                        font=tkFont.Font(size=master.get_font_size() - 5))
        lbl3.grid(row=2, column=0)

        btn_to_page1 = ttk.Button(subFrame,
                                  text="Confirm",
                                  command=lambda: self.autotest(master, number_entry))
        btn_to_page1.grid(row=4, column=0)


    def autotest(self, master, entry):
        global number_of_entry
        number_of_entry = int(entry.get())
        self.after(0, lambda: master.switch_frame(TestAutotest.Autotest))











