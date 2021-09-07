import random
import tkinter as tk
import time
from tkinter import ttk
from tkinter import font as tkFont
import PracticeIntro
import StartEndPage
import TimedIntro

# Generate a reward based on the range given by the configuration
def reward_generator(master):
    global current_reward
    current_reward = random.uniform(master.get_reward_lowerbound(), master.get_reward_higherbound()).__round__(2)
    return current_reward

# Generate the probability of winning the current trial based on the configuration
def probability_generator(master):
    global probability_to_win
    probability_to_win = random.choice(master.get_probability())
    master.record_data(probability_to_win)
    return probability_to_win

# Store the level of current task, 0 is easy, 1 is hard
global task_level

# Store the completeness of current trial, 0 is failed, 1 is success
global complete_status

# Store the winning status of current trial, 0 is lose, 1 is win
global winning_status

# Store the start time of current trial, using time.time() format
global start_time

# Store the status of data collection phase, False is don't collect, True is collect
global start_collect

# Store the number of current trial
global trial_number

# Create a page for the cue of next trial with a single "+" sign in the middle of the screen
class TrialCue(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        subFrame = tk.Frame(master=self)
        subFrame.pack()

        # Increase the trial number by 1
        global trial_number
        trial_number += 1

        master.new_data()
        master.record_data(trial_number)

        # Record the current time as time stamp
        import time
        ts = time.time()
        import datetime
        master.record_data(datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))

        lbl = tk.Label(subFrame,
                       text= " + ",
                       font=tkFont.Font(size=50, weight = "bold"))
        lbl.grid(row=0, column=0)

        self.after(500, lambda: master.switch_frame(TrialChoose))

# Creat a page for the participant to choose easy or hard trial
# If idle for certain amount of time, it will automatically choose one option
class TrialChoose(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        subFrame = tk.Frame(master=self)
        subFrame.pack()

        lbl = tk.Label(subFrame,
                       text="Choose Your Task",
                       font=tkFont.Font(size=25))
        lbl.grid(row=0, column=1)
        lbl2 = tk.Label(subFrame,
                        text=f"probability of win: {probability_generator(master)}%", font=tkFont.Font(size=15))

        lbl2.grid(row=1, column=1)

        s = ttk.Style()
        s.configure('my.TButton', font=(15))
        btn_to_EasyTask = ttk.Button(subFrame,
                                     text= "Easy Task \n $1.00 ", style = 'my.TButton',
                                     command=lambda: self.swtich_to_EasyTask(master))
        btn_to_EasyTask.grid(row=2, column=0)

        btn_to_HardTask = ttk.Button(subFrame,
                                     text=f"Hard Task \n ${reward_generator(master)} ", style='my.TButton',
                                     command=lambda: self.swtich_to_HardTask(master))
        btn_to_HardTask.grid(row=2, column=2)

        master.set_frame_switch_status(False)
        # Automatically choose a level for participant since no decision has been made within time limit
        self.after(4500, lambda: self.switch_to_Task(master))

    # Automatically choose a task level
    def switch_to_Task(self, master):
        if master.get_frame_swtich_status() is False:
            global task_level
            task_level = random.randint(0, 1)
            master.record_data(task_level)
            self.after(0, lambda: master.switch_frame(Task))

    # Switch to easy task
    def swtich_to_EasyTask(self, master):
        global task_level
        task_level = 0
        master.set_frame_switch_status(True)
        master.record_data(task_level)
        self.after(0, lambda: master.switch_frame(Task))

    # Switch to hard task
    def swtich_to_HardTask(self, master):
        global task_level
        task_level = 1
        master.set_frame_switch_status(True)
        master.record_data(task_level)
        self.after(0, lambda: master.switch_frame(Task))

# Create the page for the task with a progress bar
class Task(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        global task_level
        global current_reward

        # Decide the reward and progress bar level based on the difficulty of the trial
        if task_level == 0:
            current_reward = 1
            maximum_level = 30
            time_limit = master.get_easy_time_limit() * 1000 - 500
        else:
            maximum_level = 100
            time_limit = master.get_hard_time_limit() * 1000 - 500

        # Record the reward level of this trial
        master.record_data(current_reward)

        global indicator
        indicator = tk.IntVar(value = 0)

        subFrame = tk.Frame(master=self)
        subFrame.pack()

        progress = ttk.Progressbar(subFrame,
                                   orient = tk.VERTICAL, length = 500, maximum = maximum_level + 1,
                                   mode = 'determinate',
                                   variable = indicator)
        progress.grid(row = 0, column = 0)


        def progress_increase(event):
            if indicator.get() == maximum_level:
                global complete_status
                complete_status = True
                self.after(0, lambda: master.switch_frame(CompleteStatusPage))
                master.unbind("<KeyRelease-space>", increase_progress)
            else:
                progress.step(1)

        # Use space bar to increase progress. Make sure the button is pressed instead of just hold
        global increase_progress
        increase_progress = master.bind("<KeyRelease-space>", progress_increase)

        # If the participants spend more time than the limit allowed, switch to failed page
        master.set_frame_switch_status(False)
        self.after(time_limit, lambda: self.switch_to_FailPage(master))

    # Swtich to failed page
    def switch_to_FailPage(self, master):
        if master.get_frame_swtich_status() is False:
            global complete_status
            complete_status = False
            self.after(0, lambda: master.switch_frame(CompleteStatusPage))
            master.unbind("<KeyRelease-space>", increase_progress)

# Create a page that display the completeness status of current trial,
# based on whether the participant finish the task or not
class CompleteStatusPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        subFrame = tk.Frame(master=self)
        subFrame.pack()

        # Record the completeness status of current trial
        master.record_data(complete_status)

        lbl = tk.Label(subFrame,
                       text = f"You {self.status_to_string()} the task!", font = tkFont.Font(size=25))
        lbl.grid(row = 0, column = 0)

        if complete_status is True:
            # Decide whether the participant win this trial based on the given probability
            if random.randint(0, 100) <= probability_to_win:
                global  winning_status
                winning_status = True
            else:
                winning_status = False
        elif complete_status is False:
            winning_status = False

        self.after(1500, lambda: master.switch_frame(WinningStatusPage))

    # Convert the completeness status (False or True) to word (incomplete or complete)
    def status_to_string(self):
        global complete_status
        if complete_status is True:
            status_in_string = "completed"
        else:
            status_in_string = "failed"
        return status_in_string

# Create a page to show the winning status of current trial,
# based on whether or not the participant win this trial
class WinningStatusPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        subFrame = tk.Frame(master=self)
        subFrame.pack()

        # Record the winning status of the current trial
        master.record_data(winning_status)
        # Merge the information of this trial to the collection of data of this timed trial session
        master.data_merge()

        global status_in_string
        status_in_string = tk.StringVar()

        lbl = tk.Label(subFrame,
                       text= f"{self.status_to_string()}", font=tkFont.Font(size=25))
        lbl.grid(row=0, column=0)

        # Decide the next page to display based on the phase (practice session/timed trial session/ending)
        # of the experiment
        if PracticeIntro.number_of_practice < master.get_maximum_practice():
            self.after(1500, lambda: master.switch_frame(PracticeIntro.PracticeTrial))
        elif PracticeIntro.number_of_practice == master.get_maximum_practice() and trial_number <= 0:
            self.after(1500, lambda: master.switch_frame(TimedIntro.TimedTrialIntro))
        elif master.get_current_time() - start_time > master.get_maximum_time():
            self.after(1500, lambda: master.switch_frame(StartEndPage.EndPage))
        else:
            self.after(1500, lambda: master.switch_frame(TrialCue))

    # Convert the winning status (False or True) to word (did not win or win(with reward amount))
    def status_to_string(self):
        global status_in_string
        if winning_status is True:
            status_in_string = f"You won ${current_reward}!"
        else:
            status_in_string = "You did not win this trial"
        return status_in_string










