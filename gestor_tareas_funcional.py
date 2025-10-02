import json
from typing import List

# ---------- Funciones puras ----------
def agregar_tarea(tareas: List[str], nueva_tarea: str) -> List[str]:
    return tareas + [nueva_tarea]

def eliminar_tarea(tareas: List[str], indice: int) -> List[str]:
    return [t for i, t in enumerate(tareas) if i != indice]

def listar_tareas(tareas: List[str]) -> List[str]:
    return list(map(lambda t: f"- {t}", tareas))

# ---------- Funciones auxiliares (no puras, para I/O) ----------
def guardar_tareas(tareas: List[str], archivo="tareas.json"):
    with open(archivo, "w") as f:
        json.dump(tareas, f)

def cargar_tareas(archivo="tareas.json") -> List[str]:
    try:
        with open(archivo, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# ---------- Programa principal ----------
def main():
    tareas = cargar_tareas()

    while True:
        print("\n--- Gestor de Tareas (Funcional) ---")
        print("1. Agregar tarea")
        print("2. Listar tareas")
        print("3. Eliminar tarea")
        print("4. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            nueva = input("Ingrese la nueva tarea: ").strip()
            if nueva:
                tareas = agregar_tarea(tareas, nueva)
                print("Tarea agregada.")
            else:
                print("No puedes agregar una tarea vacía.")
        elif opcion == "2":
            print("\nTus tareas:")
            if tareas:
                for i, t in enumerate(listar_tareas(tareas)):
                    print(f"{i}. {t}")
            else:
                print("No hay tareas registradas.")
        elif opcion == "3":
            if tareas:
                for i, t in enumerate(tareas):
                    print(f"{i}. {t}")
                try:
                    indice = int(input("Ingrese el número de la tarea a eliminar: "))
                    if 0 <= indice < len(tareas):
                        tareas = eliminar_tarea(tareas, indice)
                        print("Tarea eliminada.")
                    else:
                        print("Índice fuera de rango.")
                except ValueError:
                    print("Entrada inválida, debe ser un número.")
            else:
                print("No hay tareas para eliminar.")
        elif opcion == "4":
            guardar_tareas(tareas)
            print("Saliendo... tus tareas se guardaron en 'tareas.json'")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()