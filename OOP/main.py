from gestor_tareas import GestorTareas

def menu():
    gestor = GestorTareas()

    while True:
        print("\n--- GESTOR DE TAREAS ---")
        print("1. Agregar tarea")
        print("2. Mostrar tareas")
        print("3. Completar tarea")
        print("4. Eliminar tarea")
        print("0. Salir")

        try:
            opcion = int(input("Elige una opción: "))
        except ValueError:
            print("Por favor ingresa un número válido.")
            continue

        if opcion == 1:
            desc = input("Descripción de la tarea: ")
            gestor.agregar_tarea(desc)
        elif opcion == 2:
            gestor.mostrar_tareas()
        elif opcion == 3:
            try:
                comp = int(input("Número de la tarea a completar: "))
                gestor.completar_tarea(comp)
            except ValueError:
                print("Por favor ingresa un número válido.")
        elif opcion == 4:
            try:
                elim = int(input("Número de la tarea a eliminar: "))
                gestor.eliminar_tarea(elim)
            except ValueError:
                print("Por favor ingresa un número válido.")
        elif opcion == 0:
            print("Saliendo del gestor...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()
