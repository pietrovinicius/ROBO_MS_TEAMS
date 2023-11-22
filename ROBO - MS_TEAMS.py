#05/10/2023
#@PLima
# ROBO - MICROSOFT TEAMS
import pyautogui as py
import datetime
import time
import re
import os

#para sair da automacao colocando o mouse no topo a esquerda da janela
py.FAILSAFE = True
varia = True
chave = True
contador = 0

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
        
    

contador_ultimo = 0
#abrindo log.txt para leitura
with open("log.txt" , "r") as log:
    print("Abrindo log.txt para leitura;")
    for linha in log:
        #print(linha)
        contador_ultimo = linha
    contador_ultimo = contador_ultimo.split()
    contador_ultimo = contador_ultimo[-1]
    contador_ultimo = re.sub(r"\D","",contador_ultimo)
    contador = int(contador_ultimo)
    print(f"Contador com o sub: {contador_ultimo}\nContador atual: {contador}")
    print(type(contador))

try:              
    print("============================== inicio ========================")
    if not os.path.exists("log.txt"):
            with open("log.txt" , "a") as log:
                log.write("")
                        
    with open("log.txt" , "a", encoding="utf-8-sig")  as log:
        #log.write(f"\nAgora: {str(agora)}")           
        print("Agora: " , str(agora()))            
        py.alert(title="==== Início ====" , text="Robo Inicializado: " + str(agora()) , timeout=5000) 
        pausa(1)
        print("hotkey win")
        py.hotkey("win")
        pausa(1)
        print("Escrevendo teams")
        py.write("teams")
        pausa(1)
        print("Apertando enter;")
        py.hotkey("enter")

        try:    
            while chave:
                #tempo para clicar nas 2 opções:
                pausa(30)
                if varia:
                    contador = contador + 1
                    print(f"183,166 - {agora()}:  {str(contador)}x")
                    log.write(f"\n{agora()}: {str(contador)}x")        
                    py.click(183,166, duration=1)
                    varia=False
                elif (varia==False):
                    contador = contador + 1
                    print(f"183,166 - {agora()}:  {str(contador)}x")  
                    log.write(f"\n{agora()}: {str(contador)}x")                       
                    #py.click(223,174 , duration=1)
                    py.click(183,166, duration=1) 
                    varia=True
        except KeyboardInterrupt:            
            print("Interrompido pelo ctrl + c!!!")            
            print(f"log.close() - {agora()}:  {str(contador)}x\n==================================== FIM ====================================")
            error = str("{agora()}\nError: {erro}")
            #logi("Interrompido pelo ctrl + c!!!")
        except Exception as erro:
            log.close()
            print(f"log.close() {agora()}\nErro: {erro=}, {type(erro)=}")  
            error = str("{agora()}\nError: {erro}")
            #logi(error)                
    log.close()
except Exception as erro:
    print(f"\n{agora()}\nError: {erro}")  
    error = str("{agora()}\nError: {erro}")
    #logi(error)