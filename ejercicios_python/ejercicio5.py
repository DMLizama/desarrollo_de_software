peliculas_list = []
peliculas_por_anio = {}

i=0
while i <= 4: #for i in range(5)
    peli = input("Ingrese nombre de película: ")
    anio = int(input("Ingrese año de estreno: ")) #no atrapa si ingresa una str...

    peliculas_list.append(peli) #agrego la peli a la lista

    if anio not in peliculas_por_anio: #si no hay dict con anio = anio, creo el dict con ese anio
        peliculas_por_anio[anio] = []
    
    peliculas_por_anio[anio].append(peli) #agrego la peli al dict con el anio = anio

    i+=1

print("\nLista de pelis:")
#for pelicula in sorted(peliculas_list):
#    print(pelicula)
print(peliculas_list)


print("\nPelis según el año")
for anio, pelicula in peliculas_por_anio.items():
    print(f"{anio}: {pelicula}")
