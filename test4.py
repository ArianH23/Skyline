import matplotlib.pyplot as plt
import sys


# arr2 = [-8,-3,-2, 1, 3, 4, 5, 6, 7]
# val2 =   [14,2,5, 6, 3, 0, 3, 6, 0]

# arr1 = [3, 7]
# val1 =   [5,0]

arr1 = [-7,-2, 0, 1, 3, 5, 7]
val1 =   [3,9,1, 6, 0, 2, 0]

arr2 = [-9,-3,0, 2, 4, 6, 8]
val2 =   [2,4,1, 2, 6, 5, 0]

i1 = 0
i2 = 0


plt.hist(arr1, bins=arr1, weights=val1)
plt.ylim(0,15)
plt.xlim(-10,10)
pathOfImage = "plot1.png"
plt.savefig(pathOfImage)
# plt.show()
plt.clf()

plt.hist(arr2, bins=arr2, weights=val2)
plt.ylim(0,15)
plt.xlim(-10,10)

pathOfImage = "plot2.png"
plt.savefig(pathOfImage)
# plt.show()
plt.clf()
# interArr11 = arr1[0]
# interArr12 = arr1[1]

# interArr21 = arr2[0]
# interArr22 = arr2[1]

# mayorInterval = 0

# ultimoValor1 = val1[0]
# ultimoValor2 = val2[0]

# if arr1[0] == arr2[0]:
#     intervals.append(arr1[0])

# if arr1[0] < arr2[0]:
#     intervals.append(arr1[0])

# if arr1[0] > arr2[0]:
#     intervals.append(arr2[0])


# if arr1[index1] <arr2[index2]:
#     arr1.

def foo():
    index1 = 0
    index2 = 0

    
    arr1 = [-7,-2, 0, 1, 3, 5, 7]
    val1 =   [3,9,1, 6, 0, 2, 0]

    arr2 = [-9,-3,0, 2, 4, 6, 8]
    val2 =   [2,4,1, 2, 6, 5, 0]

    intervals = []
    values = []

    while  index1 < arr1.__len__() and index2 < arr2.__len__() and arr1[index1] == arr2[index2]:

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

            # else:
            #     values.append(val1[index1])

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

    for i in range (1, intervals.__len__()):
        if i == intervals.__len__():
            flattenedIntervals.append(intervals[i])
            flattenedValues.append(lastVal)

        if values[i] != lastVal:
            flattenedIntervals.append(intervals[i])
            flattenedValues.append(lastVal)

            lastVal = values[i]

    flattenedValues.append(0)

    return flattenedIntervals, flattenedValues

# while index1 != (val1.__len__()) and index2 != (val2.__len__()):

# while  index1 < arr1.__len__() and index2 < arr2.__len__() and arr1[index1] == arr2[index2]:
#     print (index1)
#     print (index2)
#     print ()
#     values.append(max(val1[index1], val2[index2]))
#     intervals.append(arr1[index1])

#     index1 = index1 + 1
#     index2 = index2 + 1


# if index1 < arr1.__len__() and index2 < arr2.__len__() and arr1[index1] < arr2[index2]:
    
#     index1, index2 = foo(index1, index2)

# print (str(index1) +" " + str(index2))

# if index1 != arr1.__len__() :
#     intervals = intervals + arr1[index1:]
#     values = values + arr1[index1:-1]

# elif index2 != arr2.__len__():
#     intervals = intervals + arr2[index2:]
#     values = values + val2[index2:-1]
            

# if values.__len__() == intervals.__len__()-1:
#     values.append(0)
intervals, values = foo()

print (intervals)
print (values)

plt.hist(intervals, bins=intervals, weights=values)
plt.ylim(0,15)
plt.xlim(-10,10)
pathOfImage = "plot3.png"
plt.savefig(pathOfImage)
# plt.show()