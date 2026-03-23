import os
import time
import sqlite3

DB_NAME = "miprimeraprueba.db"

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# vamos a crear la conexión a la base de datos y el cursor para ejecutar las consultas
conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

# creamos la tabla productos con los campos clave, nombre y costo
cursor.execute("""
CREATE TABLE IF NOT EXISTS productos (
    clave INTEGER PRIMARY KEY,
    nombre TEXT,
    costo REAL
)
""")
conn.commit()
#menu opciones para la pesrona
while True:
    print(
        '---MENU----\n'
        '1. Agregar producto\n'
        '2. Eliminar producto\n'
        '3. Buscar producto\n'
        '4. Actualizar producto\n'
        '5. Mostrar la lista de productos\n'
        '6. Salir del sistema\n'
    )

    try:
        opcion = int(input('Elige la opción del menú: '))
    except ValueError:
        print("Ingresa un número válido.")
        time.sleep(2)
        clear()
        continue
#agrego el producto
    if opcion == 1:
        try:
            clave = int(input('Ingrese la clave del producto: '))
            nombre = input('Ingrese el nombre del producto: ')
            costo = float(input('Ingrese el costo del producto: '))

            sql = "INSERT INTO productos (clave, nombre, costo) VALUES (?, ?, ?)"
            val = (clave, nombre, costo)
            cursor.execute(sql, val)
            conn.commit()

            print(cursor.rowcount, "producto agregado.")
        except sqlite3.IntegrityError:
            print("Ya existe un producto con esa clave.")
        time.sleep(2)
        clear()
#elimino el producto
    elif opcion == 2:
        clave = int(input('Ingrese la clave del producto a eliminar: '))
        sql = "DELETE FROM productos WHERE clave = ?"
        val = (clave,)
        cursor.execute(sql, val)
        conn.commit()

        if cursor.rowcount:
            print(cursor.rowcount, "producto eliminado.")
        else:
            print("No se encontró ningún producto con esa clave.")
        time.sleep(2)
        clear()
#busco el producto
    elif opcion == 3:
        clave = int(input('Ingrese la clave del producto a buscar: '))
        sql = "SELECT * FROM productos WHERE clave = ?"
        val = (clave,)
        cursor.execute(sql, val)
        result = cursor.fetchone()

        if result:
            print(f"\nProducto encontrado:\n  Clave: {result[0]} | Nombre: {result[1]} | Costo: ${result[2]:.2f}")
        else:
            print("Producto no encontrado.")
        time.sleep(3)
        clear()
#actualizo el producto
    elif opcion == 4:
        clave = int(input('Ingrese la clave del producto a actualizar: '))
        nombre = input('Ingrese el nuevo nombre del producto: ')
        costo = float(input('Ingrese el nuevo costo del producto: '))

        sql = "UPDATE productos SET nombre = ?, costo = ? WHERE clave = ?"
        val = (nombre, costo, clave)
        cursor.execute(sql, val)
        conn.commit()

        if cursor.rowcount:
            print(cursor.rowcount, "producto actualizado.")
        else:
            print("No se encontró ningún producto con esa clave.")
        time.sleep(2)
        clear()
#muestro la lista de productos
    elif opcion == 5:
        cursor.execute("SELECT * FROM productos")
        result = cursor.fetchall()

        if result:
            for x in result:
                print(x)
        else:
            print("No hay productos registrados.")

        time.sleep(10)
        clear()
#salgo del sistema
    elif opcion == 6:
        print('Saliendo del sistema...')
        time.sleep(1)
        clear()
        break

    else:
        print("Opción no válida.")
        time.sleep(2)
        clear()
#cierro la conexión a la base de datos
cursor.close()
conn.close()

