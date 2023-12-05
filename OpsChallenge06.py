# Import the osi module
import os

# Declare and initialize variables
command1 = "whoami"
command2 = "ip a"
command3 = "lshw -short"

# Execute the first bash command using the os.popen() function
output1 = os.popen(command1).read()
print(output1)

# Execute the second bash command using the os.system() function
os.system(command2)

# Execute the third bash command using the 'subprocess' module
import subprocess
output3 = subprocess.check_output(command3, shell=True)
print(output3.decode("utf-8"))
