libros = [
    ("El principito", 1943, True),
    ("Alas de Hierro", 2023, True),
    ("Alchemised", 2026, False)
]

print(libros)
print(len(libros))
print(libros[0])
print(libros[0][0])

for libro in libros:
    print(libro)

for titulo,anio,disponible in libros:
    print(titulo)
    print(anio)
    print(disponible)
    print() #separador entre libros
    print("-----") #línea separadora entre libros

#EJERCICIO 2:
#Modifica el programa para mostrar exclusivamente los títulos de los libros disponibles
libros = [
    ("El principito", 1943, True),
    ("Alas de Hierro", 2023, True),
    ("Alchemised", 2026, False)
]

#1
for titulo, anio, disponible in libros:
    if disponible:
        print(titulo)

#2
for libro in libros:
    if libro[2]: #verifica si el libro está disponible
        print(libro[0])

#3
print([libro[0] for libro in libros if libro[2]])

#EJERCICIO 2:
cont=0
#1
for libro in libros:
    if libro[2]: #verifica si el libro está disponible
        cont+=1
print(f"Número de libros disponibles: {cont}")

#2
for titulo, anio, disponible in libros:
    if disponible:
        cont+=1
print(f"Número de libros disponibles: {cont}")

#3
print(len([libro[0] for libro in libros if libro[2]]))

libros.append(("El Hobbit", 1937, True))
print(libros) #verifica que se haya agregado el libro
print(len(libros)) #verificar el número de libros después de agregar uno nuevo
print([libro[0] for libro in libros if libro[2]]) #verificar los títulos de los libros disponibles después de agregar uno nuevo

print([libro[0] for libro in libros if libro[2]]) #verificar los títulos de los libros disponibles después de agregar uno nuevo
#("En algún lugar de la Mancha", 1605, True)

titulos =[] 
for titulo, anio, disponible in libros:
    if disponible:
        titulos.append(titulo)
print(titulos)