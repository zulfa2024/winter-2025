'''
Write a python program that asks for n students' details, including ID, Name , gender. For each student,also ask for two hobbies, which should be stored in tuple. Maintain all student records in a list, where each student's details are stored as a list containing their ID, Name, gender,and hobbies tuple. Finally, display the student information.
'''
import os
os. system("cls")

students = []

n = int(input("Enter the number of students: "))

for i in range(n):
    student_id = input("Enter the student ID: ")
    student_name = input("Enter the student name: ")
    student_gender = input("Enter the student gender: ")
    student_hobbies = (input("Enter the first hobby: "), input("Enter the second hobby: "))
    student_information = [student_id, student_name, student_gender, student_hobbies,]
    print(f"Student {i+1} details: {student_information}")
    students.append(student_information)
    print("-" * 50)
    input("\nPress any key to continue...")
    

    
    
    
    
    
    
    
    
    
    

