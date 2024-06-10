my_dict = {'home':136, 'floor':8,'flat':65}
print(my_dict)
print(my_dict['home'])
my_dict.update({'room':2, 'entrance':4})
print(my_dict)
a = my_dict.pop('room')
print(my_dict)
print(a)

my_set = {1,2,3,5,5,9,4}
print(my_set)
my_set.add(7)
my_set.add(8)
print(my_set)
my_set.discard(2)
print(my_set)
my_set.remove(1)
print(my_set)