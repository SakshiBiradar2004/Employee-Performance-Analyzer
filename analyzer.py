# analyzer.py
import csv

# class for one employee
class Employee:
    def __init__(self, emp_id, name, dept, score):
        self.emp_id = str(emp_id)
        self.name = name
        self.dept = dept
        self.score = float(score)

    def efficiency(self):
        return self.score


# class for all employees
class PerformanceAnalyzer:
    def __init__(self):
        self.employees = []

    # add new employee
    def add_employee(self, emp_id, name, dept, score):
        # check duplicate id
        for e in self.employees:
            if e.emp_id == str(emp_id):
                print("ID already exists! try again.")
                return
        # check valid number
        try:
            score = float(score)
            if score < 0:
                print("score cannot be negative")
                return
        except:
            print("enter a valid number for score")
            return

        new_emp = Employee(emp_id, name, dept, score)
        self.employees.append(new_emp)
        print(name, "added successfully!")

    # view all employees
    def view_all(self):
        if len(self.employees) == 0:
            print("no employees yet")
            return
        print("\nID\tName\tDept\tScore")
        for e in self.employees:
            print(e.emp_id, "\t", e.name, "\t", e.dept, "\t", e.score)

    # search employee
    def search_employee(self, text):
        found = []
        for e in self.employees:
            if text.lower() in e.name.lower() or text == e.emp_id:
                found.append(e)
        if len(found) == 0:
            print("no match found")
        else:
            print("\nSearch Results:")
            for e in found:
                print(e.emp_id, e.name, e.dept, e.score)

    # update employee
    def update_employee(self, emp_id):
        for e in self.employees:
            if e.emp_id == emp_id:
                print("Current info:", e.name, e.dept, e.score)
                new_name = input("new name (press enter to keep same): ")
                new_dept = input("new dept (press enter to keep same): ")
                new_score = input("new score (press enter to keep same): ")

                if new_name != "":
                    e.name = new_name
                if new_dept != "":
                    e.dept = new_dept
                if new_score != "":
                    try:
                        val = float(new_score)
                        if val >= 0:
                            e.score = val
                        else:
                            print("score cannot be negative")
                    except:
                        print("enter a valid number")
                print("updated successfully!")
                return
        print("ID not found")

    # delete employee
    def delete_employee(self, emp_id):
        for e in self.employees:
            if e.emp_id == emp_id:
                self.employees.remove(e)
                print("deleted successfully!")
                return
        print("ID not found")

    # top 3 performers
    def top_performers(self):
        if len(self.employees) == 0:
            print("no data yet")
            return
        sorted_list = sorted(self.employees, key=lambda x: x.score, reverse=True)
        print("\nTop 3 Performers:")
        for e in sorted_list[:3]:
            print(e.emp_id, e.name, e.dept, e.score)

    # save data
    def save_data(self, file="employees.csv"):
        try:
            with open(file, "w", newline="") as f:
                w = csv.writer(f)
                w.writerow(["ID", "Name", "Dept", "Score"])
                for e in self.employees:
                    w.writerow([e.emp_id, e.name, e.dept, e.score])
            print("data saved")
        except:
            print("error while saving")

    # load data
    def load_data(self, file="employees.csv"):
        try:
            with open(file, "r") as f:
                r = csv.DictReader(f)
                self.employees = []
                for row in r:
                    emp = Employee(row["ID"], row["Name"], row["Dept"], row["Score"])
                    self.employees.append(emp)
            print("data loaded")
        except FileNotFoundError:
            print("no file found, starting new")
        except:
            print("error while loading")
