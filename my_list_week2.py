my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)

my_list.insert(2, 15)
print(my_list)

my_list.extend([50, 60, 70])
print(my_list)

del my_list[-1]
print(my_list)

my_list.sort()
index = my_list.index(30)
print(my_list)

print("The index of the value 30 is:", index)