import tkinter as tk
import customtkinter as ctk

def evaluacion_nom_035():
    app = ctk.CTk()
    app.geometry("1280x720")
    app.title("Evaluación NOM-035 - Factores Psicosociales en Fabricación Aditiva")

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    main_frame = ctk.CTkScrollableFrame(app, width=850)
    main_frame.pack(fill="both", expand=True, padx=40, pady=40)

    titulo = ctk.CTkLabel(
        main_frame,
        text="Evaluación NOM-035 - Factores Psicosociales en Fabricación Aditiva",
        font=("Arial", 22, "bold")
    )
    titulo.pack(pady=(0, 20))

    PREGUNTAS = [
        "Durante la operación y post-procesamiento de las impresoras 3D metálicas, ¿te expones a niveles de ruido, polvo o temperaturas que consideras molestos o peligrosos?",
        "¿La duración extensa de los trabajos de impresión y los plazos de entrega ajustados te generan una sensación de presión o estrés constante?",
        "¿Tu trabajo requiere un nivel de atención y concentración muy alto para monitorear los procesos de impresión que al final del día te cause fatiga mental?",
        "¿Las largas jornadas de impresión o la necesidad de monitorear equipos fuera del horario laboral normal interfiere con tu tiempo de descanso, comidas o vida personal?",
        "¿El estrés o la carga mental asociada a la planificación y supervisión de proyectos complejos afecta tu estado de ánimo o tus relaciones en casa?",
        "Al estar desarrollando el trabajo ¿la comunicación con otros departamentos es fluida y respetuosa?"
    ]

    OPCIONES_RESPUESTA = [
        "Siempre",
        "Casi siempre", 
        "A veces",
        "Nunca"
    ]

    variables = {}

    def calcular_puntuacion(pregunta_index, respuesta):
        if pregunta_index == 5:
            puntuaciones_invertidas = {
                "Siempre": 0,
                "Casi siempre": 1,
                "A veces": 2, 
                "Nunca": 3
            }
            return puntuaciones_invertidas[respuesta]
        else:
            puntuaciones_normales = {
                "Siempre": 3,
                "Casi siempre": 2,
                "A veces": 1,
                "Nunca": 0
            }
            return puntuaciones_normales[respuesta]

    def calcular_resultado():
        total_puntos = 0
        respuestas_completas = True

        for i, pregunta in enumerate(PREGUNTAS):
            variable = variables[pregunta]
            if variable.get() == "":
                respuestas_completas = False
                break
            respuesta_seleccionada = variable.get()
            total_puntos += calcular_puntuacion(i, respuesta_seleccionada)

        if not respuestas_completas:
            resultado_label.configure(
                text="Por favor, responde todas las preguntas antes de calcular el resultado.",
                text_color="yellow"
            )
            return

        if total_puntos >= 12:
            riesgo = "ALTO RIESGO PSICOSOCIAL"
            recomendacion = "Se recomienda tomar acciones inmediatas para reducir los factores de riesgo."
            color = "#f44336"
        elif total_puntos >= 6:
            riesgo = "RIESGO MODERADO"
            recomendacion = "Es necesario evaluar los factores de riesgo y considerar mejoras."
            color = "#ff9800"
        else:
            riesgo = "BAJO RIESGO PSICOSOCIAL" 
            recomendacion = "El ambiente laboral parece adecuado."
            color = "#4CAF50"

        resultado_texto = f"{riesgo}\n\nPuntuación total: {total_puntos}/18\n\n{recomendacion}"
        resultado_label.configure(text=resultado_texto, text_color=color)

    for i, pregunta in enumerate(PREGUNTAS):
        pregunta_frame = ctk.CTkFrame(main_frame)
        pregunta_frame.pack(fill="x", padx=10, pady=15)

        pregunta_label = ctk.CTkLabel(
            pregunta_frame,
            text=f"{i+1}. {pregunta}",
            font=("Arial", 14, "bold"),
            wraplength=850,
            justify="left"
        )
        pregunta_label.pack(anchor="w", padx=20, pady=(15, 10))

        variables[pregunta] = tk.StringVar(value="")

        opciones_frame = ctk.CTkFrame(pregunta_frame)
        opciones_frame.pack(fill="x", padx=20, pady=(0, 15))

        for j, opcion in enumerate(OPCIONES_RESPUESTA):
            opcion_radio = ctk.CTkRadioButton(
                opciones_frame,
                text=opcion,
                variable=variables[pregunta],
                value=opcion,
                font=("Arial", 12),
                fg_color="orange",
            )
            opcion_radio.pack(anchor="w", pady=5)

    boton_frame = ctk.CTkFrame(main_frame)
    boton_frame.pack(fill="x", padx=10, pady=20)

    calcular_boton = ctk.CTkButton(
        boton_frame,
        text="Calcular Resultado",
        command=calcular_resultado,
        font=("Arial", 16, "bold"),
        height=40
    )
    calcular_boton.pack(pady=20)

    resultado_frame = ctk.CTkFrame(main_frame)
    resultado_frame.pack(fill="x", padx=10, pady=20)

    resultado_label = ctk.CTkLabel(
        resultado_frame,
        text="Complete la evaluación y haga clic en 'Calcular Resultado'",
        font=("Arial", 16),
        wraplength=850,
        justify="center"
    )
    resultado_label.pack(padx=20, pady=20)

    app.mainloop()
