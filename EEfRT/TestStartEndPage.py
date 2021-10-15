import tkinter as tk
from tkinter import ttk
from tkinter import font as tkFont
import TestMenu
from scipy import stats
from scipy.stats import chisquare
from scipy.stats import kstest

# The name of the participant
global participant_name

# collect generated probability data
global probability_data

# collect generated reward data
global reward_data

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

        global probability_data
        probability_data = []
        global reward_data
        reward_data = []


# Create the ending page of this EEfRT app. The very last page of this app. Provides option to
# restarts the experiment, which leads back to the start page
class EndPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        subFrame = tk.Frame(master=self)
        subFrame.pack()

        # observed value for [number 12, number 50, number 88]
        prob_obs = [0, 0, 0]
        for prob in probability_data:
            if prob == 12:
                prob_obs[0] += 1
            elif prob == 50:
                prob_obs[1] += 1
            elif prob == 88:
                prob_obs[2] += 1

        p_value_prob = 1 - chisquare(prob_obs)[1]
        if p_value_prob < 0.25:
            prob_result = 'Pass'
            prob_color = 'green'
        else:
            prob_result = 'Fail'
            prob_color = 'red'

        p_value_reward = 1 - kstest(reward_data, 'uniform', args=(1.24, 4.3))[1]
        if p_value_reward < 0.25:
            reward_result = 'Pass'
            reward_color = 'green'
        else:
            reward_result = 'Fail'
            reward_color = 'red'

        lbl = tk.Label(subFrame,
                       text="Test Result", font=tkFont.Font(size= master.get_font_size()))
        lbl.grid(row=0, column=0)
        lbl2 = tk.Label(subFrame,
                        text="The probability of winning each trial is random:", font=tkFont.Font(size= (master.get_font_size() - 5)))
        lbl2.grid(row=1, column=0)
        lbl3 = tk.Label(subFrame,
                        text=f"{prob_result}",
                        font=tkFont.Font(size=(master.get_font_size() - 5)),
                        fg = f"{prob_color}")
        lbl3.grid(row=1, column=2)
        lbl4 = tk.Label(subFrame,
                        text="The distribution of the reward is uniform:",
                        font=tkFont.Font(size=(master.get_font_size() - 5)))
        lbl4.grid(row=2, column=0)
        lbl5 = tk.Label(subFrame,
                        text=f"{reward_result}",
                        font=tkFont.Font(size=(master.get_font_size() - 5)),
                        fg=f"{reward_color}")
        lbl5.grid(row=2, column=2)




        # Button to the start page
        btn_to_restart = ttk.Button(subFrame,
                                    text="Restart",
                                    command=lambda: master.switch_frame(StartPage))
        btn_to_restart.grid(row=3, column=0)









        print(prob_obs)
        print(p_value_prob)
        print(prob_result)
        print(p_value_reward)
        print(reward_result)
