def registrar_gasto(gastos):
    print("\n--- Registro de Gasto ---")
    placa = input("Placa del vehículo: ").upper()
    concepto = input("Concepto (Gasolina, Peaje, etc.): ")
    try:
        valor = float(input("Valor del gasto: "))
        # Guardamos como diccionario (Lo que pedía el Estudiante 2)
        nuevo_gasto = {
            "placa": placa,
            "concepto": concepto,
            "valor": valor
        }
        gastos.append(nuevo_gasto)
        print("¡Gasto registrado con éxito!")
    except ValueError:
        print("Error: El valor debe ser un número.")

def mostrar_total(gastos):
    print("\n--- Resumen de Gastos ---")
    if not gastos:
        print("No hay gastos registrados.")
        return
    
    total = 0
    # Ciclo for para sumar (Lo que pedía el Estudiante 3)
    for g in gastos:
        total += g["valor"]
    
    print(f"El Gasto Total acumulado de todos los vehículos es: ${total:,.2f}")

def buscar_por_placa(gastos):
    print("\n--- Búsqueda por Placa ---")
    if not gastos:
        print("No hay datos para buscar.")
        return
        
    placa_buscada = input("Ingrese la placa a consultar: ").upper()
    encontrado = False
    
    print(f"\nResultados para la placa {placa_buscada}:")
    for g in gastos:
        if g["placa"] == placa_buscada:
            print(f"- {g['concepto']}: ${g['valor']:,.2f}")
            encontrado = True
    
    if not encontrado:
        print("No se encontraron gastos para esa placa.")

def main():
    gastos = [] # Lista de diccionarios (Estudiante 1)
    
    while True:
        print("\n===== GESTOR DE COMBUSTIBLE Y GASTOS =====")
        print("1. Registrar Gasto")
        print("2. Ver Total Gastado")
        print("3. Buscar Gastos por Vehículo")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_gasto(gastos)
        elif opcion == "2":
            mostrar_total(gastos)
        elif opcion == "3":
            buscar_por_placa(gastos)
        elif opcion == "4":
            print("Cerrando sistema... ¡Buen viaje!")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    main()