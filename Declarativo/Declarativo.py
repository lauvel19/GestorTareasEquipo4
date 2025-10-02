# Lista de tareas inicial
tareas = [
    {"id": 1, "titulo": "Estudiar paradigmas de programación", "completada": False},
    {"id": 2, "titulo": "Hacer la actividad didáctica", "completada": False}
]

# Contador para IDs únicos
contador_id = [3]  # Usamos lista para mantener mutabilidad en closures


# Funciones para las operaciones
def agregar(titulo):
    nueva_tarea = {
        "id": contador_id[0],
        "titulo": titulo,
        "completada": False
    }
    contador_id[0] += 1
    tareas.append(nueva_tarea)
    return f'✓ Tarea agregada: "{titulo}"'


def listar():
    if len(tareas) == 0:
        return "No hay tareas registradas."

    # Uso declarativo de map (comprensión de listas)
    return '\n'.join([
        f"{i + 1}. [{'✓' if tarea['completada'] else ' '}] {tarea['titulo']} (ID: {tarea['id']})"
        for i, tarea in enumerate(tareas)
    ])


def eliminar(id_tarea):
    # Buscar la tarea
    tarea_a_eliminar = next((t for t in tareas if t['id'] == id_tarea), None)

    if not tarea_a_eliminar:
        return f"✗ No se encontró tarea con ID: {id_tarea}"

    # Uso declarativo de filter
    tareas[:] = [t for t in tareas if t['id'] != id_tarea]
    return f'✓ Tarea eliminada: "{tarea_a_eliminar["titulo"]}"'


def completar(id_tarea):
    # Buscar la tarea
    tarea_encontrada = next((t for t in tareas if t['id'] == id_tarea), None)

    if not tarea_encontrada:
        return f"✗ No se encontró tarea con ID: {id_tarea}"

    # Uso declarativo de map para transformar el estado
    for tarea in tareas:
        if tarea['id'] == id_tarea:
            tarea['completada'] = not tarea['completada']
            break

    estado = 'desmarcada' if not tarea_encontrada['completada'] else 'completada'
    return f'✓ Tarea "{tarea_encontrada["titulo"]}" {estado}'


def filtrar(solo_completadas=False):
    # Filtrado declarativo
    tareas_filtradas = [
        t for t in tareas
        if (t['completada'] if solo_completadas else not t['completada'])
    ]

    if len(tareas_filtradas) == 0:
        return f"No hay tareas {'completadas' if solo_completadas else 'pendientes'}."

    return '\n'.join([
        f"{i + 1}. {tarea['titulo']} (ID: {tarea['id']})"
        for i, tarea in enumerate(tareas_filtradas)
    ])


# Diccionario de configuración declarativa para las operaciones
operaciones = {
    'agregar': agregar,
    'listar': listar,
    'eliminar': eliminar,
    'completar': completar,
    'filtrar': filtrar
}


# Función declarativa para ejecutar comandos
def ejecutar_comando(comando, *args):
    operacion = operaciones.get(comando)
    return operacion(*args) if operacion else "✗ Comando no reconocido"


# ========== DEMOSTRACIÓN ==========
if __name__ == "__main__":
    print("=== GESTOR DE TAREAS - PARADIGMA DECLARATIVO ===\n")

    print("📋 Listar tareas iniciales:")
    print(ejecutar_comando('listar'))
    print("\n" + "=" * 50 + "\n")

    print("➕ Agregar nueva tarea:")
    print(ejecutar_comando('agregar', 'Preparar presentación de paradigmas'))
    print("\n" + "=" * 50 + "\n")

    print("📋 Listar todas las tareas:")
    print(ejecutar_comando('listar'))
    print("\n" + "=" * 50 + "\n")

    print("✓ Completar una tarea (ID: 1):")
    print(ejecutar_comando('completar', 1))
    print("\n" + "=" * 50 + "\n")

    print("📋 Listar tareas pendientes:")
    print(ejecutar_comando('filtrar', False))
    print("\n" + "=" * 50 + "\n")

    print("🗑️ Eliminar una tarea (ID: 2):")
    print(ejecutar_comando('eliminar', 2))
    print("\n" + "=" * 50 + "\n")

    print("📋 Listar tareas finales:")
    print(ejecutar_comando('listar'))
    print("\n" + "=" * 50 + "\n")