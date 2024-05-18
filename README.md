# Desafio Yuhu: Sistema de Gestión de Tareas con Django y PostgreSQL

El objetivo de este desafío es evaluar las habilidades del candidato en el desarrollo
de aplicaciones backend utilizando el framework Django en Python y una base de
datos PostgreSQL. Debes crear un sistema de gestión de tareas que permita a los
usuarios realizar las siguientes operaciones:
1. Crear una nueva tarea con un título, un email y una descripción.
2. Leer la lista de tareas existentes.
3. Actualizar una tarea existente (modificar el título o la descripción).
4. Eliminar una tarea existente.
Requisitos:
1. Utilizar el framework Django para crear la aplicación web.
2. Utilizar una base de datos PostgreSQL para almacenar las tareas.
3. Implementar vistas y modelos de Django para cada una de las operaciones
mencionadas anteriormente.
4. La aplicación debe manejar solicitudes HTTP GET, POST, PUT y DELETE.
5. Debe proporcionar una interfaz de usuario simple (puede ser una página
HTML, no se evaluará diseño).
6. El código debe estar bien estructurado y seguir las mejores prácticas de
desarrollo en Django.
API Pública
Además de la interfaz de usuario, la aplicación debe proporcionar un API público
que permita a los desarrolladores interactuar con el sistema de gestión de tareas
utilizando solicitudes HTTP.
Especificar los siguientes endpoints en el API:
```
• GET /api/tasks: Devuelve la lista de tareas existentes.
• POST /api/tasks: Crea una nueva tarea con un título y una descripción.
• PUT /api/tasks/{id}: Actualiza una tarea existente especificada por
su ID.
```

## Dependencias del proyecto:

Se utilizó Django version 5.0.3 junto con python 3.12.0, PostgreSQL en su version 12.19 y Redis como backend para Celery
