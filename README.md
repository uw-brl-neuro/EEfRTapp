# EEfRTapp

User Guide
---
Follow the procedures to start the program:

1. Download the code from the "code" button on the top right 
2. Open the folder that you just downloaded
3. Open the EEfRT folder   
4. Copy the complete *file path* of the EEfRTapp.py file
5. Open the command prompt (windows) or terminal (mac)
6. Type the command: ``python`` and paste the file path that you copied 
7. You command now should look like ``python EEfRT-file-path``, hit the enter/return key

Now you should see the window of the app pops up. If you receive an errors, it is most likely due 
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
Comments are added to each class, function, and global variables. If you have any specific
question, please contact: davin05@uw.edu. 


