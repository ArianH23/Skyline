from matplotlib import pyplot as plt
from random import randint, random
import time


class Skyline:

    # MÈTODE CREADOR
    def __init__(self, param1, param2=None, param3=None, xmin=None, xmax=None, color=None, type=None, asigna_atribs=True):
        """
        Mètode creador de la classe Skyline.
        """

        # Creació de Skyline simple
        # En aquest cas depenent de si param3 es buit:
        # param1 = xmin, param2 = height, param3 = xmax
        # param1 = llistaIntervals, param2 = llistaValues
        if type is None:
            # Primer tipus de creacio especificada
            if param3 is None:
                self.__intervalos = param1
                self.__values = param2
            # Segon tipus de creacio especificada
            else:
                self.__intervalos = [param1, param3]
                self.__values = [param2] + [0]

            if color is None:
                # Avoid creating a white Skyline which would not be seen in the plot.
                red = min(0.85, random())
                green = min(0.85, random())
                blue = min(0.85, random())

                self.__color = (red, green, blue)
            else:
                self.__color = color
            # Dependiendo de asigna_atribs, se haran calculos que puedan ser necesarios o no.
            if asigna_atribs:
                self.__area = self.__calculaArea()
                self.__height = max(self.__values)
                self.__intervalos, self.__values = Skyline.__flatten(
                    self.__intervalos, self.__values)

        # Creació de Skyline compost
        # En aquest cas:
        # param1 = llistaDeIntervalsIHeightsDe Skylines, de la forma:
        # [[xmin1, height1, xmax1], [xmin2, height2, xmax2]...]
        elif type == "complex":

            firstSky = Skyline(param1[0][0], param1[0][1], param1[0][2])

            self.__height = param1[0][1]

            for i in range(1, len(param1)):
                # Si el Skyline té alçada major que 0 i per tant es pot crear
                if param1[i][1] > 0:
                    firstSky += Skyline(param1[i][0],
                                        param1[i][1], param1[i][2])

                    if param1[i][1] > self.__height:
                        self.__height = param1[i][1]

                # Optimización: cada 512 Skylines se hace un flatten con
                # los valores que tenga firstSky, esto facilita las siguientes uniones.
                if i & ((1 << 9) - 1) == 0:
                    firstSky.__intervalos, firstSky.__values = Skyline.__flatten(
                        firstSky.__intervalos, firstSky.__values)

            self.__intervalos, self.__values = Skyline.__flatten(
                firstSky.__intervalos, firstSky.__values)

            self.__color = firstSky.__color
            self.__area = self.__calculaArea()

        # Creació de Skyline aleatori
        # En aquest cas:
        # param1 = nombreDeEdificis, param2 = alçadaMaximaDelsEdificis, param3 = ampladaMaximaDelsEdificis
        elif type == "random":

            maxFinal = xmax-param3

            nombreDeEdificis = param1
            alturaMaxima = param2
            ampladaMaxima = param3

            randomWidth = randint(1, ampladaMaxima)
            randomHeight = randint(1, alturaMaxima)
            randomXMin = randint(xmin, maxFinal)

            firstSky = Skyline(randomXMin, randomHeight,
                               randomXMin + randomWidth)

            self.__height = randomHeight

            for i in range(1, nombreDeEdificis):

                randomHeight = randint(0, alturaMaxima)
                randomXMin = randint(xmin, maxFinal)
                randomWidth = randint(1, ampladaMaxima)

                if randomHeight > 0:

                    firstSky += Skyline(randomXMin, randomHeight,
                                        randomXMin + randomWidth, asigna_atribs=False)

                    if randomHeight > self.__height:
                        self.__height = randomHeight

                # Optimización: cada 512 Skylines se hace un flatten con
                # los valores que tenga firstSky, esto facilita las siguientes uniones.
                if i & ((1 << 9) - 1) == 0:
                    firstSky.__intervalos, firstSky.__values = Skyline.__flatten(
                        firstSky.__intervalos, firstSky.__values)

            self.__intervalos, self.__values = Skyline.__flatten(
                firstSky.__intervalos, firstSky.__values)
            self.__color = firstSky.__color
            self.__area = self.__calculaArea()

    # OVERLOADS DE LA CLASSE SKYLINE

    def __add__(self, other):
        """
        Overload de l'operació add de la classe Skyline.
        """
        # Cas en el que es fa una unió
        if isinstance(other, Skyline):
            arr2 = other.__intervalos
            val2 = other.__values
            intervalos, values = self.__union(arr2, val2)

            return Skyline(intervalos, values)

        # Cas en el que es fa un desplaçament positiu
        elif isinstance(other, int):
            intervalOff = self.__moveOffset(other)

            return Skyline(intervalOff, self.__values, color=self.__color)

    def __iadd__(self, other):
        """
        Overload de l'operació iadd de la classe Skyline.
        """
        # Aques overload es necessari per evitar calculs innecessaris quan
        # es fan unions que podien ser costoses, podem suposar que other és un Skyline.

        # Cas en el que es fa una unió
        if isinstance(other, Skyline):
            arr2 = other.__intervalos
            val2 = other.__values
            intervalos, values = self.__union(arr2, val2)

            return Skyline(intervalos, values, asigna_atribs=False)

    def __sub__(self, other):
        """
        Overload de l'operació sub de la classe Skyline.
        """
        # Cas en el que es fa un desplaçament negatiu
        if isinstance(other, int):
            intervalOff = self.__moveOffset(-other)

            return Skyline(intervalOff, self.__values, color=self.__color)

    def __mul__(self, other):
        """
        Overload de l'operació mul de la classe Skyline.
        """

        # Cas en el que es fa una intersecció
        if isinstance(other, Skyline):
            arr2 = other.__intervalos
            val2 = other.__values

            intervalos, values = self.__intersection(arr2, val2)

            return Skyline(intervalos, values)
        # Cas en el que es fa una replicació
        elif isinstance(other, int):
            intervals, values = self.__replicate(other)
            return Skyline(intervals, values, color=self.__color)

    def __neg__(self):
        """
        Overload de l'operació neg de la classe Skyline.
        """
        # Cas en el que es fa una operació mirror
        intervals, values = self.__mirror()
        return Skyline(intervals, values, color=self.__color)

    # MÈTODES PRIVATS
    def __calculaArea(self):
        """
        Mètode privat que calcula l'àrea del Skyline.
        """
        area = 0
        intervalos = self.__intervalos
        values = self.__values

        for i in range(1, len(intervalos)):
            width = intervalos[i] - intervalos[i-1]
            height = values[i-1]

            area += width * height

        return area

    def __mirror(self):
        """
        Mètode que permet a un Skyline fer l'operació de mirror sobre ell mateix.
        Aquesta basicament consisteix en mantenir els intervals minims i màxims
        i girar els tamanys dels edificis.
        """
        intervalsDistance = []
        reversedValues = self.__values[:-1]
        reversedValues.reverse()
        reversedValues.append(0)

        i = 1

        while i < len(self.__intervalos):
            intervalsDistance.append(
                self.__intervalos[i] - self.__intervalos[i-1])
            i += 1

        lastValueInInterval = self.__intervalos[0]
        finalIntervals = [lastValueInInterval]

        i = len(intervalsDistance) - 1

        while i >= 0:
            lastValueInInterval += intervalsDistance[i]
            finalIntervals.append(lastValueInInterval)
            i -= 1

        return finalIntervals, reversedValues

    def __moveOffset(self, offset):
        """
        Mètode que permet al Skyline fer l'operació de desplaçament donat un offset.
        Basicament consisteix en moure tots els intervals amb l'offset donat.
        """
        intervals = [x + offset for x in self.__intervalos]

        return intervals

    def __replicate(self, rep):
        """
        Mètode que permet al Skyline fer l'operació de replicació donat un nombre de repeticions.
        Afegeix als intervals donats replicacions rep vegades de la mateixa forma a la dreta, i 
        multiplica la llista de values per rep replicant-la.
        """
        # Si el Skyline es buit
        if rep == 0:
            return [0, 1], [0, 0]

        distance = self.__intervalos[-1] - self.__intervalos[0]
        intervalsToAppend = self.__intervalos[1:]
        valuesToReplicate = self.__values[:-1]

        finalIntervals = self.__intervalos

        i = 1

        while i < rep:
            intervalsToAppend = [x + distance for x in intervalsToAppend]
            finalIntervals.extend(intervalsToAppend)
            i += 1

        valuesToReplicate = valuesToReplicate * rep
        valuesToReplicate.append(0)
        return finalIntervals, valuesToReplicate

    def __union(self, arr2, val2):
        """
        Mètode que permet al Skyline fer l'operació d'unió amb un altre Skyline.
        """
        index1 = 0
        arr1 = self.__intervalos
        val1 = self.__values

        # Si alguno de los Skylines es vacio, retorna el otro Skyline, si los dos lo son, da igual el que se retorne.
        if val1[0] == 0:
            return arr2, val2
        elif val2[0] == 0:
            return arr1, val1

        # La lista de intervalos y valores a devolver
        intervals = []
        values = []

        # Comprobador de si se entra en el siguiente bucle
        overlapped = False
        # Si tienen los mismos intervalos iniciales, estos se unifican con el value mas alto de los dos.
        while index1 < len(arr1) and index1 < len(arr2) and arr1[index1] == arr2[index1]:
            overlapped = True
            values.append(max(val1[index1], val2[index1]))
            intervals.append(arr1[index1])

            index1 += 1

        # Esto asegura que el siguiente elemento de arr1 a
        # analizar sea más pequeño que el siguiente que tenga arr2
        if index1 < len(arr1) and index1 < len(arr2):

            if arr2[index1] < arr1[index1]:

                arr1, arr2 = arr2, arr1
                val1, val2 = val2, val1

        index2 = index1

        # Si el indice no sobresale de arr2
        if index2 < len(arr2):
            # Busca donde iria en arr1 el valor de arr2[index2]
            posLittleArr2inArr1 = Skyline.__binary_search(arr1, arr2[index2])

            # Si la posición encontrada es mayor que la lista arr1
            if posLittleArr2inArr1 == len(arr1):
                # Añade los intervalos de arr1 a la lista de intervalos resultantes.
                intervals.extend(arr1[index1:posLittleArr2inArr1])

                # Si el valor que tiene val2[index2-1] es 0, y por lo tanto no hay
                # edificio en el intervalo que habría entre arr1[index1] y arr2[index2] por parte de arr2,
                # simplemente extiende los valores de val1 sobre la lista final de valores.
                if val2[index2-1] == 0:
                    values.extend(val1[index1:posLittleArr2inArr1-1])

                # En caso contrario, al extenderla, se tiene que tener en cuenta
                # cual es el valor de val2[index2-1] al extender la lista
                else:
                    while index1 < posLittleArr2inArr1-1:

                        if val2[index2-1] > val1[index1]:
                            values.append(val2[index2-1])
                        else:
                            values.append(val1[index1])
                        index1 += 1

                # Si no se entro en el primer bucle, no exite la posibilidad de que un
                # Skyline se sobreponga sobre el otro
                if not overlapped:
                    values.append(0)

                # Es posible que se sobrepongan
                else:
                    values.append(val2[index2-1])

            # Si no es así
            else:
                # Añade los intervalos de arr1 a la lista de intervalos resultantes.
                intervals.extend(arr1[index1:posLittleArr2inArr1])

                # Si el valor que tiene val2[index2-1] es 0, y por lo tanto no hay
                # edificio en el intervalo que habría entre arr1[index1] y arr2[index2] por parte de arr2,
                # simplemente extiende los valores de val1 sobre la lista final de valores.
                if val2[index2-1] == 0:
                    values.extend(val1[index1:posLittleArr2inArr1])

                # En caso contrario, al extenderla, se tiene que tener en cuenta
                # cual es el valor de val2[index2-1] al extender la lista
                else:
                    while index1 < posLittleArr2inArr1:

                        if val2[index2-1] > val1[index1]:
                            values.append(val2[index2-1])
                        else:
                            values.append(val1[index1])
                        index1 += 1

            index1 = posLittleArr2inArr1
        # El objetivo principal de todo lo que se ha hecho anteriormente es
        # utilizar una unica funcion extend en vez de varios appends si es posible,
        # eso aumenta muchisimo la eficiencia de la operacion en Skylines grandes
        # en los que se les une un unico edificio.

        # Bucle principal
        while index1 < len(arr1) and index2 < len(arr2):

            if arr1[index1] > arr2[index2]:

                intervals.append(arr2[index2])
                # Agrega el value mayor entre val1[index1 - 1] y val2[index2] a la
                # lista de valores final ya que se pueden estar solapando.
                if val1[index1 - 1] < val2[index2]:
                    values.append(val2[index2])

                else:
                    values.append(val1[index1-1])

                index2 += 1

            elif arr1[index1] < arr2[index2]:

                intervals.append(arr1[index1])
                # Agrega el value mayor entre val1[index1] y val2[index2 -1] a la
                # lista de valores final ya que se pueden estar solapando.
                if val2[index2 - 1] > val1[index1]:
                    values.append(val2[index2 - 1])

                else:
                    values.append(val1[index1])

                index1 += 1

            # Si ambos intervalos son iguales
            elif arr1[index1] == arr2[index2]:
                # Se unifican con el valor máximo
                values.append(max(val1[index1], val2[index2]))
                intervals.append(arr1[index1])

                index1 += 1
                index2 += 1

        # Si quedan valores no visitados en alguna de las dos listas
        if index1 != len(arr1):
            intervals.extend(arr1[index1:])
            values.extend(val1[index1:-1])

        elif index2 != len(arr2):
            intervals.extend(arr2[index2:])
            values.extend(val2[index2:-1])

        # Si por algun motivo ha faltado añadir el último valor 0 en la lista de valores:
        if len(values) == len(intervals)-1:
            values.append(0)

        return intervals, values

    def __intersection(self, arr2, val2):
        """
        Mètode que permet al Skyline fer l'operació de intersecció amb un altre Skyline.
        """
        index1 = 0

        arr1 = self.__intervalos
        val1 = self.__values

        # La lista de intervalos y valores a devolver
        intervals = []
        values = []

        # Si tienen los mismos intervalos iniciales, estos se unifican con el value mas bajo de los dos.
        while index1 < len(arr1) and index1 < len(arr2) and arr1[index1] == arr2[index1]:

            values.append(min(val1[index1], val2[index1]))
            intervals.append(arr1[index1])

            index1 += 1

        # Esto asegura que el siguiente elemento de arr1 a
        # analizar sea más pequeño que el siguiente que tenga arr2
        if index1 < len(arr1) and index1 < len(arr2):

            if arr2[index1] < arr1[index1]:

                arr1, arr2 = arr2, arr1
                val1, val2 = val2, val1

        index2 = index1

        # Bucle principal
        while index1 != len(arr1) and index2 != len(arr2):

            if arr1[index1] > arr2[index2]:

                intervals.append(arr2[index2])
                # Coges el value minimo de los dos posibles
                # entre val1[index1 - 1] y val2[index2]
                if val1[index1 - 1] > val2[index2]:

                    values.append(val2[index2])
                else:
                    values.append(val1[index1-1])
                index2 = index2 + 1

            elif arr1[index1] < arr2[index2]:

                intervals.append(arr1[index1])
                # Coges el value minimo de los dos posibles
                # entre val1[index1] y val2[index2 - 1]
                if val2[index2 - 1] < val1[index1]:
                    values.append(val2[index2 - 1])
                else:
                    values.append(val1[index1])

                index1 = index1 + 1

            # Si ambos intervalos son iguales
            elif arr1[index1] == arr2[index2]:
                # Se unifican con el valor mínimo

                values.append(min(val1[index1], val2[index2]))
                intervals.append(arr1[index1])

                index1 = index1 + 1
                index2 = index2 + 1

        if len(values) == len(intervals)-1:
            values.append(0)

        # 'Aplana' los resultados quitando valores innecesarios
        flattenedIntervals, flattenedValues = Skyline.__flatten(
            intervals, values)

        # Quita aquellos valores iniciales vacios innecesarios
        while len(flattenedValues) > 0 and flattenedValues[0] == 0:
            flattenedIntervals.pop(0)
            flattenedValues.pop(0)

        # Si el resultado final de la operación es vacio, devuelve
        # una representación simple de un Skyline vacio
        if len(flattenedValues) == 0:
            return [0, 1], [0, 0]

        return flattenedIntervals, flattenedValues

    # MÈTODES PÚBLICS
    def get_area(self):
        """
        Mètode getter de l'atribut àrea.
        """
        return self.__area

    def get_height(self):
        """
        Mètode getter de l'atribut height.
        """
        return self.__height

    def saveImage(self):
        """
        Mètode que permet al Skyline guardar una imatge de la seva representació.
        """
        plt.hist(self.__intervalos, bins=self.__intervalos,
                 weights=self.__values, color=self.__color)

        pathOfImage = "img.png"
        plt.savefig(pathOfImage)

        plt.clf()
        return pathOfImage

    # MÈTODES PRIVATS ESTÀTICS
    @staticmethod
    def __binary_search(list, val):
        """
        Funció que busca el valor val a la llista list i retorna on està, si no hi és, retorna la posició on hauria d'estar.
        """
        low = 0
        high = len(list)
        while low < high:
            mid = (low+high)//2

            if list[mid] < val:
                low = mid+1
            else:
                high = mid
        return low

    @staticmethod
    def __flatten(intervals, values):
        """
        Funció que \'aplana\' les dues llistes donades treient valors que es puguin considerar redundants i simplificant-les.
        """
        flattenedIntervals = []
        flattenedIntervals.append(intervals[0])
        flattenedValues = []

        lastVal = values[0]

        for i in range(1, len(intervals)):
            if i == len(intervals):
                flattenedIntervals.append(intervals[i])
                flattenedValues.append(lastVal)

            if values[i] != lastVal:
                flattenedIntervals.append(intervals[i])
                flattenedValues.append(lastVal)

                lastVal = values[i]

        flattenedValues.append(0)

        return flattenedIntervals, flattenedValues
