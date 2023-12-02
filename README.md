
# WikipediaApi

## Project Description
WikipediaApi is a Python-based project designed to interact with the Wikimedia API. It fetches historical events data for specific dates, processes this data, and outputs it into an Excel file. This tool is particularly useful for historians, educators, students, or anyone interested in historical events.

## Features
- Fetches data from Wikimedia API for specific dates.
- Processes historical events, births, deaths, and holiday data.
- Outputs the data into well-structured Excel files.
- Includes utility functions for data exploration and debugging.

## Installation
To install and run WikipediaApi, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   ```
2. **Navigate to the project directory:**
   ```bash
   cd WikipediaApi
   ```
3. **Install required packages:**
    - Ensure you have Python 3.x installed.
    - Install the required packages:
      ```bash
      pip install -r requirements.txt
      ```

## Usage
To use WikipediaApi, run the `api_base.py` script:

1. **Set up credentials:**
    - Update the `credentials.py` file with your API credentials.

2. **Run the script:**
   ```bash
   python api_base.py
   ```

3. **Check the output:**
    - The script will generate an Excel file with historical data for the specified date.

## License
This project is licensed under the MIT License - see the `LICENSE.md` file for details.
