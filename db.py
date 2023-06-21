employees =[]


# Create
def add_employee():

    name=input("Enter employee name")
    age = int(input("Enter employee age"))
    position = input("Enter employee position")

    employee = {
        'name': name,
        'age': age,
        'position': position
    }

    employees.append(employee)
    print("Employee added successfully")

# Read

def print_employee_details(employee):
    print("Employee Details")
    print("Name",employee['name'])
    print("Age",employee['age'])
    print("Position",employee['position'])
    print()

def display_employee_details():
    if not employees:
        print("Employee not found")
    else:
        print("Employee list")
        for employee in employees:
            print_employee_details(employee)

# Update
def update_employee():
    name=input("Enter employee name to update")

    for employee in employees:
        if employee['name']==name:
            print_employee_details(employee)
            new_name = input("Enter new name")
            new_age= int(input("Enter new age"))
            new_position = input("Enter new position")

            if new_name:
                employee['name']=new_name
            if new_age:
                employee['age']=new_age
            if new_position:
                employee['position']=new_position
            print("Employee details updated")
            print_employee_details(employee)
            return
        print("Employee found")

# Delete

def delete_employee():
    name=input("Enter employee name to delete")
    for employee in employees:
        if employee['name']==name:
            print_employee_details(employee)
            confirm = input("Are you sure")
            if confirm.lower() == 'y':
                employees.remove(employee)
                print("Employee detail deleted")
            else:
                print("Deletion cancelled")
            return
        print("Employee not found")

def main_menu():
    while True:
        print("1 Add Employee")
        print("2 Get Employee details")
        print("3 update Employee details")
        print("4 delete Employee details")
        print("5 Exit")

        choice = int(input("make choice"))
        if choice ==1:
            add_employee()
        elif choice==2:
            display_employee_details()
        elif choice==3:
            update_employee()
        elif choice==4:
            delete_employee()
        elif choice==5:
            break
        else:
            print("Invalid option")
main_menu()
