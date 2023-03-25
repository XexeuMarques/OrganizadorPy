import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
from colorama import Fore, Style


# Função que cria a interface gráfica para escolher a pasta
def choose_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        organize_files(folder_selected)


# Função que organiza os arquivos na pasta selecionada
def organize_files(folder):
    print(Fore.YELLOW + "Organizando arquivos na pasta: " + folder + Style.RESET_ALL)
    try:
        # Verifica se as pastas já existem e cria se necessário
        folders = ["Videos", "Imagens", "Documentos", "Audio"]
        for folder_name in folders:
            if not os.path.exists(os.path.join(folder, folder_name)):
                os.makedirs(os.path.join(folder, folder_name))

        # Move os arquivos para suas respectivas pastas
        for file_name in os.listdir(folder):
            if file_name.endswith(('.mp4', '.avi', '.mkv', '.mov')):
                shutil.move(os.path.join(folder, file_name), os.path.join(folder, "Videos"))
            elif file_name.endswith(('.jpg', '.jpeg', '.png', '.gif')):
                shutil.move(os.path.join(folder, file_name), os.path.join(folder, "Imagens"))
            elif file_name.endswith(('.doc', '.docx', '.pdf', '.txt')):
                shutil.move(os.path.join(folder, file_name), os.path.join(folder, "Documentos"))
            elif file_name.endswith(('.mp3', '.wav', '.flac')):
                shutil.move(os.path.join(folder, file_name), os.path.join(folder, "Audio"))

        # Imprime mensagem de sucesso
        print(Fore.GREEN + "Organização de arquivos concluída com sucesso!" + Style.RESET_ALL)
        messagebox.showinfo("Sucesso", "Organização de arquivos concluída com sucesso!")
    except Exception as e:
        # Imprime mensagem de erro
        print(Fore.RED + "Ocorreu um erro durante a organização de arquivos: " + str(e) + Style.RESET_ALL)
        messagebox.showerror("Erro", "Ocorreu um erro durante a organização de arquivos: " + str(e))


# Cria a janela para escolher a pasta
root = tk.Tk()
root.withdraw()
folder_selected = filedialog.askdirectory()

# Se uma pasta foi selecionada, chama a função para organizar os arquivos
if folder_selected:
    organize_files(folder_selected)
else:
    print(Fore.RED + "Nenhuma pasta selecionada!" + Style.RESET_ALL)
    messagebox.showwarning("Aviso", "Nenhuma pasta selecionada!")

