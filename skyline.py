from matplotlib import pyplot as plt
import random
from random import randint
import time

class Skyline:

    def __init__(self, interval1, heights, interval2=None, xmin=None, xmax=None, color=None, type=None):

        if type == "random":
            maxFinal = xmax-interval2
            randomWidth = randint(1,interval2)
            randomHeight = randint(1,heights)
            randomXMin = randint(xmin,maxFinal)
            firstSky = Skyline(randomXMin,randomHeight,randomXMin + randomWidth)

            # print (firstSky.intervalos)
            # print(firstSky.values)
            for i in range (1,interval1):
                # print(i)
                # print("randoming")
                randomHeight = randint(1,heights)
                randomXMin = randint(xmin,maxFinal)
                randomWidth = randint(1,interval2)
                # print(type(randomHeight))
                # print(str(randomXMin) + " " +str(randomHeight) +  " " + str(randomXMin +randomWidth))
                newSky = Skyline(randomXMin,randomHeight,randomXMin + randomWidth)
                firstSky = firstSky + newSky
                # print(firstSky.values)
                # # input()
                # print (firstSky.intervalos)
                # print(firstSky.values)

            self.intervalos = firstSky.intervalos
            self.values = firstSky.values
            self.color = firstSky.color

        else:
            if interval2 is None:
                self.intervalos = interval1
                self.values = heights

            else:
                self.intervalos = [interval1, interval2]
                self.values = [heights] + [0]

            if color == None:
                self.color = (random.random(), random.random(), random.random())
            else:
                self.color = color

    def __add__(self, other):
        if isinstance(other, Skyline):
            arr2 = other.intervalos
            val2 = other.values
            intervalos, values = self.union(arr2, val2)

            return Skyline(intervalos, values)

        elif isinstance(other, int):
            intervalOff = self.moveOffset(other)

            return Skyline(intervalOff, self.values)

    def __sub__(self, other):
        if isinstance(other, int):
            intervalOff = self.moveOffset(-other)

            return Skyline(intervalOff, self.values)

    def __mul__(self, other):
        if isinstance(other, Skyline):
            arr2 = other.intervalos
            val2 = other.values

            intervalos, values = self.intersection(arr2, val2)

            return Skyline(intervalos, values)

        elif isinstance(other, int):
            intervals, values = self.replicate(other)
            return Skyline(intervals, values, color=self.color)

    def __neg__(self):
        intervals, values = self.mirror()
        return Skyline(intervals, values, color=self.color)

    def mirror(self):
        intervalsDistance = []
        reversedValues = self.values[:-1]
        reversedValues.reverse()
        reversedValues.append(0)

        i = 1

        while i < self.intervalos.__len__():
            intervalsDistance.append(self.intervalos[i] - self.intervalos[i-1])
            i += 1

        lastValueInInterval = self.intervalos[0]
        finalIntervals = [lastValueInInterval]

        i = intervalsDistance.__len__() - 1

        while i >= 0:
            lastValueInInterval += intervalsDistance[i]
            finalIntervals.append(lastValueInInterval)
            i -= 1

        return finalIntervals, reversedValues

    def moveOffset(self, offset):
        intervals = [x + offset for x in self.intervalos]

        return intervals

    def replicate(self, rep):
        distance = self.intervalos[-1] - self.intervalos[0]
        intervalsToAppend = self.intervalos[1:]
        valuesToReplicate = self.values[:-1]

        finalIntervals = self.intervalos

        i = 1

        while i < rep:
            intervalsToAppend = [x + distance for x in intervalsToAppend]
            finalIntervals = finalIntervals + intervalsToAppend
            i += 1

        valuesToReplicate = valuesToReplicate * rep
        valuesToReplicate.append(0)
        return finalIntervals, valuesToReplicate

    def saveImage(self):
        plt.hist(self.intervalos, bins=self.intervalos,
                 weights=self.values, color=self.color)

        # Necessary to plot only integer values in the axis
        # # # # # self.xyints()

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
        firsta = time.time()*100000000
        index1 = 0
        index2 = 0
        arr1 = self.intervalos
        val1 = self.values
        seconda = time.time()*100000000

        # print("asig: " + str(seconda-firsta))

        intervals = []
        values = []

        while index1 < arr1.__len__() and index2 < arr2.__len__() and arr1[index1] == arr2[index2]:

            values.append(max(val1[index1], val2[index2]))
            intervals.append(arr1[index1])

            index1 = index1 + 1
            index2 = index2 + 1
        # For the whole operation to work, the program has to take the
        # array with the first smallest value as a "reference" to check
        # the values of the other array, this conditional makes sure that
        # arr1 is the array which has the smallest first value
        if index1 < arr1.__len__() and index2 < arr2.__len__():
            if arr2[index2] < arr1[index1]:
                arr1, arr2 = arr2, arr1
                index1, index2 = index2, index1
                val1, val2 = val2, val1
        # print("im going")
        # print(arr1)
        # print(arr2)
        # print()
        # print(val1)
        # print(val2)
        # print ("arr1[0]: " + str(arr1[0]))
        # print ("arr2[0]: " + str(arr2[0]))

        first1 = time.time()*100000000

        # while arr1[index1] < arr2[index2] and index1!=arr1.__len__()-1:
        #     # print("we in")
        #     intervals.append(arr1[index1])
        #     values.append(val1[index1])
        #     index1 += 1
        second1 = time.time()*100000000
        if index2 < arr2.__len__():
            posLittleArr2inArr1 = bisect_left(arr1,arr2[index2])
            # print(posLittleArr2inArr1)
            intervals.extend(arr1[index1:posLittleArr2inArr1])
            values.extend(val1[index1:posLittleArr2inArr1])
            index1 = posLittleArr2inArr1

        # print("bsearch: " + str(second1-first1))
        first2 = time.time()*100000000
        # Iterating
        numite = 0
        while index1 < arr1.__len__() and index2 < arr2.__len__():
            # print("inside big loop")
            firstn = time.time()*100000000

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
            secondn = time.time()*100000000
            # print("tiempo ite: " + str(secondn-firstn))
            # print()
            numite += 1

        # print("numero de ites: " + str(numite))
        # second2 = time.time()*100000000
        # print("bucle2: " + str(second2-first2))
        # print()
        # print(intervals)
        # print(values)
        first3 = time.time()*100000000

        if index1 != arr1.__len__():
            intervals.extend(arr1[index1:])
            values.extend(val1[index1:-1])

        elif index2 != arr2.__len__():
            intervals.extend(arr2[index2:])
            values.extend(val2[index2:-1])

        if values.__len__() == intervals.__len__()-1:
            values.append(0)
        # second3 = time.time()*100000000
        # print("append: " + str(second3-first3))


        # For the intervals and values to look cleaner,
        # it is necessary some kind of flattening around the results.
        # We don't want consecutive intervals with the same values to appear more than once.


        # flattenedIntervals = []
        # flattenedIntervals.append(intervals[0])
        # flattenedValues = []

        # lastVal = values[0]

        # for i in range(1, intervals.__len__()):
        #     if i == intervals.__len__():
        #         flattenedIntervals.append(intervals[i])
        #         flattenedValues.append(lastVal)

        #     if values[i] != lastVal:
        #         flattenedIntervals.append(intervals[i])
        #         flattenedValues.append(lastVal)

        #         lastVal = values[i]

        # flattenedValues.append(0)
        # input()
        return intervals, values

    def intersection(self, arr2, val2):
        index1 = 0
        index2 = 0
        arr1 = self.intervalos
        val1 = self.values

        intervals = []
        values = []

        while index1 < arr1.__len__() and index2 < arr2.__len__() and arr1[index1] == arr2[index2]:

            values.append(min(val1[index1], val2[index2]))
            intervals.append(arr1[index1])

            index1 = index1 + 1
            index2 = index2 + 1

        if index1 < arr1.__len__() and index2 < arr2.__len__():
            if arr2[index2] < arr1[index1]:
                arr1, arr2 = arr2, arr1
                index1, index2 = index2, index1
                val1, val2 = val2, val1

        while index1 != arr1.__len__() and index2 != arr2.__len__():

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

        if values.__len__() == intervals.__len__()-1:
            values.append(0)

        flattenedIntervals = []
        flattenedIntervals.append(intervals[0])
        flattenedValues = []

        lastVal = values[0]

        for i in range(1, intervals.__len__()):
            if i == intervals.__len__():
                flattenedIntervals.append(intervals[i])
                flattenedValues.append(lastVal)

            if values[i] != lastVal:
                flattenedIntervals.append(intervals[i])
                flattenedValues.append(lastVal)

                lastVal = values[i]

        flattenedValues.append(0)

        while flattenedValues[0] == 0:
            flattenedIntervals.pop(0)
            flattenedValues.pop(0)

        return flattenedIntervals, flattenedValues

def bisect_left(a, x, lo=0, hi=None):
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        # Use __lt__ to match the logic in list.sort() and in heapq
        if a[mid] < x: lo = mid+1
        else: hi = mid
    return lo