# SkylineBot
Práctica de Python para la asignatura LP de la FIB en el Q2 2019-2020. [Enunciat de la pràctica](https://github.com/gebakx/SkylineBot).

Un Skyline es la representación de la vista horizontal de los edificios de una ciudad.
Este bot permite a un usuario manipular sus propios Skylines mediante un intérprete usando un conjunto de comandos.

## Para empezar
A continuacion una serie de instrucciones para tener todo preparado para empezar a utilizar el bot.

### Prerequisitos
Hay una serie de librerias de Python3 necesarias para ejecutar el bot, para obtenerlas basta con usar el siguiente comando:

```bash
$ pip3 install -r requirements.txt
```
### Ejecucion
Para ejecutar el bot con el que se podrá interactuar atraves de Telegram serán necesarios una serie de archivos generados por antlr. Para obtenerlos bastará con ejecutar la siguiente instrucción:
```bash
$ antlr4 -Dlanguage=Python3 -no-listener -visitor cl/Skyline.g4
```

Y finalmente, para empezar a interactuar con el bot por Telegram:
```bash
$ python3 bot.py
```
El bot necesitará un archivo `token.txt` para que funcione correctamente. El archivo `bot.py` cargará de forma predeterminada aquel documento de texto `token.txt` que se encuentre en el mismo directorio.

## Clase Skyline
### Atributos
Un Skyline esta representado por 3 atributos principalmente:
* Lista de intervalos: Una lista de enteros que representa los intervalos en los que hay edificios del mismo tamaño.
* Lista de valores: Una lista de enteros que representa el valor de la altura entre cada intervalo. El valor en la posicion `i` de la lista de valores corresponderá a la altura que tendrá el edificio en los intervalos `i` e `i+1` en la lista de intervalos. El último valor de esta lista siempre será 0.
* Tupla de colores: Una tupla que contiene los colores RGB del Skyline. Así cada Skyline siempre se representará con el mismo color sin poder provocar confusión al usuario, ayudandolo a diferenciar entre los diferentes Skylines que pueda tener, eso sí, si se hace una unión o una intersección, entonces este color se verá modificado de forma completamente aleatoria.

### Métodos
Las siguientes funciones estan documentadas en el codigo explicando como funcionan, ya que son más sofisticadas que las otras.
* Union: Método de Union del Skyline self con otro pasado por parámetro.
* Intersección: Método de Intersección del Skyline self con otro pasado por parámetro.

Cabe destacar que hay dos formas de hacer uniones en el codigo. Una se hace con el overload del operador `+` y la otra en `+=`. La primera se usa en uniones simples, ya que hará los calculos necesarios para obtener immediatemente el área del nuevo Skyline. El segundo tipo de unión obviará el cálculo de este dato, lo cual la hará más eficiente, esta unión solo se hace en la creación de edificios aleatorios y compuestos. Se puede comprobar que en cuanto la creación del Skyline ha finalizado, entonces se hará el cálculo del área.<br><br>

Estas otras funciones tienen una pequeña descripción en el código y no son dificiles de comprender. Aún así tienen algun que otro comentario:
* Mirror: Invierte un Skyline
* MoveOffset: Desplaza un Skyline dado un valor de desplazamiento.
* Replicate: Replica consecutivamente un Skyline dado un valor de replicación.

### Métodos estáticos
La clase Skyline tiene un par de métodos estaticos que ayudan en algunos cálculos.
* binary_search(list, val): El método ya se sobreentiende, dado `val`, indica en que posición está en la lista `list`, si no se encuentra, devuelve la posición en la que debería ir.
* flatten(intervals, values): El método quita valores que se puedan considerar redundantes dada una lista de intervalos y valores. Por ejemplo, si tenemos los siguientes valores del primer bloque, estos se transformarán en los del segundo bloque llamando a la función flatten con los parámetros correctamente:

    ```python
    intervals   = [0,4,5]
    values      = [3,3,0]
    ```


    ```python
    intervals   = [0,5]
    values      = [3,0]
    ```

### Optimización de la creadora aleatoria y compuesta
Estas dos creadoras aprovechan la función `flatten` para ser más optimas, tras varias pruebas se ha comprobado que si cada 512 uniones (el número es una potencia de 2 para que la evaluación sea lo más rápida posible) se hace una llamada a esta función con los `intervalos` y `values` que tenga en ese momento, entonces la velocidad a la que se genera el Skyline aleatorio o compuesto se reduce de forma considerable.

## Gestión de datos
Mientras dure la sesión del bot, para cada usuario que interactue con él, el bot creará una tabla de símbolos que asociará al usuario con sus datos. Cuando el bot se apague, todas las tablas de símbolos que el bot tenga de cada usuario se perderán. <br>

Para que la gestión de datos funcione correctamente es necesario que exista la carpeta Data. Dentro de esta, cada usuario tiene su propia carpeta, para identificar cuál es la asignada a cada usuario, el nombre de esta se forma a partir del primer nombre del usuario, la inicial de su apellido (si es que tiene), y los 5 ultimos digitos de su identificador de Telegram. Allá estarán alojados todos los Skylines que el usuario haya guardado con el comando `/save id`, que serán ficheros con el identificador del Skyline como nombre más la extensión `.sky`, que podrán ser cargados en la tabla de simbolos del usuario.<br>

Si el usuario quiere consultar la lista de Skylines que tiene actualmente en su tabla de simbolos puede usar el comando `/lst`. Si quiere borrar todos los identificadores puede usar el comando `/clean`.<br>

El usuario tiene que tener en mente que la única forma de mantener un Skyline entre una sesión y otra del bot es utilizando el comando `/save id` para guardar el Skyline en disco.<br>

Si el usuario quiere consultar la lista de Skylines que tiene actualmente en disco puede usar el nuevo comando `/disk`, que está explicado más abajo.<br>

Para cargar el sky en la tabla de símbolos actual del usuario basta con usar `/load id` de aquel Skyline que tenga en disco. Este comando además borrará el Skyline de disco para dejar más espacio.

## Comando adicional: /disk
Este comando se ha creado para que el usuario pueda saber cuales son los Skylines guardados en disco ya que no habia otra forma de saberlo anteriormente. Esto evitará que sea imprescindible para él tener que recordar el nombre de los Skylines que ha guardado entre sesión y sesión.<br>
Para usarlo basta con enviar `/disk` al bot, si el usuario tiene Skylines en disco, se le mostrará el nombre de estos, en caso contrario el bot enviará un mensaje indicando que no hay ningún Skyline suyo en disco.

# Gestión de errores del visitor
El visitor se encargará de devolver una imagen o un error dependiendo del resultado del analisis que haga. Los unicos errores que es capaz de gestionar son aquellos que aparecen en el enunciado de la práctica.

## Built With

* [ANTLR4](https://www.antlr.org/) - ANother Tool for Language Recognition
* [matplotlib](https://matplotlib.org/) - Plotting library
* [python-telegram-bot](https://python-telegram-bot.org/) - Telegram Bot API wrapper for Python

## Autor
* Rodrigo Arian Huapaya Sierra