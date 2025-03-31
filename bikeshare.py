import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTH_DATA = ['january', 'february', 'march', 'april', 'may', 'june','all']
DAY_DATA = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Would you like to see data for Chicago, New York City, or Washington?").lower()
        if city in CITY_DATA:
            break
        else:
            print("Invalid input. Please enter a valid city name.")

    # TO DO: get user input of filter Type (type_filter)for month,day or not at all (all, january, february, ... , june)
    while True:
        type_filter = input("Would you like to filter the data by month, day, or not at all?").lower()
        if type_filter in ("month","day","not at all"):
            break
        else:
            print("Invalid input. Please enter a valid value as one of month, day, or not at all.")
   
    # TO DO: get user input for month (all, january, february, ... , june) if user chooses month in above filter
    if type_filter == "month":
        while True:
            month = input("Which month - All, January, February, March, April, May, June?").lower()
            if month in MONTH_DATA:
                break
            else:
                print("Invalid input. Please enter a valid month.")
    else:
        # Assign "all" to month when filter Type (type_filter) is not "month"
        month = 'all'
               
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    if type_filter == "day":
        while True:
            day = input("Which Day - All, 'Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'?").lower()
            if day in DAY_DATA:
                break
            else:
                print("Invalid input. Please enter a valid Day.")
    else:
        day = 'all' 
        # Assign "all" to day when filter Type (type_filter) is not "day"
          
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # Load csv file for the city specified
    file_name = CITY_DATA.get(city.lower())
    if file_name is None:
        raise ValueError(f"No Data available for city: {city}")
    
    df = pd.read_csv(file_name)
    
    # Convert the "Start Time" column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # Extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = MONTH_DATA
        month = months.index(month.lower()) + 1
        
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # Extract month, day of week and hour from 'Start Time' column
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print(f'Most Common Month: {popular_month}')
    df['hour'] = df['Start Time'].dt.hour

    # TO DO: display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()[0]
    print(f'Most Common Day of the week: {popular_day_of_week}')

    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print(f'Most Common Hour: {popular_hour}')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print(f'Most Commonly used Start Station: {popular_start_station}')

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print(f'Most Commonly used End Station: {popular_end_station}')

    # TO DO: display most frequent combination of start station and end station trip
    popular_trip = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print(f'Most frequent Trip: from {popular_trip[0]} to {popular_trip[1]}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print(f'Total Travel Time: {total_travel_time} seconds')

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print(f'Average Travel Time: {mean_travel_time} seconds')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of Each User Type:')
    print(user_types)

    # Check if 'Gender' column exists in the Dataframe
    if 'Gender' in df.columns:
        
    # TO DO: Display counts of gender
        gender_counts = df['Gender'].value_counts()
        print('Counts of Each Gender:')
        print(gender_counts)
    else:
        print('Gender information is not available.')
      
    # Check if 'Birth Year' column exists in the Dataframe
    if 'Birth Year' in df.columns:
    # TO DO: Display earliest, most recent, and most common year of birth
        earliest_year = df['Birth Year'].min()
        most_recent_year = df['Birth Year'].max()
        most_common_year = df['Birth Year'].mode()[0]
        
        print(f'Earliest Year of Birth: {int(earliest_year)}')
        print(f'Most recent Year of Birth: {int(most_recent_year)}')
        print(f'Most common Year of Birth: {int(most_common_year)}')
    else:
        print('Birth Year Information is not available')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """ Displays raw data one page at a time"""
    print("\n Displaying raw Data....")
    page_size = 5
    page_number = 0
    while True:
        raw_data = df.iloc[page_number*page_size:(page_number+1)*page_size]
        print(raw_data.to_string())
        cont = input('\nWould you like to see next {} rows of raw data? Enter Yes or No.\n'.format(page_size))
        if cont.lower() != 'yes':
            break
        page_number +=1
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

