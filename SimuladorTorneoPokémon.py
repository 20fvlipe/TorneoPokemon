import os, random as rd
os.system("cls")

combate = 0
contador_victoria = 0
contador_derrota = 0
contador_fuego = 0
contador_agua = 0
contador_planta = 0

acumulador_poder = 0

banderaLegendario = False

try:
    
    while combate <= 0:
        combate = int(input("Ingrese la Cantidad de Combates\n"))
        if combate <= 0:
            print("El valor debe ser mayor que 0.")
    
    for x in range(combate):
        nombre_entrenador = ""
        while len(nombre_entrenador) < 3:
            nombre_entrenador = input(f"Ingrese su Nombre (combate {x+1})\n").title()
            if len(nombre_entrenador) < 3:
                print("El largo del Nombre debe ser mayor a 2 caracteres.")
        
        tipo_pokemon = ""
        while tipo_pokemon != 'F' and tipo_pokemon != 'A' and tipo_pokemon != 'P':
            tipo_pokemon = input(f"Ingrese el Tipo de Pokemon (combate {x+1})\n").upper()
            if tipo_pokemon != 'F' and tipo_pokemon != 'A' and tipo_pokemon != 'P':
                print("Solo se aceptan los siguientes tipos: A (AGUA) - P (PLANTA)- F (FUEGO)")
        
        poder_base = rd.randint(1, 25)
        if tipo_pokemon == 'F':
            bonificacion = 3
            contador_fuego = contador_fuego + 1
        elif tipo_pokemon == 'A':
            bonificacion = 2
            contador_agua = contador_agua + 1
        else:
            bonificacion = 1
            contador_planta = contador_planta + 1
        
        poder_final = poder_base + bonificacion
        acumulador_poder = acumulador_poder + poder_final
        
        if poder_final >= 18:
            clasificacion_combate = "Victoria!!!"
            contador_victoria = contador_victoria + 1
        elif poder_final >= 10 and poder_final < 18:
            clasificacion_combate = "Batalla difícil."
        else:
            clasificacion_combate = "Derrota :("
            contador_derrota = contador_derrota + 1
        
        if poder_final >= 25:
            banderaLegendario = True
            mensaje = "¡Hubo un Pokémon Legendario en el Torneo!"
        
    
    promedio_poderes = acumulador_poder/combate
    
    os.system("cls")
    print("**************")
    print(f"Cantidad de Combates: {combate}")
    print(f"Cantidad de Victorias: {contador_victoria}")
    print(f"Cantidad de Derrotas: {contador_derrota}")
    print(f"Cantidad Pokemones Tipo Fuego: {contador_fuego}")
    print(f"Cantidad Pokemones Tipo Agua: {contador_agua}")
    print(f"Cantidad Pokemones Tipo Planta: {contador_planta}")
    print(f"Promedio de los poderes Finales: {promedio_poderes}")
    print(f"{mensaje}")
    print("**************")   
    
except:
    print("El valor ingresado debe ser numerico.")
    