from matplotlib import pyplot as plt
import random


class Skyline:

    def __init__(self, id, interval1, heights, interval2 = None):
        if interval2 is None:
            self.intervalos = interval1
            self.values = heights

        else:
            self.intervalos = [interval1, interval2]
            self.values = [heights] + [0]
        
        self.id = id
        self.color = (random.random(), random.random(), random.random())

    def saveImage(self):
        plt.hist(self.intervalos, bins=self.intervalos,
                 weights=self.values, color=self.color)

        # Necessary to plot only integer values in the axis
        # # # # # self.xyints()

        # plt.show()
        pathOfImage = "plotxd.png"
        plt.savefig(pathOfImage)
        # self.color = plt.get_color()
        print ("hi there")
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

    def __mul__(self, other):
        if isinstance(other, Skyline):
            arr1 = self.intervalos
            arr2 = other.intervalos

            val1 = self.values
            val2 = other.values

            index1 = 0
            index2 = 0

            intervalos, values = self.union(arr1, arr2, val1, val2)

            return Skyline("xd", intervalos, values)

    def union(self, arr1, arr2, val1, val2):
        index1 = 0
        index2 = 0

        intervals = []
        values = []

        while index1 < arr1.__len__() and index2 < arr2.__len__() and arr1[index1] == arr2[index2]:

            values.append(max(val1[index1], val2[index2]))
            intervals.append(arr1[index1])

            index1 = index1 + 1
            index2 = index2 + 1
        
        while index1 != arr1.__len__() and index2 != arr2.__len__():

            if arr1[index1] > arr2[index2]:
                intervals.append(arr2[index2])
                if val1[index1 - 1] < val2[index2]:

                    values.append(val2[index2])
                else:
                    values.append(val1[index1-1])
                index2 = index2 + 1

            elif arr1[index1] < arr2[index2]:

                intervals.append(arr1[index1])
                if val2[index2 - 1] > val1[index1]:
                    values.append(val2[index2 - 1])
                else:
                    values.append(val1[index1])
                index1 = index1 + 1

            elif arr1[index1] == arr2[index2]:

                values.append(max(val1[index1], val2[index2]))
                intervals.append(arr1[index1])

                index1 = index1 + 1
                index2 = index2 + 1

        if index1 != arr1.__len__():
            intervals = intervals + arr1[index1:]
            values = values + arr1[index1:-1]

        elif index2 != arr2.__len__():
            intervals = intervals + arr2[index2:]
            values = values + val2[index2:-1]

        if values.__len__() == intervals.__len__()-1:
            values.append(0)

        return intervals, values

    
