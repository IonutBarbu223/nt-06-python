my_list=[7,8,9,2,3,1,4,10,5,6]
print(my_list)
list_1 = my_list.copy()
list_1.sort()
print(list_1)
list_1.reverse()
print(list_1)
my_skiced_list = list_1[::2]
print(my_skiced_list)
my_sliced_list2 = list_1[1::2]
print(my_sliced_list2)
my_sliced_list3 = list_1[1:8:3]
print(my_sliced_list3)



