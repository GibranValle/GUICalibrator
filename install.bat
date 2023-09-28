@ECHO OFF
SET var=%cd%
pyinstaller --onefile calibrationBot.py --collect-all customtkinter 
set DIR=%var%
xcopy %DIR%\img %DIR%\dist\img /R /S /Y /Q
pause