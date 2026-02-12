def add_task(tasks, title):
    try:
        if title is None or str(title).strip() == "":
            print(" Error: El título no puede estar vacío.")
            return

        task = {
            "id": len(tasks) + 1,
            "title": str(title).strip(),
            "completed": False
        }
        tasks.append(task)
        print(" Tarea agregada")

    except Exception as e:
        print(f" Error inesperado al agregar tarea: {e}")
    for task in tasks:
        if task["title"].lower() == title.lower():
            print("Error: ya existe una tarea con ese título")
            return

    task = {
        "id": len(tasks) + 1,
        "title": title,
        "completed": False
    }
    tasks.append(task)
    print(" Tarea agregada")


def list_tasks(tasks):
    try:
        if not tasks:
            print("No hay tareas")
            return

        for task in tasks:
            status = "✓" if task["completed"] else "X"
            print(f'{task["id"]}. {task["title"]} [{status}]')

    except KeyError:
        print(" Error: Una tarea no tiene el formato esperado (faltan claves).")
    except Exception as e:
        print(f" Error inesperado al listar tareas: {e}")


def _parse_task_id(task_id):
    """Convierte el ID a entero (con mensaje claro)."""
    try:
        return int(task_id)
    except ValueError:
        raise ValueError("El ID debe ser un número entero. Ej: 1, 2, 3")


#  FUNCIÓN DE VALIDACIÓN DE ID
def validar_task_id(task_id):
    """
    Valida que el task_id:
    - Sea un número
    - No sea negativo
    - No rompa el programa si es inválido
    """
    try:
        task_id = int(task_id)
    except ValueError:
        print(" Error: El ID debe ser un número (no letras ni símbolos).")
        return None

    if task_id < 0:
        print(" Error: El ID no puede ser negativo.")
        return None

    return task_id


def complete_task(tasks, task_id):
HEAD
    try:
        tid = _parse_task_id(task_id)

        for task in tasks:
            if task["id"] == tid:
                if task["completed"]:
                    print(" La tarea ya estaba completada.")
                else:
                    task["completed"] = True
                    print(" Tarea completada")
                return

        print(f" Error: No existe una tarea con id {tid}")

    except ValueError as e:
        print(f" Error: {e}")
    except KeyError:
        print(" Error: Una tarea no tiene el formato esperado (faltan claves).")
    except Exception as e:
        print(f" Error inesperado al completar tarea: {e}")


def delete_task(tasks, task_id):
    try:
        tid = _parse_task_id(task_id)

        for i, task in enumerate(tasks):
            if task["id"] == tid:
                tasks.pop(i)
                print(" Tarea eliminada")
                return

        print(f" Error: No existe una tarea con id {tid}")

    except ValueError as e:
        print(f" Error: {e}")
    except KeyError:
        print(" Error: Una tarea no tiene el formato esperado (faltan claves).")
    except Exception as e:
        print(f" Error inesperado al eliminar tarea: {e}")
    HEAD
    task_id = validar_task_id(task_id)
    if task_id is None:
        return  # No se rompe el menú
 upstream/main
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            print(" Tarea marcada como completada")
            return

    print(" Error: No se encontró una tarea con ese ID")


def delete_task(tasks, task_id):
    task_id = validar_task_id(task_id)
    if task_id is None:
        return  # No se rompe el menú
    try:
        task_id = int(task_id)
    except:
        print("Error: ID inválido")
        return

    for task in tasks:
        if task["id"] == task_id:
            if task["completed"]:
                print("La tarea ya estaba completada")
                return
            task["completed"] = True
            print("✔ Tarea completada")
            return

    print("Error: tarea no encontrada")



def delete_task(tasks, task_id):
    try:
        task_id = int(task_id)
    except:
        print("Error: ID inválido")
        return

    for task in tasks:
        if task["id"] == task_id:
            confirm = input(f"¿Seguro que deseas eliminar '{task['title']}'? (s/n): ")

            if confirm.lower() != "s":
                print("Eliminación cancelada")
                return
            tasks.remove(task)

            for i, t in enumerate(tasks):
                t["id"] = i + 1

            print("Tarea eliminada")
            return

    print("Error: ID no encontrado")

    print("Error: ID no encontrado")
upstream/main
