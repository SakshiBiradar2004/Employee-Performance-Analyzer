# main.py
from analyzer import PerformanceAnalyzer

a = PerformanceAnalyzer()
a.load_data()

while True:
    print("\n=== Employee Performance Analyzer ===")
    print("1. Add Employee")
    print("2. View All")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Top Performers")
    print("7. Save Data")
    print("8. Exit")

    ch = input("enter choice (1-8): ")

    if ch == "1":
        i = input("enter id: ")
        n = input("enter name: ")
        d = input("enter dept: ")
        s = input("enter score: ")
        a.add_employee(i, n, d, s)

    elif ch == "2":
        a.view_all()

    elif ch == "3":
        t = input("enter name or id to search: ")
        a.search_employee(t)

    elif ch == "4":
        i = input("enter id to update: ")
        a.update_employee(i)

    elif ch == "5":
        i = input("enter id to delete: ")
        a.delete_employee(i)

    elif ch == "6":
        a.top_performers()

    elif ch == "7":
        a.save_data()

    elif ch == "8":
        print("bye! don't forget to save data.")
        break

    else:
        print("invalid choice, try again")
