import os 
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






# student_count = 5;
# A = [student_count]

# for id_student in range(student_count):    
#     print("STUDENT #", id_student+1)

#     # x holds the list of grades
#     x = []

#     # count of assignments 
#     assignments = 5

#     # Ask for a student ID from user
#     NETID = int(input('Enter your 4 digit student NET ID: '))

#     # fill list with grades from console input
#     x = [int(input('Please enter the grade you got on assignment {}: '.format(i+1))) for i in     range(assignments)]

#     midTermGrade = int(input('Please enter the grade you got on you Mid-Term: '))
#     finalGrade = int(input('Please enter the grade you got on you Final: '))

#     # count average, 
#     average_assignment_grade = (sum(x) + midTermGrade + finalGrade) / 7 

#     print()
#     print('NET ID | Average Final Grade')
#     print('---------------------------------')

#     for number in range(1):
#         print(NETID, " | ", format(average_assignment_grade, '.1f'),'%')

#     A.append(average_assignment_grade);

# grades_sum = sum(A)
# grades_average = grades_sum / 5;
# print("SUM OF ALL STUDENTS = " + grades_sum)
# print("AVERAGE OF ALL STUDENTS = " + grades_average)