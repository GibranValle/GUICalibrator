pyinstaller --onefile calibrationBot.py --collect-all customtkinter 
set DIR=C:\Users\gibra\Documents\Programming\Python\GUICalibrator
xcopy %DIR%\img %DIR%\dist\img /R /S /Y /Q
pause