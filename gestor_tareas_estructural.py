# Lista global para almacenar las tareas
tareas = []

# Función para agregar tarea
def agregar_tarea():
    tarea = input("Ingrese una nueva tarea: ")
    tareas.append(tarea)
    print("✅ Tarea agregada con éxito.")

# Función para mostrar todas las tareas
def mostrar_tareas():
    if len(tareas) == 0:
        print("📭 No hay tareas registradas.")
    else:
        print("\n📌 Lista de Tareas:")
        for i, tarea in enumerate(tareas, 1):
            print(f"{i}. {tarea}")

# Función para eliminar una tarea
def eliminar_tarea():
    mostrar_tareas()
    if len(tareas) > 0:
        num = int(input("Ingrese el número de la tarea a eliminar: "))
        if 1 <= num <= len(tareas):
            tarea_eliminada = tareas.pop(num - 1)
            print(f"🗑️ Tarea '{tarea_eliminada}' eliminada.")
        else:
            print("❌ Número inválido.")

# Menú principal
def menu():
    while True:
        print("\n--- GESTOR DE TAREAS (Estructurado) ---")
        print("1. Agregar tarea")
        print("2. Mostrar tareas")
        print("3. Eliminar tarea")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            mostrar_tareas()
        elif opcion == "3":
            eliminar_tarea()
        elif opcion == "4":
            print("👋 Saliendo del programa...")
            break
        else:
            print("❌ Opción inválida, intente de nuevo.")

# Ejecución del programa
menu()