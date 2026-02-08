# libraries 
import os 
import time
import shutil

downloads_path = r"c:\Users\telly\Downloads"
resume_folder = r"C:\Users\telly\OneDrive\Desktop\resume"

old_files = set(os.listdir(downloads_path)) # get initial files list

while True: 
    time.sleep (3) # wait
    new_files = set(os.listdir(downloads_path))

    added_files = new_files - old_files

    for file in added_files:


        if "resume" in file.casefold():
            source = os.path.join(downloads_path, file)
            destination = os.path.join(resume_folder, file)
            shutil.move(source, destination)           
    old_files = new_files

    