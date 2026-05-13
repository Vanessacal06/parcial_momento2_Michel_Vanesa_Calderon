# =================================================================
# PROYECTO: GESTOR DE GASTOS DE VEHÍCULOS
# INTEGRACIÓN: ESTUDIANTE 1 Y ESTUDIANTE 2
# =================================================================

# --- MÓDULO DE REGISTRO (Estudiante 2) ---
def registrar_gasto(gastos):
    print("\n" + "-"*30)
    print("      NUEVO REGISTRO")
    print("-"*30)
    
    # Captura de datos básica
    placa = input("Placa del vehiculo: ")
    concepto = input("Concepto (Gasolina/Peaje/Otros): ")
    
    # Usamos float para permitir decimales en el dinero
    valor = float(input("Valor del gasto: "))
    
    # Se crea el diccionario con los datos capturados
    nuevo_registro = {
        "placa": placa,
        "concepto": concepto,
        "valor": valor
    }


    
    # Se guarda el diccionario en la lista global
    gastos.append(nuevo_registro)
    print("\n>>> Gasto guardado correctamente.")

# --- TRABAJO ESTUDIANTE 3: MÓDULO DE CÁLCULOS ---
def mostrar_total_gastos(gastos):
    total = 0
    print("\n" + "="*30)
    print("   RESUMEN DE GASTOS")
    print("="*30)
    
    # Recorrer la lista de diccionarios
    for gasto in gastos:
        # Sumar el valor de cada diccionario al total
        total = total + gasto["valor"]
        print(f"Vehiculo: {gasto['placa']} | Valor: ${gasto['valor']}")
    
    print("-" * 30)
    print(f"TOTAL ACUMULADO: ${total}")
    print("=" * 30)


# --- MENÚ DE INTERFAZ (Estudiante 1) ---
def mostrar_menu():
    print("\n========================================")
    print("   SISTEMA DE GESTION - TRANSPORTES S.A.")
    print("========================================")
    print("1. Registrar Gasto")
    print("2. Ver Total Gastado")
    print("3. Buscar por Placa (Estudiante 4)")
    print("4. Salir")
    print("========================================")


# --- FUNCIÓN PRINCIPAL ---
def main():
    # Lista donde se almacenarán todos los diccionarios de gastos
    gastos = [] 
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            # Llamamos a la función del Estudiante 2
            registrar_gasto(gastos)
            
        elif opcion == "2":
            # Llamamos a la función del Estudiante 3 y le pasamos la lista de gastos
            mostrar_total_gastos(gastos)
            
        elif opcion == "3":
            print("\n[Aviso] Módulo de búsqueda en desarrollo por Estudiante 4.")
            
        elif opcion == "4":
            print("Saliendo del sistema...")
            break
            
        else:
            print("Opcion no valida, intente de nuevo.")


# Ejecución del programa
if __name__ == "__main__":
    main()