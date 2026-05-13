# --- ESTRUCTURA PRINCIPAL (Estudiante 1) ---

def mostrar_menu():
    print("\n========== GESTOR DE GASTOS ==========")
    print("1. Registrar Gasto")
    print("2. Ver Total Gastado")
    print("3. Buscar Gastos por Placa")
    print("4. Salir")
    print("======================================")

def main():
    # Lista vacía de gastos
    gastos = [] 
    
    # Menú interactivo (while loop)
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("---  Registro ---")  
        elif opcion == "2":
            print("---  Calculando Total de Gastos ---.")
        elif opcion == "3":
            print("---  Buscando Gastos por Placa ---")
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main()