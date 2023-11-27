#27/11/2023
#@PLima
#ROBO - MICROSOFT TEAMS
import pyautogui as py
import datetime
import time
import tkinter as tk
import threading

#para sair da automacao colocando o mouse no topo a esquerda da janela
py.FAILSAFE = True
varia = True
chave = True
contador = 0
statusThread = False
um_segundo = 1

def pausa(tempo):
    #print("time de:" , tempo)
    print("Aguarde... " , tempo , "s")
    time.sleep(tempo)
    
def agora():
    agora = datetime.datetime.now()
    agora = agora.strftime("%d/%m/%Y %H:%M:%S")
    return str(agora)
        
def Executar():
    contador_ultimo = 0
    #abrindo log.txt para leitura
    global statusThread
    global um_segundo

    try:        
        global varia
        global statusThread   
        print(f"varia: {varia}\nstatusThread: {statusThread}\n")
        #py.alert(title="global varia - global statusThread" , text=f"varia: {varia}\nstatusThread: {statusThread}\n", timeout=2000)  
        print("============================== Executar() ========================")
        print("Agora: " , str(agora()))
        #py.alert(title="Agora" , text=f"agora: {str(agora())}", timeout=5000)             
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
            um_segundo = 90
            pausa(um_segundo)
            if varia and statusThread:
                print(f"183,166 - {agora()}")                
                py.click(183,166, duration=1)
                #py.alert(title="==== Py Click() ====" , text=f"py.click(183,166, duration=1) varia:{varia} {str(agora())}" , timeout=2000) 
                varia=False
            elif (varia==False and statusThread):
                print(f"183,166 - {agora()}")                                   
                #py.click(223,174 , duration=1)
                py.click(183,166, duration=1) 
                #py.alert(title="==== Py Click() ====" , text=f"py.click(183,166, duration=1) varia:{varia} {str(agora())}" , timeout=2000) 
                varia=True
            elif statusThread == False:
                print(f"statusThread: {statusThread}\n")
                #esse break abaixo esta finalizando o looping que prende a thread
                um_segundo = 0.3
                break            
    except Exception as erro:
        print(f"\n{agora()}\nError: {erro}") 
        py.alert(title="==== Exception ====" , text=erro , timeout=2000) 
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