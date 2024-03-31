from datetime import datetime
from datetime import date

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
    

print(checkDay("Tue, Fri"))