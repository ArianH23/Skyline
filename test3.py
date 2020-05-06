import matplotlib.pyplot as plt
import sys

# arr1 = [1, 3, 4, 5, 6, 7]
# val1 =   [6, 3, 0, 3, 6, 0]

# arr2 = [3, 7, 8]
# val2 =   [5, 10 ,0]

arr1 = [0, 1, 3, 5, 7]
val1 =   [1, 6, 0, 2, 0]

arr2 = [0, 2, 4, 6, 8]
val2 =   [1, 2, 6, 5, 0]

i1 = 0
i2 = 0

intervals = []
values = []

plt.hist(arr1, bins=arr1, weights=val1)
plt.ylim(0,10)
plt.xlim(0,8)
pathOfImage = "plot1.png"
plt.savefig(pathOfImage)
# plt.show()
plt.clf()

plt.hist(arr2, bins=arr2, weights=val2)
plt.ylim(0,10)
plt.xlim(0,8)

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

index1 = 0
index2 = 0

# if arr1[index1] <arr2[index2]:
#     arr1.

usoArr1 = False
def foo(index1, index2):

    while index1 != (arr1.__len__()) and index2 != arr2.__len__():
        print (arr1[index1:])
        print (arr2[index2:])
        print ("\n")
        print (intervals)
        print (values)
        input(input('? '))


        if arr1[index1] > arr2[index2]:
            intervals.append(arr2[index2])
            if val1[index1 - 1] < val2[index2]:

                values.append(val2[index2-1])
            else:
                values.append(val1[index1-1])
            index2 = index2 + 1
        
        elif arr1[index1] < arr2[index2]:

            intervals.append(arr1[index1])
            if val2[index2 - 1] > val1[index1-1]:
                values.append(val2[index2 - 1])
            else:
                values.append(val1[index1 - 1])
            index1 = index1 + 1

        elif arr1[index1] == arr2[index2]:

            values.append(max(val1[index1], val2[index2]))
            intervals.append(arr1[index1])

            index1 = index1 + 1
            index2 = index2 + 1

    return index1, index2

# while index1 != (val1.__len__()) and index2 != (val2.__len__()):

while arr1[index1] == arr2[index2]:

    values.append(max(val1[index1], val2[index2]))
    intervals.append(arr1[index1])

    index1 = index1 + 1
    index2 = index2 + 1

if arr1[index1] < arr2[index2]:
    intervals.append(arr1[index1])
    # values.append(val1[index1])
    index1 = index1 + 1
    index1, index2 = foo(index1, index2)

print (str(index1) +" " + str(index2))

if index1 != arr1.__len__() :
    intervals = intervals + arr1[index1:]
    values = values + arr1[index1-1:-1]

elif index2 != arr2.__len__():
    intervals = intervals + arr2[index2:]
    values = values + val2[index2-1:-1]
            

def posIntermedia(x, arr):
    
    if x < arr[0]: return True, -1

    for i in range (arr.__len__()):
        if x > arr[i]: return True,i
    
    return False, 0
    # elif intervals[]  

# if i1 != val1.__len__() :
#     intervals = intervals + arr1[i1:]
#     values = values + val1[i1:-1]

# elif i2 != val2.__len__():
#     intervals = intervals + arr2[i2:]
#     values = values + val2[i2:-1]

values.append(0)

print (intervals)
print (values)

plt.hist(intervals, bins=intervals, weights=values)
plt.ylim(0,10)
plt.xlim(0,8)
pathOfImage = "plot3.png"
plt.savefig(pathOfImage)
# plt.show()