# Covid19-Data-Analysis

Project Description:

This project analyzes COVID-19 cases in Germany using Python & Pandas. It performs data cleaning, time-series analysis, and visualization with Matplotlib.

Files in the Repository:

covid_analysis.py – The main script for data processing and analysis.
covid_de.zip - Contains the Database
README.md – This file containing project information.

Data Source:

To run the script, you need a CSV file containing COVID-19 data for Germany. Ensure that the file covid_de.csv is in the same directory as the script or provide a custom path.

Installation & Execution:

1) Requirements

You need Python 3.x and the following libraries:
pip install pandas matplotlib

2) Run the Script
   
python covid_analysis.py
If the covid_de.csv file is stored in a different location, you can specify the file path when running the script.

Features:

- Data cleaning (handling missing values)
- Date format conversion
- Aggregation of daily case numbers
- Calculation of a 7-day moving average
- Visualization of case numbers in Germany
- Analysis by gender and federal state

Example Visualizations:

The script generates various charts, including:
- Line chart for daily COVID-19 cases
- Bar chart for total cases per federal state
- Pie charts for gender distribution

Future Improvements: 

-  Support for interactive visualizations with Plotly
-  Analysis of vaccination rates & hospitalization trends
-  Integration with an API for real-time data updates

Author: Pascal Hamm

