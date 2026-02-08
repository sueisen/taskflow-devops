def add_task(tasks, title):
    # Manejo básico por si title viene raro
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


def complete_task(tasks, task_id):
    # Debe marcar la tarea como completada sin crashear si el ID está mal
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

        # si no encontró el id
        print(f" Error: No existe una tarea con id {tid}")

    except ValueError as e:
        print(f" Error: {e}")
    except KeyError:
        print(" Error: Una tarea no tiene el formato esperado (faltan claves).")
    except Exception as e:
        print(f" Error inesperado al completar tarea: {e}")


def delete_task(tasks, task_id):
    # Debe eliminar la tarea sin crashear si el ID está mal
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
