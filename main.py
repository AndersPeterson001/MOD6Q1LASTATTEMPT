import tkinter as tk
from tkcalendar import DateEntry
from datetime import datetime

def calculate_date_difference():
    date1 = cal1.get_date()
    date2 = cal2.get_date()
    difference = (date2 - date1).days

    # Writing dates to a file
    with open('dates.txt', 'w') as file:
        file.write(f"{date1}\n{date2}\nDifference in days: {difference}")

    # Showing result in the GUI
    result_label.config(text=f"Days Difference: {difference}")

def main():
    # Initialize the tkinter window
    global root, cal1, cal2, result_label
    root = tk.Tk()
    root.title("Date Difference Calculator")

    # Create two datepickers
    cal1 = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2, date_pattern='y-mm-dd')
    cal1.pack(pady=10)

    cal2 = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2, date_pattern='y-mm-dd')
    cal2.pack(pady=10)

    # Create a calculate button
    calculate_button = tk.Button(root, text="Calculate Difference", command=calculate_date_difference)
    calculate_button.pack(pady=10)

    # Label to show the result
    result_label = tk.Label(root, text="")
    result_label.pack(pady=10)

    # Run the main loop
    root.mainloop()

if __name__ == "__main__":
    main()
