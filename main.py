from hugchat import hugchat
from hugchat.login import Login
from env import *
from os import system
from colorama import Fore, Style


sign = Login(email, passwd)
cookies = sign.login()
chatbox = hugchat.ChatBot(cookies)
id = chatbox.new_conversation()
# Switch model 1: (default: meta-llama/Llama-2-70b-chat-hf.)
chatbox.switch_llm(2)

system('cls')
# Menú de opciones con colores y limpieza
while True:
    try:
        print(Fore.LIGHTGREEN_EX + "\nOpciones:" + Style.RESET_ALL)
        print(Fore.LIGHTWHITE_EX + "1. Chat 🔞 " + Style.RESET_ALL)
        print(Fore.LIGHTWHITE_EX + "2. Limpiar 🗑️" + Style.RESET_ALL)
        print(Fore.RED + "3. Salir 💨" + Style.RESET_ALL)

        opcion = int(input(Fore.WHITE + "\nSeleccione una opción: " + Style.RESET_ALL))

        if opcion == 1:
            user_input = input("> ")
            print(f"\n 🗣️' {Fore.LIGHTBLACK_EX} {chatbox.chat(user_input)}  {Style.RESET_ALL} ' ")
        elif opcion == 2:
            system('cls')
            print(Fore.LIGHTGREEN_EX + "!La consola ha sido limpiada! 👌" + Style.RESET_ALL)
        elif opcion == 3:
            break
        else:
            print(Fore.RED + "Opción no válida" + Style.RESET_ALL)
    except:
        continue
