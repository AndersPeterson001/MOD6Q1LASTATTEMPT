# Import the datetime class from the datetime module
from datetime import datetime


def display_differences(date_pairs, output_label):
    # Initialize an empty string to hold the output
    output = ""

    # Iterate through each pair of dates in the date_pairs list
    for date1, date2 in date_pairs:
        try:
            # Convert the first date string to a datetime object
            date1_obj = datetime.strptime(date1, '%Y-%m-%d')
            # Convert the second date string to a datetime object
            date2_obj = datetime.strptime(date2, '%Y-%m-%d')

            # Calculate the absolute difference between the two dates
            delta = abs(date2_obj - date1_obj)
            # Get the number of days in the difference
            difference = delta.days

            # Append the formatted information to the output string
            output += f"Date 1: {date1}\nDate 2: {date2}\nDifference: {difference} days\n\n"
        except ValueError as e:
            # If there's a ValueError (e.g., wrong date format), add an error message to the output
            output += f"Invalid date format for pair ({date1}, {date2}): {e}\n\n"

    # Update the output_label's text with the generated output
    output_label.config(text=output)
