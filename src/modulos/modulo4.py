from os import system, name
from time import sleep
import tkinter as tk
import customtkinter as ctk

# Constante con todos los criterios disponibles
CRITERIOS_TOTALES = [
    "resistencia a la corrosion",
    "resistencia a altas temperaturas",
    "resistencia al desgaste/abrasion",
    "biocompatibilidad",
    "costo por kg",
    "disponibilidad en el mercado",
    "costo de la maquinaria",
    "costo de post-procesado",
    "resistencia a la tension (uts)",
    "densidad",
    "procesabilidad de impresion 3d",
    "dureza"
]

def clear_screen():
    system('cls' if name == 'nt' else 'clear')

def solicitar_criterios_clave() -> list:
    criterios_clave = []
    
    while len(criterios_clave) < 4:
        clear_screen()
        
        # 1. Mostrar estado de la selección
        num_seleccionado = len(criterios_clave)
        print("MÓDULO 4A: Selección de Indicadores Clave (AHP)")
        print(f"SELECCIONADOS: {num_seleccionado}/4")
        if criterios_clave:
            print(f"Criterios elegidos: {', '.join(c.upper() for c in criterios_clave)}\n")
        else:
            print("\n")
            
        # Mostrar menu de criterios
        print("Selecciona los criterios a agregar:")
        for i, criterio in enumerate(CRITERIOS_TOTALES):
            estado = " [ELEGIDO]" if criterio in criterios_clave else ""
            print(f"{i+1}. {criterio}{estado}")

        num_indicador = num_seleccionado + 1
        try:
            seleccion = input(f"\nIngresa el número de la opción para el Indicador {num_indicador}: ")
            
            # Validación de entrada
            seleccion_idx = int(seleccion) - 1
            if seleccion_idx < 0 or seleccion_idx >= len(CRITERIOS_TOTALES):
                raise ValueError("Opción no válida. Ingresa un número de la lista.")
            
            criterio_seleccionado = CRITERIOS_TOTALES[seleccion_idx]
            
            # Validación de duplicados
            if criterio_seleccionado in criterios_clave:
                print(f"\n❌ El criterio '{criterio_seleccionado.upper()}' ya fue seleccionado.")
                sleep(2)
                continue
            
            # Agregar criterio
            criterios_clave.append(criterio_seleccionado)
            print(f"\n✅ Agregado: {criterio_seleccionado.upper()}")
            sleep(1.5)
            
        except ValueError as e:
            print(f"\n❌ ERROR: {e}")
            sleep(2)

    clear_screen()
    print("--- SELECCIÓN FINALIZADA --- \n")
    return criterios_clave

def generar_conclusion_filamento(material_optimo: str, porcentaje_de_mejora: float):
    criterios_clave = solicitar_criterios_clave()
    
    indicadores_str = ", ".join(criterios_clave)
    
    texto_final = (
        f"La Evaluación AHP de Siete Filamentos** determina que la selección estratégica es el {material_optimo}, "
        f"material que alcanzó un {porcentaje_de_mejora:.2f}% de prioridad en el análisis. "
        f"Este resultado se fundamenta en su desempeño sobresaliente en los criterios clave: {indicadores_str}, "
        f"lo que garantiza el cumplimiento de los requerimientos más críticos para el desarrollo de "
        f"Componentes de Interfaces Humano-Máquina Subacuáticas."
    ) 
    print(texto_final)

def modelo_grand_prix():
    app = ctk.CTk()
    app.geometry("1280x720")
    app.title("Modelo Grand Prix - Índice de Afectación de la Decisión")

    # Apariencia
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    # Frame principal
    main_frame = ctk.CTkScrollableFrame(app)
    main_frame.pack(fill="both", expand=True, padx=40, pady=40)

    # Título principal
    titulo = ctk.CTkLabel(
        main_frame,
        text="Modelo Grand Prix - Índice de Afectación de la Decisión",
        font=("Arial", 22, "bold")
    )
    titulo.grid(row=0, column=0, columnspan=3, pady=(0, 20))

    CRITERIOS = [
        "Confianza en condiciones submarinas",
        "Vida útil del componente en agua salada", 
        "Impacto en el presupuesto del proyecto",
        "Confiabilidad en interfaz humano-máquina",
        "Seguridad del operario en uso submarino"
    ]
    
    PESOS = {
        "Confianza en condiciones submarinas": 0.20,
        "Vida útil del componente en agua salada": 0.15,
        "Impacto en el presupuesto del proyecto": 0.15,
        "Confiabilidad en interfaz humano-máquina": 0.25,
        "Seguridad del operario en uso submarino": 0.25
    }

    variables = {}
    valor_labels = {}
    sliders = {}

    # Función para crear callback dinámico
    def crear_callback(criterio, var, label):
        def callback(value):
            var.set(value)
            label.configure(text=f"{value:.2f}")
            calcular_resultados()
        return callback

    # Crear sliders dinámicamente
    for i, criterio in enumerate(CRITERIOS):
        variables[criterio] = tk.DoubleVar(value=4.0)

        # Label principal del criterio
        criterio_label = ctk.CTkLabel(
            main_frame,
            text=f"{criterio} (Peso: {PESOS[criterio]*100}%):",
            font=("Arial", 16, "bold")
        )
        criterio_label.grid(row=i+1, column=0, padx=20, pady=15, sticky="w")

        # Slider
        sliders[criterio] = ctk.CTkSlider(
            main_frame,
            from_=1,
            to=7,
            variable=variables[criterio],
            width=400,
            height=20,
            progress_color="#2c29ba",
            button_color="#4dafff"
        )
        sliders[criterio].grid(row=i+1, column=1, padx=20, pady=15, sticky="ew")

        # Label de valor
        valor_labels[criterio] = ctk.CTkLabel(
            main_frame,
            text="4.00",
            font=("Arial", 16, "bold"),
            width=60
        )
        valor_labels[criterio].grid(row=i+1, column=2, padx=20, pady=15)

        # Configurar comando después de crear el label
        sliders[criterio].configure(
            command=crear_callback(criterio, variables[criterio], valor_labels[criterio])
        )

    def calcular_resultados():
        # Fórmula con pesos diferentes: Suma ponderada de los ratings
        suma_ponderada = 0
        for criterio in CRITERIOS:
            rating = variables[criterio].get()
            peso = PESOS[criterio]
            suma_ponderada += rating * peso
        
        # Convertir a porcentaje
        porcentaje = ((suma_ponderada - 1) / 6) * 100
        
        # Interpretar el resultado
        if porcentaje >= 80:
            interpretacion = "IMPACTO MUY POSITIVO - Decisión altamente favorable"
            color = "#4CAF50"
        elif porcentaje >= 60:
            interpretacion = "IMPACTO POSITIVO - Buena decisión con beneficios claros" 
            color = "#FF9800"
        elif porcentaje >= 40:
            interpretacion = "IMPACTO NEUTRO - Considera alternativas o mejoras"
            color = "#FFC107"
        else:
            interpretacion = "IMPACTO NEGATIVO - Reevalúa esta opción"
            color = "#f44336"
        
        indice_label.configure(text=f"Índice de Afectación: {porcentaje:.2f}%")
        interpretacion_label.configure(text=interpretacion, text_color=color)

    # Frame de resultados
    resultados_frame = ctk.CTkFrame(main_frame)
    resultados_frame.grid(row=len(CRITERIOS)+1, column=0, columnspan=3, padx=10, pady=30, sticky="ew")

    # Label del índice
    indice_label = ctk.CTkLabel(
        resultados_frame,
        text="Índice de Afectación: 50.00%",
        font=("Arial", 24, "bold")
    )
    indice_label.pack(pady=(20, 10))

    # Label de interpretación
    interpretacion_label = ctk.CTkLabel(
        resultados_frame,
        text="Ajusta los sliders para ver el impacto de tu decisión",
        font=("Arial", 16),
        text_color="gray"
    )
    interpretacion_label.pack(pady=(0, 20))

    # Configurar grid
    main_frame.grid_columnconfigure(0, weight=1)
    main_frame.grid_columnconfigure(1, weight=2)
    main_frame.grid_columnconfigure(2, weight=0)
    
    # Calcular resultados iniciales
    calcular_resultados()

    app.mainloop()
