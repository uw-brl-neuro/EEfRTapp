import tkinter as tk
from tkinter import ttk
from tkinter import font as tkFont
import StartEndPage
import Trial

# keep track of how many practice trials have passed
global number_of_practice

class ExperimentIntro(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        subFrame = tk.Frame(master=self)
        subFrame.pack()

        lbl_title = tk.Label(subFrame,
                             text = "What is EEfRT Experiment?", font= tkFont.Font(size=master.get_font_size()) )
        lbl_title.grid(row = 0, column = 1)

        text_box = tk.Text(subFrame,
                           font= tkFont.Font(size= master.get_font_size()),
                           width = (65 + (2 * (25 - master.get_font_size()))),
                           height = (20 + (0.5 * (25 - master.get_font_size()))))
        text_box.grid(row = 1, column = 1)

        scroll = tk.Scrollbar(subFrame, orient = "vertical", command = text_box.yview)
        scroll.grid(row = 1, column = 2, sticky = "ns")

        text_box.config(yscrollcommand = scroll)
        quote = f"""            The EEfRT task is a multi-trial game in which you, the participants, are given an opportunity on each trial to choose between two different task difficulty levels in order to obtain 'rewards'.
            
            Successful completion of hard-task trials requires you to make {master.get_hard_press_level()} button spacebar presses, using the nondominant little finger within {master.get_hard_time_limit()} seconds, while successful completion of easy-task trials requires you to make {master.get_easy_press_level()} button spacebar presses, using the dominant index finger within {master.get_easy_time_limit()} seconds.
            
            For easy-task trials, you are eligible to win the same amount, $1.00, on each trial if you successfully completed the task. For hard-task choices, you are eligible to win higher amounts that varied per trial within a range of ${master.get_reward_lowerbound()} – ${master.get_reward_upperbound()}.
            
            However, you are not guaranteed to win the reward even if you complete the task; some trials are 'win' trials, in which you received the stated reward, while others are 'no win' trials, in which you received no reward for that trial.
            
            To help you determine which trials are more likely to be win trials, you will be provided with the probability of it being a winning trial at the beginning of each trial. The level of probabilities are 88%, 50%, or 12%.
            
            At the beginning of each trial, you will have a 5-second choice period in which you are presented with information regarding the probability of winning and the reward magnitude of the hard task.
            
            You had {(master.get_maximum_time() / 60).__round__(2)} minutes to play as many trials as you could. Be careful that since hard-task trials take approximately twice as much time to complete as easy-task trials, the number of trials that the you are able to play depended in part on the choices that you made. This meant that making more hard-task trials toward the beginning of the experiment could reduce the total number of trials, which could in turn mean that you did not get a chance to play high- value, high-probability trials that might have appeared towards the end of the playing time.
        """
        text_box.insert(tk.END, quote)
        text_box.config(state = "disabled")

        btn_to_startpage = ttk.Button(subFrame,
                                      text="Previous Page",
                                      command=lambda: master.switch_frame(StartEndPage.StartPage))
        btn_to_startpage.grid(row=2, column=1)

        btn_to_practiceIntro = ttk.Button(subFrame,
                                      text="I understand, Next Page",
                                      command=lambda: master.switch_frame(PracticeIntro))
        btn_to_practiceIntro.grid(row=3, column=1)



# Create the introductory page to the practice trial session
class PracticeIntro(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        subFrame = tk.Frame(master=self)
        subFrame.pack()

        # Do not collect data from the trial at this phase
        Trial.start_collect = False
        # Exclude the number of practice trials from the count of total trials
        Trial.trial_number = 0 - master.get_maximum_practice()

        # Reset the number of practice that has given to the participant to 0
        global number_of_practice
        number_of_practice = 0

        lbl = tk.Label(subFrame,
                       text = f"Before we officially begin, you would play {master.get_maximum_practice()} practice trials",
                       font= tkFont.Font(size=master.get_font_size()))
        lbl.grid(row = 0, column = 1)
        lbl2 = tk.Label(subFrame,
                        text = "[Detailed Explanation To Be Inserted]", font = tkFont.Font(size= (master.get_font_size() - 10)))

        lbl2.grid(row = 1, column = 1)

        # Button to Start Page
        btn_to_startpage = ttk.Button(subFrame,
                                      text = "Previous Page",
                                      command = lambda : master.switch_frame(ExperimentIntro))
        btn_to_startpage.grid(row = 2, column = 0)

        # Button to the practice trial page
        btn_to_trial = ttk.Button(subFrame,
                                  text="Next Page",
                                  command=lambda: master.switch_frame(PracticeTrial))
        btn_to_trial.grid(row= 2, column=2)

# Create an intro page for each practice trial and show the number of current practice trial
class PracticeTrial(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        # Increase the number of practice trials given to the participant by 1
        global number_of_practice
        number_of_practice += 1

        subFrame = tk.Frame(master=self)
        subFrame.pack()

        lbl = tk.Label(subFrame,
                       text = f"Pratice Trial {number_of_practice}",
                       font= tkFont.Font(size= master.get_font_size()))
        lbl.grid(row = 0, column = 1)

        # Button to the introductory page of the practice trial session
        btn_to_PracticeIntro = ttk.Button(subFrame,
                                          text="Restart Practice",
                                          command=lambda: master.switch_frame(PracticeIntro))
        btn_to_PracticeIntro.grid(row=2, column=0)

        # Button to begin this practice trial
        btn_to_trial = ttk.Button(subFrame,
                                  text="Confirm",
                                  command=lambda: master.switch_frame(Trial.TrialCue))
        btn_to_trial.grid(row=2, column=2)



