grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
#print((sum(grades[0]))/(len(grades[0])))
#students = list(students)
#print(students)
#print(type(students))
students = sorted(students)
#print(students)
f= [(sum(grades[0]))/(len(grades[0])),(sum(grades[1]))/(len(grades[0])),(sum(grades[2]))/(len(grades[0])),(sum(grades[3]))/(len(grades[0])),(sum(grades[4]))/(len(grades[0]))]
#print(f)
g = {students[0]:f[0], students[1]:f[1],students[2]:f[2], students[3]:f[3], students[4]:f[4]}
print(g)