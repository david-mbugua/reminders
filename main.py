import datetime

# Function to add a new reminder
def add_reminder(reminder_text, reminder_date):
    # Create a new reminder dictionary
    new_reminder = {
        "text": reminder_text,
        "date": reminder_date
    }
    
    # Add the new reminder to the list of reminders
    reminders.append(new_reminder)

# Function to show all reminders
def show_reminders():
    # Check if there are any reminders
    if len(reminders) == 0:
        print("No reminders to show.")
        return
    
    # Print the list of reminders
    print("Your reminders:")
    for reminder in reminders:
        print(f"{reminder['text']} on {reminder['date']}")

# Initialize the list of reminders
reminders = []

# Add some test reminders
add_reminder("Buy milk", datetime.date(2022, 12, 14))
add_reminder("Pay electricity bill", datetime.date(2022, 12, 20))
add_reminder("Submit project report", datetime.date(2022, 12, 22))

# Show the reminders
show_reminders()
