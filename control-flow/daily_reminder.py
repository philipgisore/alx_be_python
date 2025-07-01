
task = input("Please enter task description: ")
priority = input("Choose priority level (high, medium, low): ").lower()
time_bound = input("Is the task time bound? (yes/no): ").lower()

reminder = ""

match priority:
    case "high":
            reminder = f"Reminder: '{task}' is a HIGH priority task"
    case "medium":
        reminder = f"Reminder: '{task}' is a MEDIUM priority task"
    case "low":
        reminder = f"Reminder: '{task}' is a LOW priority task"
    case _:
        reminder = f"Reminder: '{task}' has unkown priority level"

if time_bound == "yes":
    reminder += "It requires immediate attention today!"

print(reminder)


