import os
#create python program to accept n number of students as a list and each student will be a tuple 
#student ID, student first name, student last name, phone number

students = []
     
for i in range(3):
    student_id = input(f"Enter student ID {i+1}: ")
    first_name = input(f"Enter student first name {i+1}: ")
    last_name = input(f"Enter student last name {i+1}: ")
    phone_number = input(f"Enter student phone number {i+1}: ")
    
    student = (student_id, first_name, last_name, phone_number)
    students.append(student)
    print(type(student))
    
    
