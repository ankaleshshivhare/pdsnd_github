>**Note**: Please **fork** the current Udacity repository so that you will have a **remote** repository in **your** Github account. Clone the remote repository to your local machine. Later, as a part of the project "Post your Work on Github", you will push your proposed changes to the remote repository in your Github account.

### Date created
03/31/2025

### Project Title
**Bike Share Data**

### Description
The project runs a _Python_ program_ which allows users to explore **US Bike Share Data**  data according to their needs to rent bicycles.
The program when invoked first welcomes the user and motivates him to explore **US Bike Share Data** Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter

### Files used
i) **Python Program:** _bikeshare.py
ii) ** Data Files:** _chicago.csv_ , _new_york_city.csv_, _washington.csv_ 

### Python Program Description

The program first asks users to enter city, month, and day.
Once users enter details _(of City, Month and/or Day)  for which they want to explore the data,
the program Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day

The user is able to
i) See statistics on the most frequent times of travel.
ii) See statistics on the most popular stations and trip.
iii) See statistics on the total and average trip duration.


### Credits

i) Docstrings provided by Udacity to use in Python Program.
ii) Udacity Bike Share Data Project Details.

