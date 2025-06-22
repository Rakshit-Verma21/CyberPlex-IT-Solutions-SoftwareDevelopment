'''
Add, delete, search student

Console based

File storage or array

'''

import json


student_dic={}

def load_file():
    try:
        with open('student.json', 'r') as file:
            global student_dic
            student_dic = json.load(file)
    except FileNotFoundError:
        print("File not found")

def write():
    with open("student.json","w") as f:
         json.dump(student_dic, f, indent=4)

         print("Successfull")
    
def add_student():
    id=int(input("Enter Student ID: "))
    name=input("Enter Student Name: ")
    age=int(input("Enter Student Age: "))
    course=input("Enter Student Course: ")
    student_dic[id]={"name":name,"age":age,"course":course}
    write()
    

def delete_student():
    if not student_dic:
        print("No Students in the list")
    else:
        id=input("Enter Student ID to delete: ").strip()
        if id in student_dic:
            del student_dic[id]
            write()
        else:
            print("Student not found")
def read():
    if not student_dic:
        print("No Students in the list")
    else:
        for id,student in student_dic.items():
            print(f"ID : {id} | Name: {student['name']}")
            print("\n")

def search():
    if not student_dic:
        print("No Students in the list")
    else:
        read()
        id=input("Enter Student ID to search: ").strip()
        if str(id) in student_dic:
            name=student_dic[id]["name"]
            age=student_dic[id]["age"]
            course=student_dic[id]["course"]
            print(f"Name: {name}, Age: {age}, Course: {course}")
        else:
            print("Student not found")

while True:
    load_file()
    print("1. Add Student")
    print("2. Delete Student")
    print("3. Search Student")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        delete_student()
    elif choice == "3":
        search()
    elif choice == "4":
        break
    else:
        print("Invalid choice")