import time
import pyautogui
import datetime
import tkinter as tk
from tkinter import messagebox
import threading

statusThread = False
numero = 90

#"============================== inicio ========================"
def interface():
    root = tk.Tk()
    root.maxsize(360,300)
    root.minsize(360,300)
    root.geometry("360x250")
    root.title("CLICK F5")
    
    global statusThread
    
    global numero
    
    
    def main():
        global numero
        
        print(f"Numero: {numero}")
        try:
            time.sleep(14)
            pyautogui.alert(title="==== Click F5 ====" , text=f"Robo que pressiona o F5" , timeout=1000)
            print(' pyautogui.click(800,800) ')
            time.sleep(1)
            pyautogui.click(800,800)
            lb_console = tk.Label(root, text="... Inicializado ...")
            lb_console.place(x=175,y=255)
            while statusThread:
                # Move o cursor do mouse para o centro da tela 
                # Pressiona a tecla F5
                numero = int(texto_tempo.get("1.0",tk.END).strip())
                pyautogui.press('F5')
                print(f'Espera por {numero} segundos')
                time.sleep(numero)
        except KeyboardInterrupt:
            print("Aplicativo interrompido pelo usuário.")
        except Exception as erro:
            print(f"Error: {erro}") 
            pyautogui.alert(title="==== Erro ====" , text=f"Erro:\n{erro}" , timeout=5000) 
    
    def start():        
        global statusThread
        #criando evento na thread, para ser usado apos ser setado, ser verificado e encerrar a thread
        if statusThread:
            print(f"Thread já foi iniciada, statusThread: \n{statusThread}")
        else:        
            statusThread = True
            print(f"statusThread: {statusThread}\nthreadExecutar.start()\n")
            #iniciando thread para usar na funcao Executar()    
            threadExecutar = threading.Thread(target=main).start()
            
    def fechar_app():
        global statusThread
        # Exiba uma caixa de diálogo de confirmação
        resultado = messagebox.askyesno("Confirmação", "Tem certeza de que deseja fechar o aplicativo?")
        if resultado:
            # Feche o aplicativo
            statusThread = False
            print(f"statusThread: {statusThread}\nthreadExecutar.start()\n")
            root.destroy()
            exit()
            
    imagem = tk.PhotoImage(file="clickF5.png" , height=100 , width=200)
    lb_barra_superior = tk.Label(root, image=imagem)
    lb_barra_superior.place(x=85,y=5)
    
    lb_qnt_tempo = tk.Label(root, text="Tempo estimado: ")
    lb_qnt_tempo.place(x=125,y=115)
    
    texto_tempo = tk.Text(root, height=1, width=2)
    texto_tempo.insert("1.0", "90")
    texto_tempo.place(x=165,y=135)
        
    bt_Iniciar = tk.Button(root, width=12, text="Iniciar", command=lambda: [ print("Botao Iniciar") , start()])
    bt_Iniciar.place(x=65,y=200)

    bt_Sair = tk.Button(root, width=12, text="Fechar", command=lambda: [ print("Botao Fechar") , fechar_app()])
    bt_Sair.place(x=225,y=200)
    
    lb_console = tk.Label(root, text="...")
    lb_console.place(x=175,y=255)
    
    root.mainloop()

if __name__ == "__main__":
    print(' ===================== MAIN()===================== ')
    interface()