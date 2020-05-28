# SkylineBot
Práctica de Python para la asignatura LP de la FIB en el Q2 2019-2020. [Enunciat de la pràctica](https://github.com/gebakx/SkylineBot).

Un Skyline representa la vista horizontal de los edificios de una ciudad.
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

## Gestión de datos
Mientras dure la sesioón del bot, para cada usuario que interactue con él, el bot creará una tabla de símbolos que asociará al usuario con sus datos. Cuando el bot se apague, todas las tablas de símbolos que el bot tenga de cada usuario se perderán. <br>

Para que la gestión de datos funcione correctamente es necesario que exista la carpeta Data. Dentro de esta, cada usuario tiene su propia carpeta, para identificar cuál es la asignada a cada usuario, el nombre de esta se forma a partir del primer nombre del usuario, la inicial de su apellido (si es que tiene), y los 5 ultimos digitos de su identificador de Telegram. Allá tendrá alojados todos sus datos, es decir, sus Skylines. Que en principio serán ficheros con la extensión `.sky` que podrán cargar en su tabla de símbolos.<br>

Un fichero `*.sky` representa uno de los Skylines que el usuario ha guardado en disco que previamente se encontraba en su tabla de símbolos usando el comando `/save id`. Solo de esta forma el usuario podrá preservar un Skyline entre una sesión y otra.

Para ver la lista de ficheros con estensión `.sky` que el usuario tiene actualmente en disco se ha añadido un nuevo comando `/disk` para evitar confusiones y que no sea imprescindible recordar el nombre de los Skylines que se han guardado previamente.<br>

Para cargar el sky en la tabla de símbolos actual del usuario basta con usar `load id`.
## Classe Skyline
### Atributos
Un Skyline esta representado por 3 atributos principalmente:
* Lista de intervalos: Una lista de enteros que representa los intervalos en los que hay edificios del mismo tamaño.
* Lista de valores: Una lista de enteros que representa el valor de la altura entre cada intervalo. El valor en la posicion `i` de la lista de valores corresponderá a la altura que tendrá el edificio en los intervalos `i` e `i+1` en la lista de intervalos. El último valor de esta lista siempre será 0.
* Tupla de colores: Una tupla que contiene los colores RGB del Skyline. Así siempre se representará siempre del mismo color sin poder provocar confusión al usuario.

### Métodos
Las siguientes funciones estan documentadas en el codigo explicando como funcionan, ya que son más sofisticadas que las otras.
* Union: Método de Union del Skyline self con otro pasado por parámetro.
* Intersección: Método de Intersección del Skyline self con otro pasado por parámetro.
Estas otras funciones tienen una pequeña descripción en el código y no son dificiles de comprender. Aún así tienen algun que otro comentario:
* Mirror: Invierte un Skyline
* MoveOffset: Desplaza un Skyline dado un valor de desplazamiento.
* Replicate: Replica consecutivamente un Skyline dado un valor de replicación.
### Métodos estáticos
La clase Skyline tiene un par de métodos estaticos que ayudan en algunos cálculos.
* binary_search(list, val): El método ya se sobreentiende, dado `val`, indica en que posición está en la lista `list`, si no se encuentra, devuelve la posición en la que debería ir.
* flaten(intervals, values): El método quita valores que se puedan considerar redundantes dada una lista de intervalos y valores. Por ejemplo, si tenemos los siguientes valores del primer bloque, estos se transformarán en los del segundo bloque, que serían equivalentes:

    ```python
    intervals   = [0,4,5]
    values      = [3,3,0]
    ```


    ```python
    intervals   = [0,5]
    values      = [3,0]
    ```

## Comando adicional: /disk
Este comando se ha creado para que el usuario pueda saber cuales son los Skylines guardados en disco ya que no habia otra forma de saberlo anteriormente.<br>
Para usarlo basta con enviar `/disk` al bot, si el usuario tiene Skylines en disco, se le mostrará el nombre de estos, en caso contrario el bot enviará un mensaje diciendo que no hay ningún Skyline suyo en disco.
## Built With

* [ANTLR4](https://www.antlr.org/) - ANother Tool for Language Recognition
* [matplotlib](https://matplotlib.org/) - Plotting library
* [python-telegram-bot](https://python-telegram-bot.org/) - Telegram Bot API wrapper for Python

## Autor
* Rodrigo Arian Huapaya Sierra