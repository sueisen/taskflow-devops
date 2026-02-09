import json
import os

FILE_NAME = "tasks.json"


def load_tasks():
    """
    Carga las tareas desde el archivo JSON.
    Si el archivo no existe o está vacío, devuelve una lista vacía.
    NO debe marcar error, solo regresar [].
    """
    # Si el archivo no existe, regresamos lista vacía
    if not os.path.exists(FILE_NAME):
        return []

    try:
        # Abrimos el archivo en modo lectura
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            content = file.read().strip()

            # Si el archivo está vacío, regresamos lista vacía
            if content == "":
                return []

            # Si tiene contenido válido, lo convertimos a lista
            return json.loads(content)

    # Si el JSON está mal formado, evitamos que truene el programa
    except json.JSONDecodeError:
        return []


def save_tasks(tasks):
    """
    Guarda las tareas en el archivo JSON.
    Si el archivo no existe, Python lo crea automáticamente.
    """
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)
