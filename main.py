# libraries 
import os 
import time
import shutil

downloads_path = "c:\Users\telly\Downloads"
resume_folder = "C:\Users\telly\OneDrive\Desktop\resume"

old_files = set(os.listdir(downloads_path)) # get initial files list

while True: 
    time.sleep (3) # wait
    new_files = set(os.listdir(downloads_path))

    added_files = new_files - old_files

    