import matplotlib.pyplot as plt
arr1 = [0, 2, 3, 4, 7]
val1 =   [5, 2 ,4, 6, 0]

arr2 = [0, 2, 3, 7]
val2 =   [7, 6, 5, 0]

i1 = 0
i2 = 0

# j1 = 0
# j2 = 1

intervals = []
values = []

plt.hist(arr1, bins=arr1, weights=val1)
plt.show()
plt.clf()

plt.hist(arr2, bins=arr2, weights=val2)
plt.show()
plt.clf()

if(arr1[0] < arr2[0]):
    i1 = 1
    i2 = 0
    intervals.append(arr1[0])
    values.append(val1[0])


elif (arr1[0] > arr2[0]):
    i1 = 0
    i2 = 1
    intervals.append(arr2[0])
    values.append(val2[0])

else:
    i1 = i2 = 1
    intervals.append(arr1[0])
    values.append(max(arr1[0], arr2[0]))

# print (min((arr1[0], arr2[0])))
print (intervals)

while i1 != val1.__len__ and i2 != val2.__len__():
    if arr1[i1] == arr2[i2]:

        values.append(max(val1[i1], val2[i2]))
        i1 = i1 + 1
        i2 = i2 + 1
        

    # elif intervals[]


    i1 = i1+1
    