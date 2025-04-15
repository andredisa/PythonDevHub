# 📈 Stock Price Visualizer with Polygon.io

A simple Python project to visualize **daily open and close prices** of a selected stock over a specific month and year using the [Polygon.io](https://polygon.io/) API.

This script fetches financial data and generates a line plot to help users understand how a stock has performed within a given time frame.

---

 🧰 Features

- 🔍 User input for **month**, **year**, and **stock symbol**
- 🔗 Fetches stock data from Polygon.io API
- 📊 Plots **Open** and **Close** daily prices
- ✅ Input validation for date and stock fields
- 🔒 API key is securely imported from a config file

---

## 🛠️ Requirements

- Python 3.x
- [matplotlib](https://matplotlib.org/)
- [requests](https://pypi.org/project/requests/)
- A valid [Polygon.io API key](https://polygon.io/)

Install dependencies via pip:

```bash
pip install matplotlib requests

## 🔐 API Key Setup
Create a file named configFinanza.py in the same directory with the following content:

POLYGON_TOKEN = "your_polygon_api_key_here"

⚠️ Do not share or commit this file to public repositories.

## 🚀 How to Run

Execute the script with:
python main.py

You'll be prompted to:

Enter a month (1–12)

Enter a year (2000–2024)

Enter a stock ticker (e.g., AAPL, GOOGL, TSLA)

A line graph will be shown with daily Open and Close prices.

📉 Example Output
You’ll see a plot like:

X-axis: timestamps (daily)

Y-axis: prices in USD

Two lines:

🔵 Open prices

🔴 Close prices

💡 Ideas for Improvement
🧠 Add automatic leap year handling for February

💾 Save plots to file (.png)

⏱️ Add a time range selection (weekly, monthly, etc.)

📈 Add moving averages or volume bars

🌐 Build a web interface using Flask or Streamlit

🧠 Educational Purpose
This project is great for practicing:

API integration

JSON parsing

Data visualization

Python OOP

Input validation

📎 Disclaimer
Stock data is for educational purposes only. Do not use this tool for real-time trading decisions.

👨‍💻 Happy coding and data exploring!