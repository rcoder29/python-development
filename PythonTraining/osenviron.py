import os

# read a variable from OS environment and print it
print("PATH is", os.environ["PATH"])

# Retrieve current working directory (`cwd`)
cwd = os.getcwd()
print(cwd)

# Change directory
os.chdir("C:\\temp")
cwd = os.getcwd()
print("New Working Directory - ", cwd)

# List all files and directories in current directory
filelist = os.listdir('.')
for file in filelist:
    print(file)
