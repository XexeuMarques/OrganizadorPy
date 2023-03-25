import os
import shutil
from tkinter import filedialog
from tkinter import *
from colorama import init, Fore, Style

# Inicializa a biblioteca colorama
init()

# Menssagem de alerta
print(Fore.RED + "🔥 Lembre-se de escolher a pasta correta!!\n o diretorio escolhido poderar ser modificado 🔥\n" + Style.RESET_ALL)

# Cria a interface gráfica para selecionar a pasta a ser organizada
root = Tk()
root.withdraw()
root.update()
path = filedialog.askdirectory(title="Selecione a pasta a ser organizada 📁")
root.destroy()

# Verifica se o usuário selecionou uma pasta
if not path:
    print(Fore.RED + "Você não selecionou uma pasta para organizar 😔." + Style.RESET_ALL)
    exit()

# Defina os diretórios de destino para cada tipo de arquivo.
directories = {
    "Imagens": ["png", "jpg", "jpeg", "img"],
    "SVG": ["svg"],
    "Gif": ["gif"],
    "Documentos e PDFs": ["doc", "docx", "pdf", "txt", "md"],
    "Livros, HQs, Outros": ["cbr", "cbz", "mobi", "epub"],
    "Compactados": ["rar", "arj", "arj", "zip", "tar", "gz", "taz", "tgz"],
    "ISOs": ["iso"],
    "Roms - Super Nitendo": ["sfc", "smc"],
    "Roms - Nitendo 64": ["z64", "n64"],
    "Roms - Nitendo Switch": ["nsp"],
    "Roms - Nitendo WiiU": ["wux"],
    "Áudios e Músicas": ["mp3", "wav", "Ogg"],
    "Vídeos": ["mp4", "avi", "mpeg", "webm", "mov", "mkv"],
    "Programas": ["py", "c", "cpp", "java", "exe"],
    "Aplicativos Android": ["apk"],
    "Outros": [] #Arquivos em nem uma extenção mencionadas a cima e enviado para essa pasta
}

print(Fore.BLUE + "\nMovendo arquivos 🧹\n" + Style.RESET_ALL)
# Percorre todos os arquivos na pasta selecionada
total_files_moved = 0
total_size = 0
for filename in os.listdir(path):
    filepath = os.path.join(path, filename)
    if os.path.isfile(filepath):
        # Obtém a extensão do arquivo
        extension = os.path.splitext(filepath)[1][1:].lower()
        # Move o arquivo para a pasta correspondente
        moved = False
        for directory_name, extensions in directories.items():
            if extension in extensions:
                destination_directory = os.path.join(path, directory_name)
                if not os.path.exists(destination_directory):
                    os.mkdir(destination_directory)
                shutil.move(filepath, destination_directory)
                total_files_moved += 1
                total_size += os.path.getsize(os.path.join(destination_directory, filename))
                moved = True
                break

        # Se não foi possível mover o arquivo, move para a pasta "Outros"
        if not moved:
            destination_directory = os.path.join(path, "Outros")
            if not os.path.exists(destination_directory):
                os.mkdir(destination_directory)
            shutil.move(filepath, destination_directory)

# Imprime um relatório da organização de arquivos
for directory_name, extensions in directories.items():
    destination_directory = os.path.join(path, directory_name)
    if os.path.exists(destination_directory):
        num_files = len([name for name in os.listdir(destination_directory) if os.path.isfile(os.path.join(destination_directory, name))])
        print(Fore.GREEN + f"{num_files} Arquivos foram movidos ou ja estão na pasta -> {directory_name} ✅" + Style.RESET_ALL)
print(Fore.RED + "📁 A pasta modificado! 📁" + Style.RESET_ALL)
print(Fore.BLUE + "\nOrganização de arquivos concluída com sucesso! 😊👌\n" + Style.RESET_ALL)
print(Fore.BLUE + "Total de arquivos movidos 🚀: " + str(total_files_moved) + Style.RESET_ALL)
print(Fore.BLUE + "Tamanho total dos arquivos organizados 💪: " + str(round(total_size / (1024 * 1024), 2)) + " MB" + Style.RESET_ALL)

