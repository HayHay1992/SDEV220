# Haylea McDaniel
# M02GPALab.py
# This program accepts student last name
# Then student first name
# Then tests GPA

lastName = input("Enter student last name: ")
if lastName == 'ZZZ':
    print("Name not valid")

else:
    firstName = input("Enter student first name: ")
    studentGPA = float(input("Enter student GPA: "))

    if studentGPA >= 3.50:
        print(f"{lastName} , {firstName} made the Dean's list.\n")
    elif studentGPA < 3.5 and studentGPA >= 3.25:
        print(f"{lastName} , {firstName} made the honor roll.\n")
    elif studentGPA < 3.25:
        print(f"{lastName} , {firstName} made neither.\n")
