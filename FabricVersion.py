# author: Keduse
# date: 2022/10/04
import os, shutil

path = "C:\\Users\\"+os.getlogin()+"\\AppData\\Roaming\\.minecraft\\.mods\\"
live = "C:\\Users\\"+os.getlogin()+"\\AppData\\Roaming\\.minecraft\\mods\\"

# Remove old mods folder to make room for new
if os.path.exists(live):
    shutil.rmtree(live)

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

# Find version within mods directory and copy to loading mods
chosenVer = files[int(ver)-1]
shutil.copytree(path+chosenVer, live)

input("Success! You may close this window or press enter.")