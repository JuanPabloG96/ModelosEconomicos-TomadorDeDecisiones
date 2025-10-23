import matplotlib.pyplot as plt
from datetime import datetime

def huella_ecologica():
    # Factores de equivalencia
    EF_ENERGIA = 0.2
    EF_AGUA = 0.0001
    WF_RESIDUOS = 0.05
    CF_CO2 = 0.01
    
    # Materiales disponibles
    MATERIALES = [
        "Acero Inoxidable 316L",
        "Acero Inoxidable 17-4 PH",
        "Acero para Herramientas H13",
        "Aluminio AlSi10Mg",
        "Titanio 64 (Ti6Al4V)",
        "Inconel 718",
        "Cromo-Cobalto"
    ]
    
    # Listas para almacenar historial
    historial_labels = []
    historial_huellas = []
    historial_materiales = []
    
    print("CÁLCULO DE HUELLA ECOLÓGICA - IMPRESIÓN 3D METÁLICA")
    print("\nFactores de equivalencia:")
    print(f"  • Energía: {EF_ENERGIA} hectáreas/KWh")
    print(f"  • Agua: {EF_AGUA} hectáreas/litros")
    print(f"  • Residuos sólidos: {WF_RESIDUOS} hectáreas/kg")
    print(f"  • CO₂: {CF_CO2} hectáreas/kg")
    
    while True:
        print("\nMateriales disponibles:")
        for i, material in enumerate(MATERIALES, 1):
            print(f"  {i}. {material}")
        
        while True:
            try:
                opcion = int(input("\nSeleccione el material (1-7): "))
                if 1 <= opcion <= 7:
                    material_seleccionado = MATERIALES[opcion - 1]
                    break
                else:
                    print("❌ Opción inválida. Ingrese un número entre 1 y 7.")
            except ValueError:
                print("❌ Por favor ingrese un número válido.")
        
        # Ingresar datos
        print(f"\nMaterial seleccionado: {material_seleccionado}")
        print("\nIngrese los siguientes datos:")
        
        try:
            energia = float(input("  Energía consumida (KWh): "))
            agua = float(input("  Agua utilizada (litros): "))
            residuos = float(input("  Residuos generados (kg): "))
            co2 = float(input("  Emisiones de CO₂ (kg): "))
        except ValueError:
            print("❌ Error: Todos los valores deben ser numéricos.")
            continue
        
        # Calcular huella ecológica
        huella = (energia * EF_ENERGIA + 
                  agua * EF_AGUA + 
                  residuos * WF_RESIDUOS + 
                  co2 * CF_CO2)
        
        # Mostrar resultado
        print("\nRESULTADO:")
        print(f"  Material: {material_seleccionado}")
        print(f"  Huella ecológica total: {huella:.4f} hectáreas")
        
        # Desglose
        print("\nDesglose por componente:")
        print(f"  • Energía:   {energia * EF_ENERGIA:.4f} ha")
        print(f"  • Agua:      {agua * EF_AGUA:.4f} ha")
        print(f"  • Residuos:  {residuos * WF_RESIDUOS:.4f} ha")
        print(f"  • CO₂:       {co2 * CF_CO2:.4f} ha")
        
        # Guardar en historial
        timestamp = datetime.now().strftime("%H:%M:%S")
        label = f"{material_seleccionado[:15]}\n{timestamp}"
        historial_labels.append(label)
        historial_huellas.append(huella)
        historial_materiales.append(material_seleccionado)
        
        # Preguntar si desea continuar
        continuar = input("\n¿Desea agregar otro cálculo? (s/n): ").lower().strip()
        
        if continuar != 's':
            break
    
    # Mostrar gráfica final
    if historial_huellas:
        # Crear gráfica
        plt.figure(figsize=(12, 6))
        
        barras = plt.bar(range(len(historial_huellas)), historial_huellas, 
                        color="#32a883", edgecolor='black', linewidth=1.5)
        
        plt.xlabel('Cálculos realizados', fontsize=12, fontweight='bold')
        plt.ylabel('Huella Ecológica (hectáreas)', fontsize=12, fontweight='bold')
        plt.title('Comparativa de Huella Ecológica - Impresión 3D Metálica', 
                 fontsize=14, fontweight='bold', pad=20)
        
        plt.xticks(range(len(historial_huellas)), historial_labels, 
                  rotation=45, ha='right', fontsize=9)
        
        # Agregar valores sobre las barras
        for i, (barra, valor) in enumerate(zip(barras, historial_huellas)):
            altura = barra.get_height()
            plt.text(barra.get_x() + barra.get_width()/2., altura,
                    f'{valor:.3f} ha',
                    ha='center', va='bottom', fontsize=9, fontweight='bold')
        
        plt.grid(axis='y', alpha=0.3, linestyle='--')
        plt.tight_layout()
        
        # Mostrar resumen en consola
        print("\n RESUMEN ESTADÍSTICO:")
        print(f"  • Total de cálculos: {len(historial_huellas)}")
        print(f"  • Huella promedio: {sum(historial_huellas)/len(historial_huellas):.4f} ha")
        print(f"  • Huella mínima: {min(historial_huellas):.4f} ha ({historial_materiales[historial_huellas.index(min(historial_huellas))]})")
        print(f"  • Huella máxima: {max(historial_huellas):.4f} ha ({historial_materiales[historial_huellas.index(max(historial_huellas))]})")
        
        plt.show()
        print("\nPrograma finalizado.")
    else:
        print("\nNo se realizaron cálculos.")
