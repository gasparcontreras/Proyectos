/*
El área académica requiere generar un reporte que clasifique el desempeño de los
estudiantes según su nota final registrada en la tabla Stats.Scores.
Se debe construir una consulta que muestre:
• El nombre del estudiante.
• Una nueva columna calculada denominada, por ejemplo, estado_nota, que
clasifique al estudiante según los siguientes criterios:
o Si la nota es mayor a 80 → mostrar: "APROBADO"
o Si la nota está entre 61 y 80 → mostrar: "REFUERZO"
o Si la nota es menor o igual a 60 → mostrar: "DESAPROBADO"

Consideraciones técnicas:
• La clasificación debe realizarse utilizando la expresión CASE.
• No se debe modificar la tabla original.
• El resultado debe generarse únicamente mediante una consulta SELECT.
• La consulta debe contemplar correctamente los rangos sin superposición de
condiciones.
*/

USE [TSQL]

SELECT *
FROM Stats.Scores AS SS;


-- Consulta final

SELECT
    SS.testid,
	SS.studentid,
	SS.score,
    CASE 
        WHEN SS.score > 80 THEN 'APROBADO'
        WHEN SS.score BETWEEN 61 AND 80 THEN 'REFUERZO'
        WHEN SS.score <= 60 THEN 'DESAPROBADO'
    END AS 'ESTADO DE NOTA'
FROM Stats.Scores AS SS;


/*
El área académica requiere un reporte que clasifique el desempeño final de cada
estudiante considerando el promedio de sus evaluaciones registradas en
Stats.Scores.
Construye una consulta que muestre:
• studentid
• El promedio de nota del estudiante (calculado a partir de todas sus
evaluaciones).
• Una columna calculada estado_notas con la clasificación según el
promedio:
o Promedio > 80 → "APROBADO"
o Promedio entre 61 y 80 → "REFUERZO"
o Promedio <= 60 → "DESAPROBADO"

Reglas
• Debes usar funciones de agregación + GROUP BY.
• La clasificación debe implementarse con CASE.
• No se deben crear tablas ni modificar datos: solo SELECT.
• Ordena el resultado por studentid.
*/


SELECT *
FROM Stats.Scores AS SS;

SELECT
    SS.studentid,
    AVG(SS.score) AS PROMEDIO_NOTA,
    CASE
        WHEN AVG(SS.score) > 80 THEN 'APROBADO'
        WHEN AVG(SS.score) BETWEEN 61 AND 80 THEN 'REFUERZO'
        ELSE 'DESAPROBADO'
    END AS ESTADO_NOTAS
FROM Stats.Scores AS SS
GROUP BY SS.studentid
ORDER BY SS.studentid;

/*
Desde el área de análisis de datos se solicita generar una visualización de los
productos de la tabla Production.Products, incorporando una nueva columna
calculada que clasifique el precio de cada producto según los siguientes criterios:
• Si el precio es menor o igual a 8, debe mostrarse la etiqueta: "PRECIO
BAJO".
• Si el precio es mayor a 8 y menor o igual a 15, debe mostrarse: "PRECIO
MEDIO".
• Si el precio es mayor a 15 y menor o igual a 45, debe mostrarse: "PRECIO
MEDIO ALTO".
• Si el precio es mayor a 45, debe mostrarse: "PRECIO ALTO".
• Si el producto no tiene precio registrado (NULL), debe mostrarse el
mensaje: "NO TIENE PRECIO".
Consideraciones:
• La clasificación debe implementarse utilizando la expresión CASE.
• El resultado debe mostrarse únicamente como una consulta SELECT.
*/

SELECT *
FROM Production.Products AS PP;


SELECT
    PP.productid,
    PP.productname,
    PP.unitprice,
    CASE
        WHEN PP.unitprice IS NULL THEN 'NO TIENE PRECIO'
        WHEN PP.unitprice <= 8 THEN 'PRECIO BAJO'
        WHEN PP.unitprice > 8 AND PP.unitprice <= 15 THEN 'PRECIO MEDIO'
        WHEN PP.unitprice > 15 AND PP.unitprice <= 45 THEN 'PRECIO MEDIO ALTO'
        WHEN PP.unitprice > 45 THEN 'PRECIO ALTO'
    END AS CLASIFICACION
FROM Production.Products AS PP
ORDER BY PP.productid;

/*
Consultas agrupadas con JOIN y funciones de agregación
Desde el área de análisis comercial se solicita generar un reporte consolidado que
permita analizar el desempeño de ventas por producto y proveedor.
Para ello, deberá construirse una consulta que muestre:
• La cantidad de órdenes asociadas a cada producto.
• El promedio de venta por producto.
• El nombre del producto.
• La compañía del proveedor.
• El nombre del proveedor.
Consideraciones técnicas:
• Se deben utilizar las siguientes tablas:
o Sales.OrderDetails
o Production.Products
o Production.Suppliers
• La consulta debe incluir:
o Relaciones adecuadas mediante JOIN.
o Uso de funciones de agregación.
o Agrupación correcta de los datos.
• El resultado debe mostrar la información agrupada por producto y
proveedor.
No se deben crear tablas nuevas. El resultado debe mostrarse únicamente
mediante una consulta SELECT.
*/

SELECT *
FROM Sales.OrderDetails AS OD;

SELECT *
FROM Production.Products AS P;

SELECT *
FROM Production.Suppliers AS S;

SELECT
    P.productname,
    S.companyname,
    S.contactname,
    COUNT(DISTINCT OD.orderid) AS 'ORDENES POR PRODUCTO',
    AVG(OD.unitprice * OD.qty) AS 'PROMEDIO DE VENTA'
FROM Sales.OrderDetails AS OD
INNER JOIN Production.Products AS P
    ON OD.productid = P.productid
INNER JOIN Production.Suppliers AS S
    ON P.supplierid = S.supplierid
GROUP BY
    P.productname,
    S.companyname,
    S.contactname
ORDER BY 1, 3;