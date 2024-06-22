number1 = int(input('Введите число от 3 до 20:'))
name = []
for i in range(1, 20):
    for j in range(1, 20):
        if number1 % (i+j) == 0 and i != j and i < j:
            name.append(i)
            name.append(j)
print('Пароль:', *name)

