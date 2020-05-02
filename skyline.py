from matplotlib import pyplot as plt

class Skyline:

    def __init__(self, id, container, values):
        self.id = id
        self.intervalos = container
        self.values = [values] +[0]
        print ("creado")
        print (container)

    def show(self):
        print ("valores")
        print (self.values)
        print (self.intervalos)
        plt.hist(self.intervalos, bins=self.intervalos, weights=self.values)

        #Necessary to plot only integer values in the axis
        self.xyints()

        # plt.show()
        plt.savefig('plot.png')

    def xyints(self):
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