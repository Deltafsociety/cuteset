import os

# Create a directory to store the diary entries
diary_dir = "diary_entries"
if not os.path.exists(diary_dir):
    os.makedirs(diary_dir)

# Define the color codes for the pink theme
pink_bg = "\033[48;2;255;192;203m"
pink_fg = "\033[38;2;255;105;180m"
reset = "\033[0m"

# Define the main function to run the diary app
def main():
    print(f"{pink_bg}{pink_fg}Welcome to your Pink Diary!{reset}\n")
    print("What would you like to do?\n")
    while True:
        print("1. Write a new diary entry")
        print("2. Read a diary entry")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")
        if choice == "1":
            write_entry()
        elif choice == "2":
            read_entry()
        elif choice == "3":
            print(f"{pink_fg}Goodbye!{reset}")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Define a function to write a new diary entry
def write_entry():
    entry_date = input("Enter the date of your entry (e.g. 2023-02-20): ")
    entry_filename = os.path.join(diary_dir, f"{entry_date}.txt")
    if os.path.exists(entry_filename):
        overwrite = input("An entry already exists for this date. Do you want to overwrite it? (y/n): ")
        if overwrite.lower() != "y":
            print("Entry not saved.\n")
            return
    entry_text = input("Write your diary entry: ")
    with open(entry_filename, "w") as f:
        f.write(entry_text)
    print("Entry saved.\n")

# Define a function to read a diary entry
def read_entry():
    entry_date = input("Enter the date of the entry you want to read (e.g. 2023-02-20): ")
    entry_filename = os.path.join(diary_dir, f"{entry_date}.txt")
    if not os.path.exists(entry_filename):
        print(f"No entry found for {entry_date}.\n")
        return
    with open(entry_filename, "r") as f:
        entry_text = f.read()
    print(f"\n{pink_fg}Diary Entry for {entry_date}:{reset}\n")
    print(entry_text)
    print("\n")

# Call the main function to start the app
if __name__ == "__main__":
    main()
