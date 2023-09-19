pyinstaller --onefile calibrationBot.py --collect-all customtkinter 
set DIR=E:\Documents\Workspaces\Python\Gui
xcopy %DIR%\img %DIR%\dist\img /R /S /Y /Q
pause