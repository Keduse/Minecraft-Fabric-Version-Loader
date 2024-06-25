# author: Keduse
# date: 2024/06/24
import os, shutil

path = "C:\\Users\\"+os.getlogin()+"\\AppData\\Roaming\\.minecraft\\.mods\\"
live = "C:\\Users\\"+os.getlogin()+"\\AppData\\Roaming\\.minecraft\\mods\\"

# If .mods doesn't exist, exit program to remind user to create a backup and folder
if not os.path.exists(path):
	print("Please create a folder named '.mods' within '.minecraft' before running this script.")
	print("Also remember to create backups.")
	input("You may close the window or press enter.")
	Sys.exit()

# List versions inside .mods directory
print("Available Minecraft Mod Versions")
print("--------------------------------")
files = os.listdir(path)
i = 0
for f in files:
	i = i + 1
	print(str(i)+": "+f)

# Validate user input and if invalid, loop back to input step
while True:
	ver = input("Select a version: ")

	try:
		intVer=int(ver)
		if intVer > 0 and intVer <= i:
			break
		else:
			print("Try again, but a number 1-"+str(i))
	except ValueError as error:
		print("Try again, but with a number.")

# Remove old mods folder to make room for new
if os.path.exists(live):
    shutil.rmtree(live)

# Find version within mods directory and copy to loading mods
chosenVer = files[int(ver)-1]
shutil.copytree(path+chosenVer, live)

input("Success! You may close this window or press enter.")
