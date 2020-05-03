from matplotlib import pyplot as plt
import random

class Skyline:

    def __init__(self, id, container, values):
        self.id = id
        self.intervalos = container
        self.values = [values] +[0]
        self.color = (random.random(), random.random(), random.random())

    def saveImage(self):
        plt.hist(self.intervalos, bins=self.intervalos, weights=self.values,color=self.color)

        #Necessary to plot only integer values in the axis
        # # # # # self.xyints()

        # plt.show()
        pathOfImage = "plot.png"
        plt.savefig(pathOfImage)
        # self.color = plt.get_color()
        plt.clf()
        return pathOfImage

    def xyints(self):
        """
        Hace que los valores en los ejes X e Y del plot actual sean enteros y no floats
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