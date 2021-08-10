print("One second...")
import os
import subprocess
os.system("adb kill-server > nul")
os.system("adb start-server > nul")
os.system("cls")
devices=subprocess.getoutput("adb devices")
print(devices)
print("---------------------------------------")
if "device\n" in devices:
  print("Device found!")
else: 
  print("Device not found, please check that ADB is set up correctly on your device")
input()