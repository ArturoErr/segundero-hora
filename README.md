--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# segundero-hora
Este script en Python permite dos operaciones relacionadas con el tiempo:

Convertir una hora (HH:MM:SS) a segundos totales.

Convertir una cantidad de segundos (>=3600) a una representación en horas, minutos y segundos.

El usuario puede elegir entre ambas funciones o salir del programa.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Contenido del archivo

segundero-hora.py: Código fuente que contiene las funciones:

calc_segundos(): Lee una hora en formato HH:MM:SS, valida la entrada y muestra los segundos totales.

calc_hora(): Lee una cantidad de segundos, valida que sea >=3600 y muestra la hora correspondiente.

Menú interactivo para seleccionar la opción deseada o salir.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Requisitos

Python 3.x instalado en el sistema.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Uso

Clona el repositorio o descarga el archivo segundero-hora.py.

git clone <URL-del-repositorio>
cd <directorio-del-repositorio>

Ejecuta el script con Python:

python segundero-hora.py

Sigue las instrucciones en pantalla:

Calcular segundos -> Presionar 0
Calcular horas, minutos y segundo -> Presionar 1
Salir -> 2
Respuesta: 

Ingresa los valores cuando se te solicite y obtén el resultado en consola.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Explicación del funcionamiento

Conversión de hora a segundos:

Se solicita la hora en formato HH:MM:SS.

Se validan rangos: horas entre 0 y 23, minutos y segundos entre 0 y 59.

Se calcula segundos = horas*3600 + minutos*60 + segundos.

Conversión de segundos a hora:

Se solicita un número de segundos (>= 3600).

Se valida que sea al menos 3600.

Se calculan horas, minutos y segundos

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
