"""
This is a Python program of hospital database management that would be 
beneficial for the hospital receptionist to obtain information related 
to patients, doctors, and patient's medical history.

Name: Aakash Kishanbhai Prajapati
Title: Hospital Database Management
Subject: FCSP-1
Enrollment No. : 23002170120001


--------------------------------------------------------------------------
"""

import mysql.connector
from datetime import datetime
from datetime import date

mydb = mysql.connector.connect(
    host="localhost", user="root", passwd="aakash", database="hospital"
)


# ------------------------------------------------------------------------#
# Hospital Class                                                         #
# ------------------------------------------------------------------------#
class Hospital:
    def __init__(self):
        print("\n---------------------------------------------------")
        print("MAIN MENU")
        print("---------------------------------------------------\n")
        print("1. Patient\n2. Doctor\n3. Exit")
        try:
            data = int(input("\nChoose the data you want to work with: "))
            if data == 1:
                patient = Patient()
            elif data == 2:
                doc = Doctor()
            elif data == 3:
                exit()
            else:
                print("\nENTER A VALID CHOICE!")
                hosp = Hospital()
        except ValueError:
            print("\nENTER A VALID CHOICE!")
            hosp = Hospital()


# ------------------------------------------------------------------------#
# Doctor Class                                                           #
# ------------------------------------------------------------------------#
class Doctor:
    def __init__(self):
        print("\n---------------------------------------------------")
        print("DOCTOR MENU")
        print("---------------------------------------------------\n")
        print("1. Register New Doctor\n2. Display All Doctors\n3. Return to main menu")
        try:
            doc_choice = int(input("\nEnter your selection: "))
            if doc_choice == 1:
                self.register_doctor()
            elif doc_choice == 2:
                self.display_doctor()
            elif doc_choice == 3:
                hospital = Hospital()
            else:
                print("\nENTER A VALID CHOICE!")
                doc = Doctor()
        except ValueError:
            print("\nENTER A VALID CHOICE!")
            doc = Doctor()

    def register_doctor(self):
        doc_name = input("Enter name of doctor: ")
        doc_edu = input("Enter qualification: ")
        doc_availability = input(
            "Enter Availability(Mon, Tue, Wed, Thu, Fri, Sat, Sun): "
        )
        doc_number = validate_mobile_no(
            input("Enter valid 10-digit Mobile number containing only digits: ")
        )

        try:
            mycursor = mydb.cursor()
            query = "INSERT INTO `hospital`.`doctor` (`doc_name`, `doc_edu`, `doc_days`, `doc_phone`) VALUES (%s,%s,%s,%s)"
            values = (doc_name, doc_edu, doc_availability, doc_number)
            mycursor.execute(query, values)
            mydb.commit()
            print("Record Added Successfully!")
            self.__init__()
        except:
            print("Record of other doctor with same mobile number already exists!")
            print("\nExisting Record:")
            mycursor = mydb.cursor()
            mycursor.execute(
                "SELECT * FROM `hospital`.`doctor` WHERE doc_phone = %s", (doc_number,)
            )
            myresult = mycursor.fetchall()
            for x in myresult:
                for i in x:
                    print(i)
            print("\n---------------------------------------------------")
            print("Doctor detail not registered.")
            print("---------------------------------------------------\n")
            self.__init__()

    def display_doctor(self):
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM `hospital`.`doctor`")
        myresult = mycursor.fetchall()
        if myresult:
            print("\n---------------------------------------------------")
            print("DOCTORS")
            print("---------------------------------------------------")
            for index, value in enumerate(myresult):
                print(
                    f"\n{index+1}.\nName: {value[0]}\nDoctor Qualification: {value[1]}\nAvailability: {value[2]}\nPhone No.: {value[3]}\n"
                )
            print("---------------------------------------------------")
            self.__init__()
        else:
            print("No Doctors Registered")
            self.__init__()

    # show all appointments for doctor


# ------------------------------------------------------------------------#
# Patient Class                                                          #
# ------------------------------------------------------------------------#
class Patient:
    def __init__(self):
        print("\n---------------------------------------------------")
        print("PATIENT MENU")
        print("---------------------------------------------------\n")
        print(
            "1. Register New Patient\n2. Search Patient\n3. Schedule Appointment\n4. Return to main menu"
        )
        try:
            pat_choice = int(input("\nEnter your selection: "))
            if pat_choice == 1:
                self.register_patient()
            elif pat_choice == 2:
                self.search_patient()
            elif pat_choice == 3:
                self.appointment_schedule()
            elif pat_choice == 4:
                hospital = Hospital()
            else:
                print("\nENTER A VALID CHOICE!")
                self.__init__()
        except ValueError:
            print("\nENTER A VALID CHOICE!")
            self.__init__()

    def register_patient(self):
        patient_name = input("Enter patient's full name: ")
        patient_dob = validate_DOB(input("Enter Date of Birth (yyyy-mm-dd): "))
        patient_address = input("Enter Address: ")
        patient_phone = validate_mobile_no(
            input("Enter valid 10-digit Mobile number containing only digits: ")
        )
        patient_email = input("Enter email ID: ")
        try:
            mycursor = mydb.cursor()
            query = "INSERT INTO `hospital`.`patient` (`patient_name`,`patient_dob`,`patient_address`,\
            `patient_phone`,`patient_email`) VALUES (%s,%s,%s,%s,%s)"
            values = (
                patient_name,
                patient_dob,
                patient_address,
                patient_phone,
                patient_email,
            )
            mycursor.execute(query, values)
            mydb.commit()
            print("Record Added Successfully!")
            self.__init__()
        except:
            print("Record of other patient with same mobile number already exists!")
            print("\nExisting Record:")
            mycursor = mydb.cursor()
            mycursor.execute(
                "SELECT * FROM `hospital`.`patient` WHERE patient_phone = %s",
                (int(patient_phone),),
            )
            myresult = mycursor.fetchall()
            for x in myresult:
                for i in x:
                    print(i)
            print("\nPatient detail not registered.")
            print("\n---------------------------------------------------")
            self.__init__()

    def search_patient(self):
        patient_num = [
            validate_mobile_no(input("Enter the mobile number of patient: "))
        ]

        cursor = mydb.cursor()
        query = "SELECT * FROM `hospital`.`patient` WHERE `patient_phone` = %s"
        cursor.execute(query, patient_num)

        myresult = cursor.fetchone()

        print("\n---------------------------------------------------")

        if myresult:
            print("Patient Details:\n")
            print(
                f"Name: {myresult[0]}\nDOB: {myresult[1]}\nAddress: {myresult[2]}\nPhone No.: {myresult[3]}\ne-Mail: {myresult[4]}"
            )
            print("---------------------------------------------------\n")
            self.__init__()
        else:
            while True:
                choice = input(
                    "No record found. Do you want to register the patient? (Y/N): "
                )
                if choice == "y" or choice == "Y":
                    self.register_patient()
                    break
                elif choice == "n" or choice == "N":
                    self.__init__()
                    break
                else:
                    print("\nENTER A VALID CHOICE!")
                    self.__init__()
                    break

    def appointment_schedule(self):
        patient_num = [
            validate_mobile_no(input("Enter the mobile number of patient: "))
        ]

        mycursor = mydb.cursor()
        query = "SELECT * FROM `hospital`.`patient` WHERE `patient_phone` = %s"
        mycursor.execute(query, patient_num)
        myresult = mycursor.fetchone()
        if myresult:
            print(
                f"\nName: {myresult[0]}\nDOB: {myresult[1]}\nAddress: {myresult[2]}\nPhone No.: {myresult[3]}\ne-Mail: {myresult[4]}"
            )
            mycursor = mydb.cursor()
            query = "SELECT * FROM `hospital`.`doctor`"
            mycursor.execute(query)
            mydocresult = mycursor.fetchall()
            print("\nDoctors:")
            for index, doctor in enumerate(mydocresult):
                print(f"{index+1}. {doctor[0]}, {doctor[1]}, Available: {doctor[2]}")

            try:
                choose_doctor = int(
                    input(
                        "\nEnter the index number of doctor to select them for appointment: "
                    )
                )
                if choose_doctor > len(list(enumerate(mydocresult))):
                    print("Invalid choice")
                    self.appointment_schedule()
                else:
                    appointment_date = checkDay(list(enumerate(mydocresult))[choose_doctor - 1][1][2])
                    appointment_time = validate_time()
                    doctor_name = list(enumerate(mydocresult))[choose_doctor - 1][1][0]
                    mycursor = mydb.cursor()
                    query = "INSERT INTO `hospital`.`appointment` (`patient_name`,`patient_phone`,`doctor_name`,`appointment_date`,`appointment_time`) VALUES (%s,%s,%s,%s,%s)"
                    values = (
                        myresult[0],
                        myresult[3],
                        doctor_name,
                        appointment_date,
                        appointment_time,
                    )
                    mycursor.execute(query, values)
                    mydb.commit()
                    print("Appointment Scheduled Successfully!")
                    self.__init__()
            except ValueError:
                print("Invalid choice")
                self.appointment_schedule()

        else:
            print("\nNo record found. Please register patient.")
            try:
                while True:
                    choice = int(
                        input(
                            "\nEnter Choice (1 to register patient / 2 to re-enter number): "
                        )
                    )
                    if choice == 1:
                        self.register_patient()
                        break
                    elif choice == 2:
                        self.appointment_schedule()
                        break
                    else:
                        print("Invalid choice")

            except ValueError:
                print("Invalid choice")
                self.appointment_schedule()


# ------------------------------------------------------------------------#
#                     VALIDATIONS (DOB and Mobile)                       #
# ------------------------------------------------------------------------#


# Validate DOB
# Ref: https://www.geeksforgeeks.org/python-validate-string-date-format/
def validate_DOB(date):
    val_date = date
    while True:
        # initializing format
        format = "%Y-%m-%d"
        # using try-except to check for truth value
        try:
            datetime.strptime(val_date, format)
            break

        except:
            print("Wrong Date!")
            val_date = input("Enter Date of Birth (yyyy-mm-dd): ")
    return val_date


# Validate Mobile Number
def validate_mobile_no(mobile_no):
    while not mobile_no.isdigit() or len(mobile_no) != 10:
        mobile_no = input(
            "Enter a valid 10-digit Mobile number containing only digits: "
        )
    return mobile_no


# Validate Date
def validate_date(dates):
    while True:
        # initializing format
        format = "%Y-%m-%d"
        f_date = dates.split("-")
        # using try-except to check for truth value
        try:
            datetime.strptime(dates, format)

            if (
                date(int(f_date[0]), int(f_date[1]), int(f_date[2])) - date.today()
            ).days < 0:
                print("Cannot schedule appointment for past date")
                raise Exception
            break

        except:
            print("Wrong Date!")
            dates = input("\nEnter Date (yyyy-mm-dd): ")
    return dates


# Check availability of doctor
def checkDay(available_day):
    init_date = input("\nEnter Date (yyyy-mm-dd): ")
    dates = validate_date(init_date)
    year, month, day = dates.split("-")
    selected_day = date(int(year), int(month), int(day)).strftime("%A")
    if selected_day[:3].lower() in available_day.lower():
        return dates
    else:
        print("Doctor not available on selected date! Please choose another date.")
        return checkDay(available_day)


def validate_time():
    time = input("\nEnter time for the appointment (HH:MM):")
    try:
        datetime.strptime(time, "%H:%M")
        return time
    except:
        print("Invalid Time Format!\nPlease enter in HH:MM format.")
        return validate_time()


hospital = Hospital()
