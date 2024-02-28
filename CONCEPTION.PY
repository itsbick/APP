from datetime import datetime, timedelta

# Main function
def main():
    # Get the birthdate of the child from the user
    child_birthdate_str = input("Enter the birthdate of the child (MM-DD-YYYY): ")
    child_birthdate = datetime.strptime(child_birthdate_str, "%m-%d-%Y")

    # Define the range of days for possible conception (259 to 287 days)
    min_days = 259
    max_days = 287

    # Calculate the earliest and latest possible conception dates
    earliest_conception_date = child_birthdate - timedelta(days=max_days)
    latest_conception_date = child_birthdate - timedelta(days=min_days)

    # Print the possible range for conception
    print("Possible range for conception (259 to 287 days):")
    #print("Early possible date:", earliest_conception_date.strftime("%m-%d-%Y"))
    #print("Later possible date:", latest_conception_date.strftime("%m-%d-%Y"))

    print(earliest_conception_date.strftime("%m-%d"),"to",latest_conception_date.strftime("%m-%d-%Y"))


    # Print the estimated conception date
    #print("Estimated conception date (approximately average 280 days of):", estimated_conception.strftime("%Y-%m-%d"))

if __name__ == "__main__":
    main()
