'''
3. Mini Library System

Features:
Add books

Issue/Return book
CLI menu

'''
from datetime import date
import json

books_dic={}

def load_file():
    global books_dic
    try:
        with open('books.json', 'r') as f:
            books_dic = json.load(f)
    except FileNotFoundError:
        print("File Not Found")

def write_file():
    with open('books.json','w') as file:
        json.dump(books_dic, file,indent=4)
    
    print("Successfull")

def add_book():
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    year= input("Enter book year: ")
    genre=input("Enter The Genre: ")
    books_dic[title] = {"author":author,"year":year,"genre":genre}
    write_file()

def list_books():
    for title,book in books_dic.items():
        print(f"Title: {title}, Author: {books_dic[title]['author']},Genre: {books_dic[title]['genre']},Year: {books_dic[title]['year']}")

def issue_book():
    if not books_dic:
        print("No books available")
    else:
        print("Available books:")
        list_books()
        title = input("Enter the title of the book you want to issue: ")
        if title in books_dic:
            books_dic[title]['status']='issued'
            today = date.today()
            books_dic[title]["issue_date"]=today.strftime("%Y-%m-%d")
            write_file()
        else:
            print("Book not found")

def list_issued_books():
    for title,book in books_dic.items():
        if books_dic[title]['status'] == 'issued':
         print(f"Title: {title}, Author: {books_dic[title]['author']},Issue Date: {books_dic[title]['issue_date']}")
def return_book():
    if not books_dic:
        print("No books available")
    else:
        print("Issued books:")
        list_issued_books()
        title = input("Enter the title of the book you want to return: ")
        if title in books_dic and books_dic[title]['status'] == 'issued':
            books_dic[title]['status']='available'
            today = date.today()
            books_dic[title]["return_date"]=today.strftime("%Y-%m-%d")
            write_file()
        else:
            print("Book not found or not issued")

while True:
    print("1.Add book")
    print("2.Issue book")
    print("3.Return book")
    print("4.To Exit")
    choice=input("Enter your Choice")
    if choice == "1":
        add_book()
    elif choice == "2":
        issue_book()
    elif choice == "3":
        return_book()
    elif choice == "4":
        break
    else:
        print("Invalid choice")
    


