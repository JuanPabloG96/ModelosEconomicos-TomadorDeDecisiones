import os
import time

from modulos.modulo1 import mostrar_filamentos, agregar_filamento
from modulos.modulo2 import cambiar_campo
from modulos.modulo3 import graficar_dispersion_personalizado, crear_grafico_radar, graficar_swarm
from data.filamentos import filamentos_metalicos
from modulos.modulo4 import generar_conclusion_filamento, modelo_grand_prix
from modulos.modulo6 import huella_ecologica
from modulos.modulo7b import evaluacion_nom_035
from modulos.modulo8 import comparar_metodos_mcdm
from modulos.modulo9 import mostrar_libro

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

def menu_principal():
    print("""
Bienvenido al sistema de gestión de filamentos de metal.
\nSelecciona una opción:
1. Mostrar los filamentos de metal.
2. Agregar un nuevo filamento.
3. Cambiar un campo de un filamento.
4. Generar un gráfico de dispersión personalizado.
5. Generar un gráfico de radar.
6. Generar un gráfico de swarm.
7. Generar conclusiones sobre los filamentos.
8. Modelo Grand Prix.
9. Calcular huella ecológica.
10. Factores Psicosociales en Fabricación Aditiva
11. Comparar metodos MCDM
12. Mostrar libro PDF
0. Salir del sistema.
    """)

if __name__ == "__main__":
    while True:
        menu_principal()
        try:
            opcion = int(input(f"Selecciona una opción (0-12): "))
        except ValueError:
            print("Debes ingresar un número válido.")
            time.sleep(2)
            limpiar_pantalla()
            continue

        seleccion = {
            1: lambda: mostrar_filamentos(filamentos_metalicos),
            2: lambda: agregar_filamento(filamentos_metalicos),
            3: lambda: cambiar_campo(filamentos_metalicos),
            4: lambda: graficar_dispersion_personalizado(filamentos_metalicos),
            5: lambda: crear_grafico_radar(filamentos_metalicos),
            6: lambda: graficar_swarm(filamentos_metalicos),
            7: lambda: generar_conclusion_filamento("Titanio 64", 12.3),
            8: lambda: modelo_grand_prix(),
            9: lambda: huella_ecologica(),
            10: lambda: evaluacion_nom_035(),
            11: lambda: comparar_metodos_mcdm(filamentos_metalicos),
            12: lambda: mostrar_libro(),
            0: exit
        }
        
        if opcion in seleccion:
            limpiar_pantalla()
            seleccion[opcion]()  
            input("\nPresiona Enter para continuar...")
            limpiar_pantalla()
        else:
            print("Opción no válida.")
            time.sleep(2)
            limpiar_pantalla()
