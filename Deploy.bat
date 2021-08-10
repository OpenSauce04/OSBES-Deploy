@echo off
set adb="./platform-tools/adb.exe"
%adb% kill-server > nul
%adb% devices > devices.tmp
set /p devices=<devices.tmp
del devices.tmp
cls
echo %devices%
pause