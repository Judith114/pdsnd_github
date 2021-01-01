import time
import pandas as pd
import numpy as np
import tabulate from tabulate

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    city = ''
    while city.lower not in ['chicago', 'new york', 'washington']:
        city = input('Would you like to see data for Chicago, New York, or Washington?\n').lower()
        if city in ['chicago', 'new york', 'washington']:
            break
        else:
            print('Please try again. Would you like to see data for Chicago, New York, or Washington?')

    # TO DO: get user input for month (all, january, february, ... , june)
    month = ''
    while month.lower() not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
        month = input('By which month would you like to filter the data? January, February, March, April, May, June, or all?\n').lower()
        if month in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
            break
        else:
            print('Please try again. By which month would you like to filter the data? January, February, March, April, May, June, or all?')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = ''
    while day.lower() not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
        day = input('By which day would you like to filter the data? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or all?\n').lower()
        if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
            break
        else:
            print('Please try again. By which day would you like to filter the data? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or all?')


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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

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

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    most_common_month = df['month'].mode()[0]
    print('Most common month:', most_common_month)


    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    most_common_day_of_week = df['day_of_week'].mode()[0]
    print('Most common day of the week:', most_common_day_of_week)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_start_hour = df['hour'].mode()[0]
    print('Most common start hour:', most_common_start_hour)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print('Most commonly used start station:', most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print('Most commonly used end station:', most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['Combination'] = df['Start Station'] + 'to ' + df['End Station']
    most_frequent_combination = df['Combination'].mode()[0]
    print('Most frequent combination of start station and end station trip:', most_frequent_combination)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    total_travel_time = round(total_travel_time/60, 2)
    print('Total travel time in minutes:', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    mean_travel_time = round(mean_travel_time/60, 2)
    print('Mean travel time in minutes:', mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of user types:\n' + str(user_types))

    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender_counts = df['Gender'].value_counts()
        print('Counts of gender:\n' + str(gender_counts))
    else:
        print("There is no gender information")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_birth_year = df['Birth Year'].min()
        most_recent_birth_year = df['Birth Year'].max()
        most_common_birth_year = df['Birth Year'].mode()[0]
        print('Earliest year of birth:', int(earliest_birth_year))
        print('Most recent year of birth:', int(most_recent_birth_year))
        print('Most common year of birth:', int(most_common_birth_year))
    else:
        print("There is no birth year information")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """Displays rows of data from the file of the selected city"""

    while True:
        display_data = input('\nWould you like to see 5 lines of raw data? Enter yes or no.\n')
        if display_data.lower() != 'yes':
            break
    print(tabulate(df_default.iloc[np.arange(0+i,5+i)], headers ="keys"))
    i+=5



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
