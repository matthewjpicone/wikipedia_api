#!/usr/bin/env python3
"""
api_base.py

Author: Matthew Picone
Date: 11/3/2023

Part of the WikipediaApi project, this script is designed to interact with the Wikimedia API to fetch historical
events data, process it, and output it into an Excel file. It includes functionalities for fetching data for
specific dates, converting this data into a pandas DataFrame, and subsequently writing it to an Excel file.

See README.md for more details.
"""

import pandas as pd
import xlsxwriter
from datetime import datetime, timedelta
import requests
import credentials

# Global variable for tracking unique ID values
IDval = 1


def make_excel(df, sheet, path):
    """
    Creates an Excel file from a given DataFrame.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame containing the data to be written to the Excel file.
    sheet : str
        Name of the sheet in the Excel file.
    path : str
        Path where the Excel file will be saved.

    Returns
    -------
    None
    """
    writer = pd.ExcelWriter(path, engine='xlsxwriter')
    df.to_excel(writer, sheet_name=sheet, startrow=1, header=False, index=False)
    workbook = writer.book
    worksheet = writer.sheets[sheet]
    (max_row, max_col) = df.shape
    column_settings = [{'header': column} for column in df.columns]
    worksheet.add_table(0, 0, max_row, max_col - 1, {'columns': column_settings, "name": sheet})
    worksheet.set_column(0, max_col - 1, 12)
    writer.close()


def fetch_data_and_create_excel():
    """
    Fetches historical data from the Wikimedia API and creates an Excel file.

    The function retrieves historical event data for a specified date and processes it into a DataFrame.
    This DataFrame is then used to generate an Excel file.

    Returns
    -------
    None
    """
    global IDval
    data_array = {'Year': [], 'Date': [], 'HistoricEvent': []}

    for day_num in range(1):
        date = datetime(2023, 11, 1, 1, 00, 00) + timedelta(days=day_num)
        day, month = date.strftime("%d"), date.strftime("%m")
        wiki_date = f'{month}/{day}'

        url = 'https://api.wikimedia.org/feed/v1/wikipedia/en/onthisday/all/' + wiki_date

        # TODO: Reconfigure to use CentralConnect
        response = requests.get(url, headers=credentials.credentials.headers)
        data = response.json()
        try:
            for event in data['events']:
                data_array['Year'].append(event['year'])
                data_array['HistoricEvent'].append(event['text'])
                data_array['Date'].append(f'{day}/{month}')
                IDval += 1
        except KeyError:
            pass

    df = pd.DataFrame.from_dict(data_array)
    make_excel(df, 'TodayInHistory', 'TodayInHistory_nov.xlsx')


# The following functions are utility functions for printing different pieces of information
# from the fetched data. These can be utilized for debugging or data exploration.

def print_data_info(data):
    """
    Prints basic information about the fetched data.

    Parameters
    ----------
    data : dict
        Dictionary containing data fetched from Wikimedia API.

    Returns
    -------
    None
    """
    print(data.keys())
    print(len(data['events']), 'events')
    print(data['events'][0].keys())

    print(len(data['selected']), 'selected')
    print(data['selected'][0].keys())

    print(len(data['births']), 'births')
    print(data['births'][0].keys())

    print(len(data['deaths']), 'deaths')
    print(data['deaths'][0].keys())

    print(len(data['holidays']), 'holidays')
    print(data['holidays'][0].keys())


def print_event_info(data):
    """
    Prints detailed information about events from the fetched data.

    Parameters
    ----------
    data : dict
        Dictionary containing event data.

    Returns
    -------
    None
    """
    for event in data['events']:
        print(event['text'])
        print(event['pages'])
        print(event['year'])


def print_selected_info(data):
    """
    Prints information about selected events from the fetched data.

    Parameters
    ----------
    data : dict
        Dictionary containing selected event data.

    Returns
    -------
    None
    """
    for selected in data['selected']:
        print(selected['year'], selected['text'])


def print_births_info(data):
    """
    Prints information about birth events from the fetched data.

    Parameters
    ----------
    data : dict
        Dictionary containing birth event data.

    Returns
    -------
    None
    """
    for birth in data['births']:
        print(birth['year'], birth['text'])


def print_deaths_info(data):
    """
    Prints information about death events from the fetched data.

    Parameters
    ----------
    data : dict
        Dictionary containing death event data.

    Returns
    -------
    None
    """
    for death in data['deaths']:
        print(death['year'], death['text'])


def print_holidays_info(data):
    """
    Prints information about holidays from the fetched data.

    Parameters
    ----------
    data : dict
        Dictionary containing holiday data.

    Returns
    -------
    None
    """
    for holiday in data['holidays']:
        print(holiday['text'])


def main():
    fetch_data_and_create_excel()


if __name__ == '__main__':
    main()
