import re
import os
import requests
from urllib.parse import urlparse

telegram_messages_file = 'wallE.txt'

# Carpeta donde se guardarán los archivos ZIP descargados
download_folder = 'zips/wallE'

# Lista para almacenar las URLs encontradas
urls = []

with open(telegram_messages_file, 'r', encoding='utf-8') as file:
    for line in file:
        # Usar una expresión regular para encontrar URLs de GitHub
        # Esta es una expresión regular básica que busca URLs que comiencen con https://github.com
        found_urls = re.findall(r'https?://github\.com/[^\s]+', line)
        if found_urls:
            urls.extend(found_urls)

print("URLs encontradas en los mensajes de Telegram:")
for url in urls:
    print(url)

print("Terminado de encontrar URLs")

print("Descargando...")

# Función para descargar un archivo ZIP desde GitHub
def download_zip(repo_url, download_path):
    try:
        # Construir la URL del archivo ZIP
        zip_url = repo_url.rstrip('/') + '/archive/refs/heads/master.zip'
        
        # Descargar el archivo ZIP
        response = requests.get(zip_url)
        if response.status_code == 200:
            # Guardar el archivo ZIP
            with open(download_path, 'wb') as f:
                f.write(response.content)
            print(f'Archivo ZIP descargado desde {zip_url} y guardado en {download_path}')
        else:
            print(f'Error al descargar {zip_url}: Código de estado {response.status_code}')
    except Exception as e:
        print(f'Error al descargar {repo_url}: {str(e)}')

# Verificar y crear la carpeta de descarga si no existe
if not os.path.exists(download_folder):
    os.makedirs(download_folder)

# Iterar sobre las URLs y descargar los archivos ZIP
for url in urls:
    # Verificar y corregir la URL si es necesario
    repo_url = url.strip()
    
    # Construir el nombre del archivo ZIP basado en el nombre del repositorio
    parsed_url = urlparse(repo_url)
    repo_name = os.path.basename(parsed_url.path).rstrip('.git')
    zip_filename = f'{repo_name}.zip'
    download_path = os.path.join(download_folder, zip_filename)

    if os.path.exists(download_path):
        continue
    
    # Descargar el archivo ZIP
    download_zip(repo_url, download_path)

print('Proceso completado.')
