# -*- coding: utf-8 -*-

def _next_id(tasks):
    """Genera un ID único aunque se eliminen tareas."""
    max_id = 0
    for t in tasks:
        if isinstance(t, dict):
            tid = t.get("id")
            if isinstance(tid, int) and tid > max_id:
                max_id = tid
    return max_id + 1


def validar_task_id(task_id):
    """
    Valida que el task_id:
    - Sea un número entero
    - Sea mayor a 0
    - No rompa el programa si es inválido
    """
    try:
        task_id = int(task_id)
    except (TypeError, ValueError):
        print("❌ Error: El ID debe ser un número (no letras ni símbolos).")
        return None

    if task_id <= 0:
        print("❌ Error: El ID debe ser mayor que 0.")
        return None

    return task_id


def add_task(tasks, title):
    # Validar título
    if title is None:
        print("⚠️ El título no puede ser nulo.")
        return False

    title = str(title).strip()
    if not title:
        print("⚠️ El título no puede estar vacío.")
        return False

    # Evitar títulos duplicados (opcional, pero útil)
    for task in tasks:
        if isinstance(task, dict):
            existing_title = str(task.get("title", "")).strip()
            if existing_title.lower() == title.lower():
                print("⚠️ Ya existe una tarea con ese título.")
                return False

    task = {
        "id": _next_id(tasks),
        "title": title,
        "completed": False
    }
    tasks.append(task)
    print("✅ La tarea fue agregada correctamente.")
    print(f"📝 Título: {title}")
    return True


def list_tasks(tasks):
    if not tasks:
        print("📭 No hay tareas registradas por el momento.")
        print("👉 Agrega una nueva tarea desde el menú.")
        return

    print("📋 Lista de tareas:")
    for task in tasks:
        if not isinstance(task, dict):
            print("⚠️ Se encontró una tarea inválida (formato incorrecto).")
            continue

        tid = task.get("id", "?")
        title = task.get("title", "(Sin título)")
        completed = bool(task.get("completed", False))

        status = "✔ Completada" if completed else "✘ Pendiente"
        print(f"{tid}. {title} [{status}]")


def complete_task(tasks, task_id):
    task_id = validar_task_id(task_id)
    if task_id is None:
        return False  # No rompe el menú

    for task in tasks:
        if isinstance(task, dict) and task.get("id") == task_id:
            if task.get("completed") is True:
                print("ℹ️ La tarea ya estaba completada.")
                return True

            task["completed"] = True
            print("✅ Tarea marcada como completada.")
            return True

    print("❌ Error: No se encontró una tarea con ese ID.")
    return False


def delete_task(tasks, task_id):
    task_id = validar_task_id(task_id)
    if task_id is None:
        return False  # No rompe el menú

    for i, task in enumerate(tasks):
        if isinstance(task, dict) and task.get("id") == task_id:
            tasks.pop(i)
            print("🗑️ Tarea eliminada correctamente.")
            return True

    print("❌ Error: No se encontró una tarea con ese ID.")
    return False
