# # from matplotlib import pyplot as plt

# # x_axis = [1,2,3,4,5]

# # y_axis = [2,2,3,3,3]

# # plt.bar(x_axis, y_axis,color = "red", width=1)

# # plt.title("Hello")

# # plt.show()
# import matplotlib.pyplot as plt
# # plt.style.use('dark_background')
# w = 4
# h = 3
# d = 70
# # plt.figure(figsize=(w, h), dpi=d)


# #VALORES QUE HAY ENTRE CADA INTERVALO
# y = [1, 1, 2, 1, 5, 0, 50, 0]
# # auxy = y
# # for i in range(0,2):
# #     y = y+(auxy)
# # #-----------------------------------------------------------------------

# #INTERVALOS
# intervalos=[0, 1, 2, 3, 4,5,26,80]
# # lastOfX = listX[-1]+1

# # auxx = map(lambda x: x + lastOfX, listX) 

# # for i in range(2):
# #     listX = listX + list(auxx)
# #     semao = list(auxx)
# #     print("xd")
# #     print (semao)
# #     auxx = map(lambda x: x + lastOfX, semao) 
# #     print (list(auxx))

# # print (listX)
# # print (y)
# plt.hist(intervalos, bins=intervalos, weights=y)

# plt.show()