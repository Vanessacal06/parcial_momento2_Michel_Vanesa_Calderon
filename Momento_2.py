# =================================================================
# TRABAJO INTEGRADO: ESTUDIANTE 1 Y ESTUDIANTE 2
# =================================================================

# --- MÓDULO DE REGISTRO ---
def registrar_gasto(gastos):
    print("\n--- FORMULARIO DE REGISTRO DE GASTO ---")
    
    # Captura de datos simple
    placa = input("Ingrese la placa del vehiculo: ")
    concepto = input("Ingrese el concepto (Gasolina, Peaje, etc.): ")
    valor = float(input("Ingrese el valor del gasto: "))
    
    #Crear el diccionario con los datos
    nuevo_gasto = {
        "placa": placa,
        "concepto": concepto,
        "valor": valor
    }
    
    #Agregar el diccionario a la lista global
    gastos.append(nuevo_gasto)
    print(">>> Gasto registrado con exito.")


# --- ESTRUCTURA DEL MENÚ ---
def mostrar_menu():
    print("\n========================================")
    print("   SISTEMA DE GESTION - TRANSPORTES S.A.")
    print("========================================")
    print("1. Registrar Gasto de Vehiculo")
    print("2. Ver Resumen de Gastos (Proximamente)")
    print("3. Buscar Gastos por Placa (Proximamente)")
    print("4. Salir")
    print("========================================")


def main():
    #lista vacia para los gastos
    gastos = [] 
    
    # Bucle while para mantener el programa activo
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion (1-4): ")

        if opcion == "1":
            # Conexión entre Estudiante 1 y Estudiante 2
            registrar_gasto(gastos)
            
        elif opcion == "2":
            print("\n[Aviso] El modulo de calculos sera desarrollado por el Estudiante 3.")
            
        elif opcion == "3":
            print("\n[Aviso] El modulo de busqueda sera desarrollado por el Estudiante 4.")
            
        elif opcion == "4":
            print("Cerrando el sistema... ¡Hasta luego!")
            break # Rompe el bucle y termina el programa
            
        else:
            print("Opcion no valida. Por favor, intente de nuevo.")



if __name__ == "__main__":
    main()