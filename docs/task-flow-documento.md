# Documento del caso: Task-Flow

## 1. Parámetros de configuración de las herramientas utilizadas

### 1.1 Control de versiones (Git + GitHub)
- Repositorio: https://github.com/Andrea-Granados12/manejo-de-excepciones-Marlene
- Ramas usadas:
  - main: versión estable
  - develop: integración
  - feature/*: nuevas funcionalidades / cambios
- Reglas de colaboración:
  - Cambios se integran por Pull Request (PR)
  - Revisión mínima: 1 aprobación (si aplica)
  - Commits con mensajes claros (ej. feat:, fix:, docs:)

### 1.2 Entorno de desarrollo
- Sistema operativo: Windows
- Editor: Visual Studio Code
- Lenguaje: Python 3.x
- Ejecución local:
  - python main.py

### 1.3 Automatización / CI
No se configuró integración continua en este proyecto.
- Plataforma: GitHub Actions
- Workflow: .github/workflows/ci.yml
- Acciones:
  - instalar dependencias
  - ejecutar pruebas
  - (opcional) build/push de Docker

### 1.4 Contenedores
No se utilizó Docker en este proyecto.
- Imagen base: python:3.x-slim
- Comandos:
  - docker build -t task-flow .
  - docker run --rm task-flow

---

## 2. Plan de pruebas

### 2.1 Objetivo
Verificar que Task-Flow funciona correctamente y que valida errores sin romperse.

### 2.2 Alcance
Funciones a probar:
- add_task (agregar)
- list_tasks (listar)
- complete_task (completar)
- delete_task (eliminar)
- validaciones: título vacío, id inválido, id inexistente

### 2.3 Tipos de pruebas
- Pruebas manuales (con entradas del usuario)
- Pruebas unitarias (pytest) (si aplica)
- Pruebas en CI (si aplica)

### 2.4 Criterios de aceptación
- El programa no debe cerrarse ante entradas inválidas
- Debe mostrar mensajes de error claros
- Las tareas deben mantenerse consistentes (IDs / estados)

---

## 3. Casos de prueba

> Formato: ID, descripción, pasos, entrada, resultado esperado

### CP-01 Agregar tarea válida
- Pasos: Ejecutar el programa → Agregar tarea → escribir título
- Entrada: "Estudiar DevOps"
- Resultado esperado: Se agrega la tarea con un ID y estado "pendiente"

### CP-02 Agregar tarea vacía
- Pasos: Agregar tarea → dejar título vacío
- Entrada: ""
- Resultado esperado: Mensaje de error y no se agrega

### CP-03 Listar tareas
- Pasos: Listar tareas
- Entrada: N/A
- Resultado esperado: Se muestran tareas existentes

### CP-04 Completar tarea con ID válido
- Pasos: Completar tarea → escribir ID existente
- Entrada: 1 (ejemplo)
- Resultado esperado: La tarea cambia a completada

### CP-05 Completar tarea con ID inexistente
- Pasos: Completar tarea → escribir ID que no existe
- Entrada: 999
- Resultado esperado: Mensaje de error, no se modifica nada

### CP-06 Eliminar tarea con ID inválido
- Pasos: Eliminar → escribir texto
- Entrada: "abc"
- Resultado esperado: Mensaje de error (manejo de excepción)

---

## 4. Flujo de trabajo para el control de versiones

### 4.1 Estructura de ramas
- main: rama estable
- develop: rama de integración
- feature/*: trabajo individual por cambios

### 4.2 Flujo propuesto
1) Crear rama desde develop:
   - git checkout develop
   - git checkout -b feature/nombre-cambio
2) Commit con mensaje claro:
   - git add .
   - git commit -m "docs: agregar documento del caso task-flow"
3) Push:
   - git push -u origin feature/nombre-cambio
4) Pull Request hacia develop
5) Merge a develop
6) Pull Request de develop hacia main para versión final

---

## 5. Estrategia de despliegue

### 5.1 Tipo
- Manual (local) o CI/CD (si se configura Actions + Docker)

### 5.2 Proceso (manual)
1) Ejecutar pruebas y validar funcionalidad
2) Merge a main
3) Ejecutar:
   - python main.py

### 5.3 Proceso (si hay Docker)
1) Build de imagen:
   - docker build -t task-flow .
2) Ejecutar:
   - docker run --rm task-flow
3) (Opcional) Publicar imagen en Docker Hub:
   - docker tag task-flow usuario/task-flow:latest
   - docker push usuario/task-flow:latest
