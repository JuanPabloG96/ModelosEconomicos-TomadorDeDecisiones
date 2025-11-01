import numpy as np
import matplotlib.pyplot as plt

def comparar_metodos_mcdm (filamentos_metalicos):
    # Obtener los datos
    alternativas = [filamento["metal"] for filamento in filamentos_metalicos]
    criterios = [key for key in filamentos_metalicos[0].keys() if key != "metal"]
    valores = []

    for filamento in filamentos_metalicos:
        valor_actual = [valor for key, valor in filamento.items() if key != "metal"]
        valores.append(valor_actual)
    
    pesos_moora = [0.2458, 0.0271, 0.1287, 0.1287, 0.0280, 0.0581, 0.0099, 0.0800, 0.0160, 0.0286, 0.1682, 0.0810]
    pesos_vikor = [1/12]*12


    def calcular_moora():
        matriz_normalizada = []
        
        for i in range(len(alternativas)):
            fila = []
            for j in range(len(criterios)):
                suma_cuadrados = np.sqrt(sum(valor[j] ** 2 for valor in valores))
                fila.append((valores[i][j] / suma_cuadrados) * pesos_moora[j])
            matriz_normalizada.append(fila)
        
        resultados = []
        for i in range(len(alternativas)):
            positivo = sum(matriz_normalizada[i][j] for j in range(len(criterios)) if j not in [2, 7, 8])
            negativo = sum(matriz_normalizada[i][j] for j in [2, 7, 8])
            resultados.append(positivo - negativo)
        
        return resultados

    def calcular_vikor():
        tipos_criterios = ["b", "b", "b", "b", "c", "b", "c", "c", "b", "b", "b", "b"]
        parametro_compromiso = 0.5
        
        mejores_valores = []
        peores_valores = []
        
        for j in range(len(criterios)):
            valores_criterio = [fila[j] for fila in valores]
            
            if tipos_criterios[j] == 'b':  # Criterio de beneficio
                mejores_valores.append(max(valores_criterio))
                peores_valores.append(min(valores_criterio))
            else:  # Criterio de costo
                mejores_valores.append(min(valores_criterio))
                peores_valores.append(max(valores_criterio))
        
        medidas_utilidad_grupal = []
        medidas_arrepentimiento_individual = []
        
        for i in range(len(alternativas)):
            suma_utilidad = 0
            maximo_arrepentimiento = -float('inf')
            
            for j in range(len(criterios)):
                if mejores_valores[j] == peores_valores[j]:
                    valor_normalizado = 0
                else:
                    valor_normalizado = pesos_vikor[j] * (
                        mejores_valores[j] - valores[i][j]
                    ) / (mejores_valores[j] - peores_valores[j])
                
                suma_utilidad += valor_normalizado
                
                if valor_normalizado > maximo_arrepentimiento:
                    maximo_arrepentimiento = valor_normalizado
            
            medidas_utilidad_grupal.append(suma_utilidad)
            medidas_arrepentimiento_individual.append(maximo_arrepentimiento)
        
        mejor_utilidad = min(medidas_utilidad_grupal)
        peor_utilidad = max(medidas_utilidad_grupal)
        mejor_arrepentimiento = min(medidas_arrepentimiento_individual)
        peor_arrepentimiento = max(medidas_arrepentimiento_individual)
        
        indicadores_compromiso = []
        for i in range(len(alternativas)):
            if peor_utilidad == mejor_utilidad:
                termino_utilidad = 0
            else:
                termino_utilidad = parametro_compromiso * (
                    medidas_utilidad_grupal[i] - mejor_utilidad
                ) / (peor_utilidad - mejor_utilidad)
            
            if peor_arrepentimiento == mejor_arrepentimiento:
                termino_arrepentimiento = 0
            else:
                termino_arrepentimiento = (1 - parametro_compromiso) * (
                    medidas_arrepentimiento_individual[i] - mejor_arrepentimiento
                ) / (peor_arrepentimiento - mejor_arrepentimiento)
            
            indicadores_compromiso.append(termino_utilidad + termino_arrepentimiento)
        
        return indicadores_compromiso, medidas_utilidad_grupal, medidas_arrepentimiento_individual


    def graficar_datos(datos, nombres, titulo="Gráfica de Barras", eje_x="Alternativas", eje_y="Valores"):
        plt.figure(figsize=(10, 6))
        barras = plt.bar(nombres, datos, color='skyblue', alpha=0.7)
        
        plt.title(titulo, fontsize=14, fontweight='bold')
        plt.xlabel(eje_x, fontsize=12)
        plt.ylabel(eje_y, fontsize=12)
        plt.xticks(rotation=45)
        
        for barra, valor in zip(barras, datos):
            plt.text(barra.get_x() + barra.get_width()/2, barra.get_height() + 0.01,
                    f'{valor:.3f}', ha='center', va='bottom', fontsize=10)
        
        plt.tight_layout()
        plt.show()


    def imprimir_informacion():
        print("VARIABLES")
        print("Alternativas: ")
        for alternativa in alternativas:
            print("\t", alternativa)

        print("\nCriterios: ")
        for criterio in criterios:
            print("\t", criterio)

        print("\nPesos usados en moora: \n\t", pesos_moora)
        print("Pesos usados en vikor: \n\t pesos iguales de ", round(pesos_vikor[0], 4))

    def ordenar_alternativas(alternativas, resultados, descendente=True):
        combinados = list(zip(alternativas, resultados))
        
        if descendente:
            combinados_ordenados = sorted(combinados, key=lambda x: x[1], reverse=True)
        else:
            combinados_ordenados = sorted(combinados, key=lambda x: x[1])
        
        alternativas_ordenadas = [alt for alt, res in combinados_ordenados]
        resultados_ordenados = [res for alt, res in combinados_ordenados]
        
        return alternativas_ordenadas, resultados_ordenados


    def tabla_comparativa(alternativas_originales, alternativas_ordenadas_ahp, alternativas_ordenadas_moora, alternativas_ordenadas_vikor):
        ranking_ahp = {alt: i+1 for i, alt in enumerate(alternativas_ordenadas_ahp)}
        ranking_moora = {alt: i+1 for i, alt in enumerate(alternativas_ordenadas_moora)}
        ranking_vikor = {alt: i+1 for i, alt in enumerate(alternativas_ordenadas_vikor)}
        
        print("\n\nTABLA COMPARATIVA DE RANKINGS")
        print("=" * 56)
        print(f"{'Alternativa':<35} {'AHP':<6} {'MOORA':<6} {'VIKOR':<6}")
        print("-" * 56)
        
        for alternativa in alternativas_originales:
            print(f"{alternativa:<35} {ranking_ahp[alternativa]:<6} {ranking_moora[alternativa]:<6} {ranking_vikor[alternativa]:<6}")
        
        print("=" * 56)
        print("Nota: Ranking 1 = Mejor, 7 = Peor")

    resultados_ahp = [0.1456, 0.2242, 0.1462, 0.0795, 0.1347, 0.1378, 0.1321]
    resultados_moora = calcular_moora()
    resultados_vikor = calcular_vikor()

    resultados_q_vikor = resultados_vikor[0]

    alternativas_ordenadas_ahp, resultados_ordenados_ahp = ordenar_alternativas(alternativas, resultados=resultados_ahp)
    alternativas_ordenadas_mora, resultados_ordenados_mora = ordenar_alternativas(alternativas, resultados=resultados_moora)
    alternativas_ordenadas_vikor, resultados_ordenados_vikor = ordenar_alternativas(alternativas, resultados=resultados_q_vikor, descendente=False)

    imprimir_informacion()

    graficar_datos(
        datos=resultados_ordenados_ahp,
        nombres=alternativas_ordenadas_ahp,
        titulo="Resultados AHP"
    )

    graficar_datos(
        datos=resultados_ordenados_mora,
        nombres=alternativas_ordenadas_mora,
        titulo="Resultados Moora"
    )

    graficar_datos(
        datos=resultados_ordenados_vikor,
        nombres=alternativas_ordenadas_vikor,
        titulo="Resultados Vikor"
    )

    tabla_comparativa(
        alternativas, alternativas_ordenadas_ahp=alternativas_ordenadas_ahp,
        alternativas_ordenadas_moora=alternativas_ordenadas_mora,
        alternativas_ordenadas_vikor=alternativas_ordenadas_vikor
    )
