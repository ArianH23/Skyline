import matplotlib.pyplot as plt
import sys

arr1 = [1, 3, 4, 5, 6, 7]
val1 =   [6, 3, 0, 3, 6, 0]

arr2 = [3, 7, 8]
val2 =   [5, 10 ,0]

i1 = 0
i2 = 0

# j1 = 0
# j2 = 1

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
mayorInterval = 0

usingArr1 = False

if(arr1[0] < arr2[0]):
    i1 = 1
    i2 = 0
    intervals.append(arr1[0])
    values.append(val1[0])
    mayorInterval = val1[0]
    usingArr1 = True

elif (arr1[0] > arr2[0]):
    i1 = 0
    i2 = 1
    intervals.append(arr2[0])
    values.append(val2[0])
    mayorInterval = val2[0]
    usingArr1 = False


else:
    i1 = i2 = 1
    intervals.append(arr1[0])
    values.append(max(val1[0], val2[0]))
    mayorInterval = max(val1[0], val2[0])
    usingArr1 = True


# print (min((arr1[0], arr2[0])))
print (intervals)

while i1 != (val1.__len__()) and i2 != (val2.__len__()):
    maxV = values[-1]

    print (arr1[i1:])
    print (arr2[i2:])
    print ()
    print (intervals)
    print (values)
    input(input('? '))

    if arr1[i1] == arr2[i2]:
        intervals.append(arr1[i1])
        values.append(max(val1[i1], val2[i2]))

        i1 = i1 + 1
        i2 = i2 + 1
        
    elif arr1[i1] < arr2[i1]:

        intervals.append(arr1[i1])
        values.append(val1[i1])
        i1 = i1 + 1
    
    elif arr1[i1] > arr2[i1]:
        intervals.append(arr2[i2])
        values.append(val2[i2])
        i2 = i2 + 1

    # elif intervals[]

if i1 != val1.__len__() :
    intervals = intervals + arr1[i1:]
    values = values + val1[i1:-1]

elif i2 != val2.__len__():
    intervals = intervals + arr2[i2:]
    values = values + val2[i2:-1]

values.append(0)

print (intervals)
print (values)

plt.hist(intervals, bins=intervals, weights=values)
plt.ylim(0,10)
plt.xlim(0,8)
pathOfImage = "plot3.png"
plt.savefig(pathOfImage)
# plt.show()