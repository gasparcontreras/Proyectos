#Buscar subcadenas dentro de una cadena de texto y devolver la posición

mensaje = 'Bienvenidos alumnos al curso de Python'
buscar = 'Python'
posición = mensaje.find(buscar)
print(posición)
print(f'La palabra buscada {buscar} está en la posición {posición}')
