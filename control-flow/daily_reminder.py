try:
    task = input("Enter your task: ").lower()
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    if time_bound == 'yes':
        print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
    else:
        print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time.")
    
except:
    print("Invalid Value.")