@ECHO OFF
pyinstaller --onefile --collect-all customtkinter -w --add-data "img;img" --add-data "img\aws;img\aws" --add-data "img\aws;img\aws" --add-data "img\ff;img\ff" --add-data "img\mutl;img\mutl"  --add-data "img\ru;img\ru" calibrationBot.py
pause