from datetime import datetime
from datetime import timedelta

def display_current_datetime():
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(current_date)
    calculate_future_date()

    
def calculate_future_date():
    num_of_days = int(input("Enter the number of days to add to the current date: "))

    future_date = datetime.now() + timedelta(days=num_of_days)

    print(f"Future date: {future_date.strftime("%Y-%m-%d")}")

    

if __name__ == "__main__":
    display_current_datetime()