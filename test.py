
from datetime import datetime
from datetime import date

def validate_date(dates):
    while True:
        # initializing format
        format = "%Y-%m-%d"
        # using try-except to check for truth value
        try:
            datetime.strptime(dates, format)
            break

        except:
            print("Wrong Date!")
            dates = input("Enter Date: ")
    return dates


def check_day():
    init_date = input("Enter Date: ")
    dates=validate_date(init_date)
    year,month,day = dates.split('-')
    print(date(int(year),int(month),int(day)).strftime('%A'))

check_day()