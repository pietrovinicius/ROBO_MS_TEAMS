#27/11/2023
#@PLima
#setup para criacao de exe do ROBO - MICROSOFT TEAMS

import sys
from cx_Freeze import setup, Executable

#Robo Teams:
#ClickF5:
build_exe_options = {"packages": ["os"], "includes": ["pyautogui" , "datetime" , "time" , "os" , "tkinter" , "threading"]}


# GUI applications require a different base on Windows (the default is for
#a console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"
    
    
#ROBO TEAMS:

#setup(
#    name = "#ROBO - MICROSOFT TEAMS",
#    version = "0.1",
#    description = "Robo para que o Microsoft Teams não entre em modo ausente.",
#    options = {"build_exe": build_exe_options},
#    executables=[Executable("ROBO_-_MS_TEAMS.py", base=base)]
#)

#ROBO Click F5:
setup(
    name = "Click F5",
    version = "1.4",
    description = "Robo para clicar F5 a cada 90s.",
    options = {"build_exe": build_exe_options},
    executables=[Executable("clickF5.py", base=base , icon="clickf5.ico")]
)

#Base64_Reader:
#build_exe_options = {"packages": ["os"], "includes": ["pyautogui" , "datetime" , "time" , "os" , "tkinter" , "threading" , "base64"]}

#ROBO Base64_Reader:
#setup(
#    name = "Base64_Reader",
#    version = "1.0",
#    description = "Robo para Decodificar Base64",
#    options = {"build_exe": build_exe_options},
#    executables=[Executable("Base64_Reader.py", base=base , icon="Base64_Reader.ico")]
#)