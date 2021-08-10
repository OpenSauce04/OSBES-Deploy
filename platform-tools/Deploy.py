import os
import subprocess
os.system("adb kill-server > nul")
devices=subprocess.getoutput("adb devices")
print(devices)
input()