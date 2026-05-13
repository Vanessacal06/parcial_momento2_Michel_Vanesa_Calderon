# =================================================================
# PROYECTO: GESTOR DE GASTOS DE VEHÍCULOS
# INTEGRACIÓN FINAL CON MANEJO DE ERRORES
# =================================================================

# --- MÓDULO DE REGISTRO (Estudiante 2) ---
def registrar_gasto(gastos):
    print("\n" + "-"*30)
    print("      NUEVO REGISTRO")
    print("-"*30)
    
    # .strip() elimina espacios accidentales al inicio o final
    placa = input("Placa del vehiculo: ").strip().upper()
    concepto = input("Concepto (Gasolina/Peaje/Otros): ").strip().capitalize()
    
    # Manejo de errores para el valor numerico
    try:
        valor_input = input("Valor del gasto: ").strip()
        valor = float(valor_input)
        
        nuevo_registro = {
            "placa": placa,
            "concepto": concepto,
            "valor": valor
        }
        
        gastos.append(nuevo_registro)
        print("\n>>> Gasto guardado correctamente.")
        
    except ValueError:
        print("\nERROR: El valor debe ser un numero (ejemplo: 50000 o 10.5).")
        print("El registro ha sido cancelado por error de formato.")

# --- MÓDULO DE CÁLCULOS (Estudiante 3) ---
def mostrar_total_gastos(gastos):
    if not gastos:
        print("\n[!] No hay gastos registrados todavía.")
        return

    total = 0
    print("\n" + "="*30)
    print("   RESUMEN DE GASTOS")
    print("="*30)
    
    for gasto in gastos:
        total += gasto["valor"]
        print(f"Vehiculo: {gasto['placa']} | Concepto: {gasto['concepto']} | Valor: ${gasto['valor']:,.2f}")
    
    print("-" * 30)
    print(f"TOTAL ACUMULADO: ${total:,.2f}")
    print("=" * 30)

# --- MÓDULO DE BÚSQUEDA (Estudiante 4) ---
def buscar_gasto_por_placa(gastos):
    if not gastos:
        print("\n[!] No hay datos para buscar.")
        return

    print("\n" + "-"*30)
    print("    BUSCAR POR PLACA")
    print("-"*30)
    
    placa_buscada = input("Ingrese la placa a buscar: ").strip().upper()
    encontrado = False
    
    for gasto in gastos:
        if gasto["placa"] == placa_buscada:
            print(f">> Encontrado: {gasto['concepto']} | Valor: ${gasto['valor']:,.2f}")
            encontrado = True
    
    if not encontrado:
        print(f"No se encontraron registros para la placa: {placa_buscada}")

# --- MENÚ DE INTERFAZ (Estudiante 1) ---
def mostrar_menu():
    print("\n========================================")
    print("   SISTEMA DE GESTION - TRANSPORTES S.A.")
    print("========================================")
    print("1. Registrar Gasto")
    print("2. Ver Total Gastado")
    print("3. Buscar por Placa")
    print("4. Salir")
    print("========================================")

# --- FUNCIÓN PRINCIPAL ---
def main():
    gastos = [] 
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            registrar_gasto(gastos)
        elif opcion == "2":
            mostrar_total_gastos(gastos)
        elif opcion == "3":
            buscar_gasto_por_placa(gastos)
        elif opcion == "4":
            print("Cerrando el sistema... ¡Buen viaje!")
            break
        else:
            print("Opcion no valida, por favor elija entre 1 y 4.")

if __name__ == "__main__":
    main()