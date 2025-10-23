def mostrar_filamentos( filamentos_metalicos):
    print("\nFilamentos de metal:")
    for i, filamento in enumerate(filamentos_metalicos, 1):
        print(f"\nFilamento {i}: ", end="")
        for propiedad, valor in filamento.items():
            print(f"{propiedad}: {valor}")
        print()

def agregar_filamento(filamentos_metalicos):
    try:
        metal = input("\nNombre del nuevo filamento: ").strip()
        resistencia_a_la_corrosion = float(input(f"Resistencia a la corrosion de {metal}: "))
        resistencia_a_altas_temperaturas = float(input(f"Resistencia a altas temperaturas de {metal}: "))
        resistencia_al_desgaste = float(input(f"Resistencia al Desgaste/Abrasion de {metal}: "))
        biocompatibilidad = float(input(f"Biocompatibilidad de {metal}: "))
        costo_por_kg = float(input(f"Costo por kg de {metal}: "))
        disponibilidad_en_el_mercado = float(input(f"Disponibilidad en el mercado de {metal}: "))
        costo_de_la_maquinaria = float(input(f"Costo de la maquinaria de {metal}: "))
        costo_de_post_procesado = float(input(f"Costo de post-procesado de {metal}: "))
        resistencia_a_la_tension = float(input(f"Resistencia a la tension (UTS) de {metal}: "))
        densidad = float(input(f"Densidad de {metal}: "))
        procesabilidad_de_impresion_3D = float(input(f"Procesabilidad de impresion 3D de {metal}: "))
        dureza = float(input(f"Dureza de {metal}: "))
        
        nuevo_filamento = {
            "metal": metal,
            "resistencia_a_la_corrosion": resistencia_a_la_corrosion,
            "resistencia_a_altas_temperaturas": resistencia_a_altas_temperaturas,
            "resistencia_al_desgaste": resistencia_al_desgaste,
            "biocompatibilidad": biocompatibilidad,
            "costo_por_kg": costo_por_kg,
            "disponibilidad_en_el_mercado": disponibilidad_en_el_mercado,
            "costo_de_la_maquinaria": costo_de_la_maquinaria,
            "costo_de_post_procesado": costo_de_post_procesado,
            "resistencia_a_la_tension": resistencia_a_la_tension,
            "densidad": densidad,
            "procesabilidad_de_impresion_3D": procesabilidad_de_impresion_3D,
            "dureza": dureza
        }

        filamentos_metalicos.append(nuevo_filamento)

        print(f"\nFilamento '{metal}' añadido con éxito.")
    except ValueError:
        print("Error: Por favor, ingresa el tipo de dato correcto.")
