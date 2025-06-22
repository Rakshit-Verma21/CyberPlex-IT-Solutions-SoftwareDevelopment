'''
Note Keeper CLI

Features:
Create, read, delete notes
CLI interface
Data stored in file

'''

import json

notes={}

def load_notes():
    global notes
    try:
        with open('notes.txt', 'r') as f:
            notes = json.load(f)
    except FileNotFoundError:
        print("File not found. Creating new file...")
def create_note():
    id=input("Enter note ID: ")
    title = input("Enter note title: ")
    content = input("Enter note content: ")
    notes[id] = {"title": title, "content": content}
    
    with open('notes.txt', 'w') as f:
        json.dump(notes, f)
        print("Added")

def read_note():
    if not notes:
        print("No notes available")
    else:
        print("Your Notes List")
        for id, note in notes.items():
            print(f"ID: {id} - Title: {note['title']} - Content: {note['content']}\n")

def delete_note():
    
    if not notes:
        print("No notes to delete")
    else:
        id = input("Enter note ID to delete: ")
        if id in notes:
         del notes[id]
         with open('notes.txt', 'w') as f:
            json.dump(notes, f)
            print("Deleted")
print("Welcome to Note Keeper CLI")
load_notes()
while True: 
    print("\nOptions:")
    print("1. Create note | 2. Read note | 3. Delete note | 4. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        create_note()
    elif choice == "2":
        read_note()
    elif choice == "3":
        delete_note()
    elif choice == "4":
        break
    else:
        print("Invalid option. Please choose a valid option.")





