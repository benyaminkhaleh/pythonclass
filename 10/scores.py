names = ['ali','majid','reza','amir','mohammad','akbar']
score = [20 , 19 , 18 , 15 , 10 , 8]
Student_grades = {}
i = 0
for name in names :
    Student_grades[str(name)] = score[i]
    i += 1
print(Student_grades)