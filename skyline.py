from matplotlib import pyplot as plt
from random import randint, random


class Skyline:

    def __init__(self, interval1, heights, interval2=None, xmin=None, xmax=None, color=None, type=None, asigna_atribs=True):
        """
        Mètode creador de la classe Skyline.
        """

        # Creació de Skyline simple
        if type == None:
            if interval2 is None:
                self.__intervalos = interval1
                self.__values = heights

            else:
                self.__intervalos = [interval1, interval2]
                self.__values = [heights] + [0]

            if color == None:
                # Avoid creating a white Skyline which would not be seen in the plot.
                red = min(0.85, random())
                green = min(0.85, random())
                blue = min(0.85, random())

                self.__color = (red, green, blue)
            else:
                self.__color = color

            if asigna_atribs == True:
                self.__area = self.__calculaArea()
                self.__height = max(self.__values)
                self.__intervalos, self.__values = flatten(
                    self.__intervalos, self.__values)

        # Creació de Skyline compost
        elif type == "complex":
            firstSky = Skyline(interval1[0], interval1[1], interval1[2])

            self.__height = interval1[1]

            for i in range(1, len(interval1) // 3):
                if interval1[(i*3)+1] > 0:
                    firstSky += Skyline(interval1[i*3],
                                        interval1[(i*3)+1], interval1[(i*3)+2])

                if interval1[(i*3)+1] > self.__height:
                    self.__height = interval1[(i*3)+1]

            self.intervalos, self.values = flatten(
                firstSky.__intervalos, firstSky.__values)

            self.__color = firstSky.__color
            self.__area = self.__calculaArea()

        # Creació de Skyline aleatori
        elif type == "random":
            maxFinal = xmax-interval2

            randomWidth = randint(1, interval2)
            randomHeight = randint(1, heights)
            randomXMin = randint(xmin, maxFinal)

            firstSky = Skyline(randomXMin, randomHeight,
                               randomXMin + randomWidth)

            self.__height = randomHeight
            # print (firstSky.intervalos)
            # print(firstSky.values)
            for i in range(1, interval1):
                # print(i)
                # print("randoming")
                randomHeight = randint(0, heights)
                randomXMin = randint(xmin, maxFinal)
                randomWidth = randint(1, interval2)
                # print(type(randomHeight))
                # print(str(randomXMin) + " " +str(randomHeight) +  " " + str(randomXMin +randomWidth))
                if randomHeight > 0:
                    newSky = Skyline(randomXMin, randomHeight,
                                     randomXMin + randomWidth, asigna_atribs=False)
                    firstSky += newSky

                    if randomHeight > self.__height:
                        self.__height = randomHeight
                # print(firstSky.values)
                # # input()
                # print (firstSky.intervalos)
                # print(firstSky.values)

            self.intervalos, self.values = flatten(
                firstSky.__intervalos, firstSky.__values)
            self.__color = firstSky.__color
            self.__area = self.__calculaArea()

    def __calculaArea(self):
        """
        Mètode que calcula l'àrea del Skyline.
        """
        area = 0
        intervalos = self.__intervalos
        values = self.__values

        for i in range(1, len(intervalos)):
            width = intervalos[i] - intervalos[i-1]
            height = values[i-1]

            area += width * height

        return area

    def __add__(self, other):
        """
        Overload de l'operació add de la classe Skyline.
        """
        if isinstance(other, Skyline):
            arr2 = other.__intervalos
            val2 = other.__values
            intervalos, values = self.union(arr2, val2)

            return Skyline(intervalos, values)

        elif isinstance(other, int):
            intervalOff = self.moveOffset(other)

            return Skyline(intervalOff, self.__values, color=self.__color)

    def __iadd__(self, other):
        """
        Overload de l'operació iadd de la classe Skyline.
        """
        if isinstance(other, Skyline):
            arr2 = other.__intervalos
            val2 = other.__values
            intervalos, values = self.union(arr2, val2)

            return Skyline(intervalos, values, asigna_atribs=False)

    def __sub__(self, other):
        """
        Overload de l'operació sub de la classe Skyline.
        """
        if isinstance(other, int):
            intervalOff = self.moveOffset(-other)

            return Skyline(intervalOff, self.__values, color=self.__color)

    def __mul__(self, other):
        """
        Overload de l'operació mul de la classe Skyline.
        """
        if isinstance(other, Skyline):
            arr2 = other.__intervalos
            val2 = other.__values

            intervalos, values = self.intersection(arr2, val2)

            return Skyline(intervalos, values)

        elif isinstance(other, int):
            intervals, values = self.replicate(other)
            return Skyline(intervals, values, color=self.__color)

    def __neg__(self):
        """
        Overload de l'operació neg de la classe Skyline.
        """
        intervals, values = self.mirror()
        return Skyline(intervals, values, color=self.__color)

    def mirror(self):
        """Mètode que permet a un Skyline fer l'operació de mirror sobre ell mateix."""
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

    def moveOffset(self, offset):
        intervals = [x + offset for x in self.__intervalos]

        return intervals

    def replicate(self, rep):
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

    def saveImage(self):
        plt.hist(self.__intervalos, bins=self.__intervalos,
                 weights=self.__values, color=self.__color)

        # Necessary to plot only integer values in the axis
        # # self.xyints()

        # plt.show()
        pathOfImage = "img.png"
        plt.savefig(pathOfImage)
        # self.color = plt.get_color()
        plt.clf()
        return pathOfImage

    def xyints(self):
        """
        Hace que los valores en los ejes X e Y
        del plot actual sean enteros y no floats
        """
        yint = []
        locs, labels = plt.yticks()
        for each in locs:
            yint.append(int(each))
        plt.yticks(yint)

        xint = []
        locs, labels = plt.xticks()
        for each in locs:
            xint.append(int(each))
        plt.xticks(xint)

    def union(self, arr2, val2):
        index1 = 0
        arr1 = self.__intervalos
        val1 = self.__values

        # Si algun dels Skylines és buit, retorna l'altre Skyline.
        if val1[0] == 0:
            return arr2, val2
        elif val2[0] == 0:
            return arr1, val1

        intervals = []
        values = []
        overlapped = False
        while index1 < len(arr1) and index1 < len(arr2) and arr1[index1] == arr2[index1]:
            overlapped = True
            values.append(max(val1[index1], val2[index1]))
            intervals.append(arr1[index1])

            index1 += 1
            # index2 += 1
        # For the whole operation to work, the program has to take the
        # array with the first smallest value as a "reference" to check
        # the values of the other array, this conditional makes sure that
        # arr1 is the array which has the smallest first value
        if index1 < len(arr1) and index1 < len(arr2):
            if arr2[index1] < arr1[index1]:
                arr1, arr2 = arr2, arr1
                # index1, index2 = index2, index1
                val1, val2 = val2, val1

        index2 = index1

        if index2 < len(arr2):
            posLittleArr2inArr1 = binary_search(arr1, arr2[index2])

            # The smallest number of arr2 is bigger than the largest in arr1
            if posLittleArr2inArr1 == len(arr1):
                intervals.extend(arr1[index1:posLittleArr2inArr1])
                values.extend(val1[index1:posLittleArr2inArr1-1])

                if not overlapped:
                    values.append(0)
                    # print("adding")
                else:
                    values.append(val2[index2-1])
            # else
            else:
                intervals.extend(arr1[index1:posLittleArr2inArr1])

                if val2[index2-1] == 0:
                    values.extend(val1[index1:posLittleArr2inArr1])

                else:
                    while index1 < posLittleArr2inArr1:
                        # print(index1)

                        if val2[index2-1] > val1[index1]:
                            values.append(val2[index2-1])
                        else:
                            values.append(val1[index1])
                        index1 += 1
                        # values.extend(val1[index1:posLittleArr2inArr1])
            index1 = posLittleArr2inArr1

        while index1 < len(arr1) and index2 < len(arr2):
            # print("inside big loop")
            # firstn = time.time()*100000000
            # print()
            if arr1[index1] > arr2[index2]:
                intervals.append(arr2[index2])
                if val1[index1 - 1] < val2[index2]:

                    values.append(val2[index2])
                else:
                    values.append(val1[index1-1])
                index2 += 1

            elif arr1[index1] < arr2[index2]:

                intervals.append(arr1[index1])
                # "if index2 > 0" It is not necessary to check this conditions, since if
                # index2 == 0 then index2-1 == -1 and the elem at post -1 of val2 is 0
                # which is the neutral value of the whole operation
                if val2[index2 - 1] > val1[index1]:
                    values.append(val2[index2 - 1])
                else:
                    values.append(val1[index1])

                index1 += 1

            elif arr1[index1] == arr2[index2]:

                values.append(max(val1[index1], val2[index2]))
                intervals.append(arr1[index1])

                index1 += 1
                index2 += 1

        # print(val2)
        if index1 != len(arr1):
            intervals.extend(arr1[index1:])
            values.extend(val1[index1:-1])

        elif index2 != len(arr2):
            intervals.extend(arr2[index2:])
            values.extend(val2[index2:-1])
            # print("extending")

        if len(values) == len(intervals)-1:
            values.append(0)

        return intervals, values

    def intersection(self, arr2, val2):
        index1 = 0
        index2 = 0
        arr1 = self.__intervalos
        val1 = self.__values

        intervals = []
        values = []

        while index1 < len(arr1) and index2 < len(arr2) and arr1[index1] == arr2[index2]:

            values.append(min(val1[index1], val2[index2]))
            intervals.append(arr1[index1])

            index1 = index1 + 1
            index2 = index2 + 1

        if index1 < len(arr1) and index2 < len(arr2):
            if arr2[index2] < arr1[index1]:
                arr1, arr2 = arr2, arr1
                index1, index2 = index2, index1
                val1, val2 = val2, val1

        while index1 != len(arr1) and index2 != len(arr2):

            if arr1[index1] > arr2[index2]:
                intervals.append(arr2[index2])
                if val1[index1 - 1] > val2[index2]:

                    values.append(val2[index2])
                else:
                    values.append(val1[index1-1])
                index2 = index2 + 1

            elif arr1[index1] < arr2[index2]:

                intervals.append(arr1[index1])
                # "if index2 > 0" It is not necessary to check this conditions, since if
                # index2 == 0 then index2-1 == -1 and the elem at post -1 of val2 is 0
                # which is the neutral value of the whole operation
                if val2[index2 - 1] < val1[index1]:
                    values.append(val2[index2 - 1])
                else:
                    values.append(val1[index1])

                index1 = index1 + 1

            elif arr1[index1] == arr2[index2]:

                values.append(min(val1[index1], val2[index2]))
                intervals.append(arr1[index1])

                index1 = index1 + 1
                index2 = index2 + 1

        if len(values) == len(intervals)-1:
            values.append(0)
        print(intervals)
        print(values)
        flattenedIntervals, flattenedValues = flatten(intervals, values)
        print()
        print(flattenedIntervals)
        print(flattenedValues)

        while len(flattenedValues) > 0 and flattenedValues[0] == 0:
            flattenedIntervals.pop(0)
            flattenedValues.pop(0)

        if len(flattenedValues) == 0:
            return [0, 1], [0, 0]

        return flattenedIntervals, flattenedValues

    def get_area(self):
        """
        Mètode getter de l'atribut àrea
        """
        return self.__area

    def get_height(self):
        """
        Mètode getter de l'atribut height
        """
        return self.__height


def binary_search(list, val):
    low = 0
    high = len(list)
    while low < high:
        mid = (low+high)//2

        if list[mid] < val:
            low = mid+1
        else:
            high = mid
    return low


def flatten(intervals, values):
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
