'''
Section 1:
1. Bug Tracker (Basic)

Features:
Add bug report (title, desc)
Mark fixed
Store in array / file

'''
import json

bug_report = {}


try:
    with open('bug_tracker.txt', 'r') as file:
        bug_report = json.load(file)  
except (FileNotFoundError, json.JSONDecodeError):
    print("No previous data found, starting fresh.")

print("Welcome to Bug Tracker")
print("1. Add Bug Report")
print("2. Mark Bug as Fixed")
print("3. Exit")

while True:
    choice = input("Enter your choice: ")

    if choice == "1":
        id = input("Enter Bug ID: ")
        title = input("Enter the bug title: ")
        desc = input("Enter the bug description: ")
        bug_report[id] = {"title": title, "description": desc, "status": "open"}

        with open("bug_tracker.txt", "w") as file:
            json.dump(bug_report, file, indent=4)
        
        print("Bug Report Added Successfully")

    elif choice == "2":
        id = input("Enter Bug ID: ").strip()
        if id in bug_report:
            bug_report[id]["status"] = "fixed"
            print("Bug Marked as Fixed")

           
            with open("bug_tracker.txt", "w") as file:
                json.dump(bug_report, file, indent=4)
        else:
            print("Bug ID not found!")

    elif choice == "3":
        print("Exiting Bug Tracker")
        break
