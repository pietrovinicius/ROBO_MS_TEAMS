#27/11/2023
#@PLima
#ROBO - MICROSOFT TEAMS
import pyautogui as py
import datetime
import time
import re
import os
import tkinter as tk
import threading

#para sair da automacao colocando o mouse no topo a esquerda da janela
py.FAILSAFE = True
varia = True
chave = True
contador = 0
statusThread = False

def pausa(tempo):
    #print("time de:" , tempo)
    print("Aguarde... " , tempo , "s")
    time.sleep(tempo)
    
def agora():
    agora = datetime.datetime.now()
    agora = agora.strftime("%d/%m/%Y %H:%M:%S")
    return str(agora)

def logi(texto_):
    if not os.path.exists("log.txt"):
            with open("log.txt" , "a" , encoding="utf-8-sig") as log:
                print(f'Log é {os.path.exists("log.txt")}, então será criado na pasta')
                log.write("")
                        
    with open("log.txt" , "a", encoding="utf-8-sig")  as log:
        log.write(f"\n{str(texto_)} - {str(agora())}")    
        
def Executar():
    contador_ultimo = 0
    #abrindo log.txt para leitura
    global statusThread

    try:        
        global varia
        global statusThread   
        print(f"varia: {varia}\nstatusThread: {statusThread}\n")   
        print("============================== Executar() ========================")
        print("Agora: " , str(agora()))            
        #py.alert(title="==== Início ====" , text="Robo Inicializado: " + str(agora()) , timeout=2000) 
        pausa(1)
        print("hotkey win")
        py.hotkey("win")
        pausa(1)
        print("Escrevendo teams")
        py.write("teams")
        pausa(1)
        print("Apertando enter;")
        py.hotkey("enter")
        while chave and statusThread:
            #tempo para clicar nas 2 opções:
            pausa(60)
            if varia and statusThread:
                contador = contador + 1
                print(f"183,166 - {agora()}:  {str(contador)}x")                
                py.click(183,166, duration=1)
                varia=False
            elif (varia==False and statusThread):
                contador = contador + 1
                print(f"183,166 - {agora()}:  {str(contador)}x")                                   
                #py.click(223,174 , duration=1)
                py.click(183,166, duration=1) 
                varia=True
            elif statusThread == False:
                print(f"statusThread: {statusThread}\n")
                #esse break abaixo esta finalizando o looping que prende a thread
                break            
    except Exception as erro:
        print(f"\n{agora()}\nError: {erro}")  
        error = str("{agora()}\nError: {erro}")
        exit()
        
def pausar():
    global statusThread
    statusThread=False
    print(f"global statusThread: {statusThread}")
    print("============================== Pausar() ========================")
        
        
#"============================== inicio ========================"
def interface():
    root = tk.Tk()
    root.maxsize(400,200)
    root.minsize(400,200)
    root.geometry("400x200")
    root.title("ROBO - MICROSOFT TEAMS")
    
    def start():        
        global statusThread
        #criando evento na thread, para ser usado apos ser setado, ser verificado e encerrar a thread
        if statusThread:
            print(f"Thread já foi iniciada, statusThread: \n{statusThread}")
        else:        
            #iniciando thread para usar na funcao Executar()    
            threadExecutar = threading.Thread(target=Executar).start()
            #threadExecutar.start()
            statusThread = True
            print(f"statusThread: {statusThread}\nthreadExecutar.start()\n")    
        
    bt_Iniciar = tk.Button(root, text="Iniciar", command=lambda: [ print("Botao Iniciar") , lb_console.config(text="Robo inicializado!") , start()])
    bt_Iniciar.pack(fill="both", expand=True , padx=10 , pady=10)    

    bt_Sair = tk.Button(root, text="Pausar", command=lambda: [ print("Botao Pausar") , lb_console.config(text="Robo pausado!") , pausar()])
    bt_Sair.pack(fill="both", expand=True , padx=10 , pady=10)
    
    lb_console = tk.Label(root, text="...não inicializado...")
    lb_console.pack(fill="both" , expand=True , pady=10)    
    
    root.mainloop()  
    
if __name__ == "__main__":    
    print("============================== inicio ========================")
    interface()    