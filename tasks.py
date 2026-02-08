# -*- coding: utf-8 -*-

def add_task(tasks, title):
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "completed": False
    }
    tasks.append(task)
    print("La tarea fue agregada correctamente.")
    print(f"Titulo: {title}")


def list_tasks(tasks):
    if not tasks:
        print("No hay tareas registradas por el momento.")
        print("Agrega una nueva tarea desde el menú.")
        return

    print("Lista de tareas:")
    for task in tasks:
        status = "Tarea Completada" if task["completed"] else "Tarea Pendiente"
        print(f'{task["id"]}. {task["title"]} [{status}]')


def complete_task(tasks, task_id):
    print("Función no disponible por el momento.")
    print("Esta opción se implementará próximamente, mantente atento a las actualizaciones.")


def delete_task(tasks, task_id):
    print("Función no disponible por el momento.")
    print("Esta opción se implementará próximamente, mantente atento a las actualizaciones.")
