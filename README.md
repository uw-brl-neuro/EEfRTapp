# EEfRTapp

User Guide
---
Download the code from the "code" button on the top right and follow the procedures below to start the program:

1. Open the folder that you just downloaded
3. Open the EEfRT folder   
4. Copy the complete *file path* of the EEfRTapp.py file
5. Open the command prompt (windows) or terminal (mac)
6. Type the command: ``python`` and paste the file path that you copied 
7. You command now should look like ``python EEfRT-file-path``, hit the enter/return key

Now you should see the window of the app pops up. If you receive an error, it is most likely due 
to the python package that you downloaded doesn't come with yaml. To fix this, enter this command: ``pip install pyyaml ``.

The default setting of this app follows [this paper](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2720457/pdf/pone.0006598.pdf) by Treadway. 
However, you have the option to change the setting by following procedures:

1. Open the folder that you downloaded
2. Open the EEfRT folder
3. Open the configuration.yaml file
4. Change the setting to what you want and make sure you save the changes
5. Start/Restart the app program

After the experiment ended, the data collected will automatically be saved to the 
trailResult.csv file in the same EEfRT folder with EEfRTapp.py file, configuration.yaml file, and 
other essential files for the program to run. Each time you open the program and collect new data, 
the new data will be appended to the previously stored data. 

Developer Guide
---
Comments are added to each class, function, and global variables. 

To enter test mode, please click ``Control + T``. This will take you to the test mode, and 
allow you to run a number of auto test trials of your choice. The result of the test trial 
will also be stored in trialResult.csv. Make sure you do not mix the test result with the 
real experimental result. Also, note that for some unknown reason, the amount of time it takes 
to complete the auto tests does not grow linearly with number of test. (e.g: It takes 2 seconds
to finish 50 auto test trials, but 6 seconds to finish 100)

If you have any specific question, please contact: davin05@uw.edu. 


