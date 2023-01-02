import csv

std_field = ['student_id', 'roll', 'name', 'batch_name']
std_db = 'studentDBStore.csv'


def display_menu():
    print("---------------------------------------")
    print(" Student DBMS")
    print("---------------------------------------")
    print("1. Add New Student")
    print("2. View Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Quit")


def addStd():
    print("-------------------------")
    print("Add Student Information")
    print("-------------------------")
    global std_field
    global student_database
    student_data = []
    for field in std_field:
        value = input("Enter " + field + ": ")
        student_data.append(value)

    with open(std_db, "a", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([student_data])

    print("Data saved successfully")
    input("Press any key to continue")
    return


def viewStd():
    global std_field
    global std_db

    print("--- Student Records ---")

    with open(std_db, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for x in std_field:
            print(x, end='\t |')
        print("\n-----------------------------------------------------------------")

        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")

    input("Press any key to continue")




def updStd():
    global std_field
    global std_db

    print("--- Update Student ---")
    roll = input("Enter roll no. so as to update: ")
    index_std = None
    updated_data = []
    with open(std_db, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if roll == row[0]:
                    index_std = counter
                    print("Student Found: at index ",index_std)
                    student_data = []
                    for field in std_field:
                        value = input("Enter " + field + ": ")
                        student_data.append(value)
                    updated_data.append(student_data)
                else:
                    updated_data.append(row)
                counter += 1


    
    if index_std is not None:
        with open(student_database, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
    else:
        print("Roll No. not found in the database")

    input("Press any key to continue")


def delete_student():
    global std_field
    global std_db

    print("--- Delete Student ---")
    roll = input("Enter roll no. to delete: ")
    std_found = False
    updated_data = []
    with open(std_db, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if roll != row[0]:
                    updated_data.append(row)
                    counter += 1
                else:
                    student_found = True

    if std_found is True:
        with open(std_db, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
        print("Roll no. ", roll, "deleted successfully")
    else:
        print("Roll No. not found in our database")

    input("Press any key to continue")

while True:
    display_menu()

    choice = input("Enter your choice: ")
    if choice == '1':
        addStd()
    elif choice == '2':
        viewStd()
    elif choice == '3':
        updStd()
    elif choice == '4':
        delete_student()
    else:
        break

print("-------------------------------")
print(" Thank you for using our system")
print("-------------------------------")