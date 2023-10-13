#05/10/2023
#@PLima
# ROBO - MICROSOFT TEAMS
import pyautogui as py
import pandas
import datetime
import time
import sys

#para sair da automacao colocando o mouse no topo a esquerda da janela
py.FAILSAFE = False
varia = True
chave = True
contador = 0
def pausa(tempo):
    #print("time de:" , tempo)
    time.sleep(tempo)
        
print("============================== inicio ========================")
agora = datetime.datetime.now()    
print("Agora: " , str(agora))    
agora = agora.strftime("%d/%m/%Y %H:%M:%S")
py.alert(title="==== Início ====" , text="Robo Inicializado: " + str(agora) , timeout=5000) 
pausa(1)
print("hotkey win")
py.hotkey("win")
pausa(1)
print("Escrevendo teams")
py.write("teams")
pausa(1)
print("Apertando enter;")
py.hotkey("enter")
while chave:
    #tempo para clicar nas 2 opções:
    time.sleep(15)
    if varia:
        contador = contador + 1
        print(f"TEAMS ICONE PIETROW(346,254): {contador}x")
        #py.click(346,254 , duration=1)            
        py.click(148,314)
        varia=False
    elif (varia==False):
        contador = contador + 1
        print(f"TEAMS ICONE RECENTE(232,443): {contador}x")     
        #py.click(232,443 , duration=1)
        py.click(223,174 , duration=1) 
        varia=True