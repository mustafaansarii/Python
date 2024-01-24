from datetime import datetime, date, time, timedelta

# Get current date an1d time
current_datetime = datetime.now()
print("Current Date and Time:", current_datetime)

# Access individual components of a datetime object
print("Year:", current_datetime.year)
print("Month:", current_datetime.month)
print("Day:", current_datetime.day)
print("Hour:", current_datetime.hour)
print("Minute:", current_datetime.minute)
print("Second:", current_datetime.second)

# Create a specific date and time
custom_datetime = datetime(2022, 5, 15, 14, 30, 0)
print("Custom Date and Time:", custom_datetime)

# Format a datetime object as a string
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted Date and Time:", formatted_datetime)

# Parse a string to create a datetime object
date_str = "2022-07-20"
parsed_date = datetime.strptime(date_str, "%Y-%m-%d")
print("Parsed Date:", parsed_date)

# Calculate the difference between two dates
date1 = date(2022, 1, 1)
date2 = date(2022, 12, 31)
date_difference = date2 - date1
print("Date Difference:", date_difference.days, "days")

# Add or subtract a duration from a datetime object
one_day = timedelta(days=1)
tomorrow = current_datetime + one_day
yesterday = current_datetime - one_day
print("Tomorrow:", tomorrow)
print("Yesterday:", yesterday)
