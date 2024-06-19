#27/11/2023
#@PLima
#setup para criacao de exe do ROBO - MICROSOFT TEAMS

import sys
from cx_Freeze import setup, Executable

#Robo Teams:
build_exe_options = {"packages": ["os"], "includes": ["pyautogui" , "datetime" , "time" , "os" , "tkinter" , "threading"]}

# GUI applications require a different base on Windows (the default is for
#a console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"
    
#ROBO TEAMS:
setup(
    name = "#ROBO - MICROSOFT TEAMS",
    version = "1.1",
    description = "Robo para que o Microsoft Teams não entre em modo ausente.",
    options = {"build_exe": build_exe_options},
    executables=[Executable("ROBO_-_MS_TEAMS.py", base=base , icon="ms_teams001.ico")]
)

#OBS: lembre-se de levar o png para a pasta no qual gerou nova versao;