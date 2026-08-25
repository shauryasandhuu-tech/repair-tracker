# Phone Repair Job Tracker - Iteration 1
# This first version runs in the console (no window, no GUI yet).
# The goal here is just to get the core logic working: adding a job,
# checking the input is valid, viewing the jobs, and deleting one.
# The list only exists while the program is running, it is not saved
# to a file yet, that gets added in a later iteration.

jobs = []

def add_job():
    # Ask the user to type in each piece of information
    name = input("Customer name: ")
    phone = input("Phone number: ")
    model = input("Device model: ")
    issue = input("Issue: ")

    # Check nothing was left blank
    if name.strip() == "" or phone.strip() == "" or model.strip() == "" or issue.strip() == "":
        print("Error: all fields are required.")
        return

    # Check the phone number only has digits in it
    if not phone.strip().isdigit():
        print("Error: phone number must contain digits only.")
        return

    # Everything looks fine, so build the job as a single line and store it
    job = name + " - " + phone + " - " + model + " - " + issue
    jobs.append(job)
    print("Job saved for " + name)

def view_jobs():
    if len(jobs) == 0:
        print("No jobs yet.")
    else:
        print("---- Current Jobs ----")
        # enumerate gives us a number alongside each job, starting at 1,
        # so the user has something to type in when deleting
        position = 1
        for job in jobs:
            print(str(position) + ". " + job)
            position = position + 1

def delete_job():
    if len(jobs) == 0:
        print("No jobs to delete.")
        return

    view_jobs()
    choice = input("Type the number of the job to delete: ")

    # Check the user actually typed a number
    if not choice.isdigit():
        print("Error: please type a valid number.")
        return

    index = int(choice) - 1

    # Check the number they typed is actually in range
    if index < 0 or index >= len(jobs):
        print("Error: that job number doesn't exist.")
        return

    removed = jobs.pop(index)
    print("Deleted: " + removed)

def main_menu():
    while True:
        print("")
        print("1. Add a repair job")
        print("2. View all jobs")
        print("3. Delete a job")
        print("4. Quit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_job()
        elif choice == "2":
            view_jobs()
        elif choice == "3":
            delete_job()
        elif choice == "4":
            print("Goodbye")
            break
        else:
            print("Please choose 1, 2, 3 or 4.")

# This only runs when the file is run directly
if __name__ == "__main__":
    main_menu()