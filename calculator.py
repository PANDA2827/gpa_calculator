import math

number_sub = int(input("Number of Subjects: "))

data = []

for i in range(number_sub):
    sub_score = int(input("Score of Subjects {}: ".format(i+1)))
    data.append(sub_score)
    
grade = []

for x in data:
    
    if x >= 90:
        x = 4.00
    elif x < 90 and x >= 80:
        x = 4.00
    elif x < 80 and x >= 75:
        x = 3.67
    elif x < 75 and x >=70:
        x = 3.33
    elif x < 70 and x >= 65:
        x = 3.00
    elif x < 65 and x >= 60:
        x = 2.67
    elif x < 60 and x >= 55:
        x = 2.33
    elif x < 55 and x >= 50:
        x = 2.00
    elif x < 50 and x >= 47:
        x = 1.67
    elif x < 47 and x >= 44:
        x = 1.33
    elif x < 44 and x >= 40:
        x = 1.00
    else:
        x = 0
    grade.append(x)

gpa = sum(grade)/number_sub
print("GPA: {}".format(gpa))




