import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def graficar_dispersion_personalizado(filamentos_metalicos):
    propiedades_disponibles = [key for key in filamentos_metalicos[0].keys() if key != 'metal']
    print("\nPropiedades disponibles:")
    for i, prop in enumerate(propiedades_disponibles, 1):
        print(f"  {i}. {prop.replace('_', ' ').title()}")
    
    while True:
        try:
            eje_x_num = int(input("\nIntroduce el número de la categoría para el Eje X: "))
            eje_y_num = int(input("Introduce el número de la categoría para el Eje Y: "))

            if 1 <= eje_x_num <= len(propiedades_disponibles) and \
               1 <= eje_y_num <= len(propiedades_disponibles):
                
                eje_x_nombre = propiedades_disponibles[eje_x_num - 1]
                eje_y_nombre = propiedades_disponibles[eje_y_num - 1]
                break
            else:
                print("Por favor, introduce números válidos dentro del rango mostrado.")
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número.")
            
    eje_x_valores = [f[eje_x_nombre] for f in filamentos_metalicos]
    eje_y_valores = [f[eje_y_nombre] for f in filamentos_metalicos]
    nombres_metales = [f["metal"] for f in filamentos_metalicos]
    
    plt.figure(figsize=(10, 6))
    plt.scatter(eje_x_valores, eje_y_valores)
    
    for i, nombre in enumerate(nombres_metales):
        plt.annotate(nombre, (eje_x_valores[i], eje_y_valores[i]),
                     textcoords="offset points", xytext=(0, 10), ha='center')
                     
    plt.title(f'{eje_y_nombre.replace("_", " ").title()} vs. {eje_x_nombre.replace("_", " ").title()}')
    plt.xlabel(eje_x_nombre.replace("_", " ").title())
    plt.ylabel(eje_y_nombre.replace("_", " ").title())
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def crear_grafico_radar(filamentos_metalicos):
    if not filamentos_metalicos:
        print("Error: La lista de filamentos está vacía. No se puede generar el gráfico.")
        return

    df = pd.DataFrame(filamentos_metalicos)
    df.set_index('metal', inplace=True)
    
    filamentos_disponibles = df.index.tolist()
    print("Filamentos disponibles para comparar:")
    for i, metal in enumerate(filamentos_disponibles):
        print(f"{i+1}. {metal}")

    while True:
        try:
            opcion1 = int(input("\nIngresa el número del primer filamento: ")) - 1
            opcion2 = int(input("Ingresa el número del segundo filamento: ")) - 1
            
            if opcion1 in range(len(filamentos_disponibles)) and opcion2 in range(len(filamentos_disponibles)):
                metal1 = filamentos_disponibles[opcion1]
                metal2 = filamentos_disponibles[opcion2]
                break
            else:
                print("Error: Opciones no válidas. Por favor, ingresa los números correctos de la lista.")
        except ValueError:
            print("Error: Entrada no válida. Por favor, ingresa un número.")
            
    df_comparacion = df.loc[[metal1, metal2]].transpose()

    caracteristicas = df_comparacion.index.tolist()
    num_vars = len(caracteristicas)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)

    for columna in df_comparacion.columns:
        valores = df_comparacion[columna].tolist()
        valores += valores[:1]
        ax.plot(angles + angles[:1], valores, 'o-', linewidth=2, label=columna)
        ax.fill(angles + angles[:1], valores, alpha=0.25)

    ax.set_xticks(angles)
    ax.set_xticklabels(caracteristicas, fontsize=10, ha='right')
    ax.set_yticklabels([])

    plt.title(f'Comparación de {metal1} vs {metal2}', size=15, color='black', y=1.1)
    plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1))
    plt.grid(True)
    plt.show()

def graficar_swarm(filamentos_metalicos):
    df = pd.DataFrame(filamentos_metalicos)

    df_long = df.melt(id_vars='metal', var_name='metrica', value_name='valor')

    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(14, 8))

    swarm_plot = sns.swarmplot(
        data=df_long,
        x='metal',
        y='valor',
        hue='metal',
        legend=False,
        size=7
    )

    plt.title('Gráfico de Dispersión de Todas las Métricas por Metal', fontsize=16)
    plt.xlabel('Filamento Metálico', fontsize=12)
    plt.ylabel('Valor de la Métrica', fontsize=12)

    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
