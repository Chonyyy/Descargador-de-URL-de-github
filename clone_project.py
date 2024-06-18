import re
import os
from git import Repo


# Suponiendo que tienes un archivo de texto con los mensajes de Telegram
telegram_messages_file = 'hulk.txt'

# Carpeta donde se clonarán los repositorios
clone_folder = 'zips/hulk'

# Lista para almacenar las URLs encontradas
urls = []

with open(telegram_messages_file, 'r', encoding='utf-8') as file:
    for line in file:
        # Usar una expresión regular para encontrar URLs de GitHub
        # Esta es una expresión regular básica que busca URLs que comiencen con https://github.com
        found_urls = re.findall(r'https?://github\.com/[^\s]+', line)
        if found_urls:
            urls.extend(found_urls)

# Mostrar las URLs encontradas
print("URLs encontradas en los mensajes de Telegram:")
for url in urls:
    print(url)

print("Terminado de encontrar URLs")

print("Clonando...")

# Función para clonar un repositorio de GitHub
def clone_repo(repo_url, clone_path):
    try:
        Repo.clone_from(repo_url, clone_path)
        print(f'Repositorio clonado desde {repo_url} a {clone_path}')
    except Exception as e:
        print(f'Error al clonar {repo_url}: {str(e)}')

# Verificar y crear la carpeta de clonado si no existe
if not os.path.exists(clone_folder):
    os.makedirs(clone_folder)

# Función para agregar .git al final de la URL si no está presente
def add_git_extension(url):
    if not url.endswith('.git'):
        return url + '.git'
    else:
        return url

# Iterar sobre las URLs y clonar los repositorios
for url in urls:
    # Verificar y corregir la URL si es necesario
    repo_url = add_git_extension(url.strip())

    # Obtener el nombre del repositorio
    repo_name = os.path.basename(repo_url.rstrip('.git'))

    # Construir la ruta de clonado
    clone_path = os.path.join(clone_folder, repo_name)

    if os.path.exists(clone_path) and os.path.isdir(clone_path):
        continue
    
    # Clonar el repositorio
    clone_repo(repo_url, clone_path)

print('Proceso completado.')
