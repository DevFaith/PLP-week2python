# create empty list 
my_list = []

#Apppend elements to my_list
numbers = [10,20,30,40]

my_list.append(numbers)

print(my_list)

#second position inserted to my_list
my_list = [1,2,3,4]

my_list.insert(1,15)

print(my_list)

#extended list
my_list = [1,15,2,3,4]

extension_list = (50,60,70)

my_list.extend(extension_list)

print(my_list)

#Remove the last element fom my_list
my_list.pop()


#sort  my_list in assending order
my_list.sort()


#find and print the index value of 30 in my_list
index_60 = my_list.index(60)
print(f"The index of 30 in my_list is: {index_60}")

