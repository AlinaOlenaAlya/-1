immutable_var = 1, True, 'Name', 1.2
print(immutable_var)
# кортеж это неизменяемый тип данных, если в кортеж засунуть список, то только данные в [] можно будет изменить
mutable_list = [1, 'ok', 1.2, True]
del mutable_list [0]
print(mutable_list)
mutable_list[-1]=False
print(mutable_list)
mutable_list = mutable_list + [1,'good']
print(mutable_list)
print(mutable_list[-1])