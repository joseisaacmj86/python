#listas: son parecidas a los arreglos pero permite operaciones mas complejas

my_list1 = list()
my_list2 = []


my_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_list1)

my_list2 = [1, 2, 3, "hsg", "hsg2"]
print(my_list2)

print(type(my_list1))
print(type(my_list2))

#acceder a listas
print(my_list1[0])
print(my_list1[1])
print(my_list1[-1])
print(my_list1[-4])

my_list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_list3.pop())
print(my_list3)
