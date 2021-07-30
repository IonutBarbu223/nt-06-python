my_list=[7,8,9,2,3,1,4,10,5,6]
print(my_list)
copy_of_list = my_list.copy()
copy_of_list.sort()
print(copy_of_list)
copy_of_list.reverse()
print(copy_of_list)
my_sliced_par_list = copy_of_list[::2]
print(my_sliced_par_list)
my_sliced_impar_list = copy_of_list[1::2]
print(my_sliced_impar_list)
my_sliced_of_number_div_with3_list = copy_of_list[1:8:3]
print(my_sliced_of_number_div_with3_list)



