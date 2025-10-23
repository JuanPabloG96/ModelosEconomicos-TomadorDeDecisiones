from modulos.modulo1 import mostrar_filamentos

def cambiar_campo(filamentos_metalicos):
    mostrar_filamentos(filamentos_metalicos)
    try:
        filamento = int(input(f"Elige el filamento a modificar (1-{len(filamentos_metalicos)}): ").strip())
        if filamento <= 0 or filamento > len(filamentos_metalicos):
            print("Error: El número de filamento seleccionado no existe.")
            return

        propiedad = input("Elige la propiedad a modificar: ").strip()
        if propiedad not in filamentos_metalicos[filamento - 1]:
            print("Error: La propiedad seleccionada no existe.")
            return
        
        valor = float(input(f"Nuevo valor para la propiedad '{propiedad}': ").strip())
        filamentos_metalicos[filamento - 1][propiedad] = valor
        print(f"\nFilamento {filamento} modificado con éxito.")

    except ValueError:
        print("Error: Por favor, ingresa el tipo de dato correcto.")    
