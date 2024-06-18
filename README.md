# Descripción General

El script está diseñado para buscar URLs de repositorios de GitHub en un archivo de texto (`nombre_archivo.txt`), descargar archivos ZIP de estos repositorios y guardarlos en una carpeta específica (`zips/nombre_carpeta`). Utiliza expresiones regulares para identificar las URLs válidas y la biblioteca `requests` para gestionar las descargas desde GitHub.

## Funcionalidad

1. **Extracción de URLs de GitHub:**
   - Lee el archivo `nombre_archivo.txt` línea por línea y utiliza una expresión regular para identificar URLs que comiencen con `https://github.com`.
   - Almacena las URLs encontradas en una lista `urls`.

2. **Descarga de Archivos ZIP:**
   - Define la función `download_zip(repo_url, download_path)` para cada URL encontrada:
     - Construye la URL del archivo ZIP utilizando la estructura estándar de GitHub.
     - Utiliza `requests.get` para descargar el archivo ZIP desde GitHub.
     - Guarda el archivo descargado en la carpeta especificada (`zips/nombre_carpeta`).

3. **Verificación de Existencia y Descarga:**
   - Verifica si la carpeta de destino (`zips/nombre_carpeta`) existe. Si no existe, la crea.
   - Itera sobre las URLs extraídas y descarga los archivos ZIP solo si aún no existen en la carpeta de destino.

4. **Manejo de Errores:**
   - Captura excepciones durante la descarga y muestra mensajes de error específicos si no se puede completar una descarga correctamente.

## Archivos Generados

- **`nombre_archivo.txt`:** Contiene los mensajes de Telegram donde se buscan las URLs de GitHub.
- **`zips/nombre_carpeta`:** Carpeta donde se guardan los archivos ZIP descargados desde GitHub.

## Uso y Ejecución

- Asegúrate de tener instaladas las bibliotecas necesarias (`requests`) utilizando `pip install requests`.
- Ejecuta el archivo download_zip para iniciar la búsqueda y descarga de archivos ZIP desde los repositorios de GitHub listados en `nombre_archivo.txt`.
- El script muestra mensajes de progreso y finalización una vez completada la descarga de los archivos ZIP.
