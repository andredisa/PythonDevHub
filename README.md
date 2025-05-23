# 🐍 Python API Projects Collection

Welcome to my collection of **Python projects**! 🎓

> This repository includes three command-line tools that integrate with real-world APIs to fetch data, visualize it, and interact with the user through practical examples. Each project focuses on a specific domain — **news**, **travel**, and **finance** — and is ideal for learning how to work with APIs, parse JSON, and organize Python code.

---

## 📦 Project Overview

### 1. 📰 News Aggregator  
**Folder:** `newsApi/`

Fetch and explore the latest headlines from around the world using the [NewsAPI.org](https://newsapi.org/) service.

- 🌍 Top headlines by country or language  
- 🔍 Keyword or topic search  
- 📅 Filter by date range  
- 🌟 Sort by popularity or domain  
- 📖 View full article content  

> 🔧 Technologies: **Python 3**, `requests`, **NewsAPI**

> 📌 Concepts: `REST API`, `HTTP parameters`, `JSON parsing`, `OOP`, `CLI`

---

### 2. 🌍 Route Planner + Weather Forecast  
**Folder:** `calcKmPrevisione/`

Plan a multi-stop trip and get live weather info at each destination. Calculates distance and estimated travel time.

- 🗺️ Add and validate multiple locations  
- 🧭 Calculates distances and travel time between stops  
- 🌦️ Fetches current weather using OpenWeatherMap  
- 🔁 Ensures at least two locations before building a route  
- 📈 Displays totals at the end  

> 🔧 Technologies: **Python 3**, `requests`, `OpenStreetMap`, `OpenRouteService`, `OpenWeatherMap`

> 📌 Concepts: `Multi-API integration`, `modular Python`, `data aggregation`, `CLI input`

---

### 3. 📈 Stock Price Visualizer  
**Folder:** `graficoFinanza/`

Visualize a stock’s daily **Open** and **Close** prices for a selected month and year with a beautiful line graph.

- 🗓️ User input for month, year, and stock symbol  
- 📊 Graphs daily Open/Close prices  
- ✅ Validates stock symbols and dates  
- 🔒 API key handled via config file  
- 🖼️ Line plot with `matplotlib`  

> 🔧 Technologies: **Python 3**, `matplotlib`, `requests`, **Polygon.io**

> 📌 Concepts: `API interaction`, `data visualization`, `OOP`, `config management`

---

## 🎓 Shared Learning Objectives

Each project is designed to help you:

- ✅ Understand and integrate REST APIs  
- 🧾 Parse and process JSON responses  
- 🧱 Structure Python projects using classes and modules  
- 📊 Visualize or display real-world data  
- 🧠 Handle user input in CLI environments  

---

## 🛠️ Setup Instructions

> Each project is standalone. Follow individual project READMEs for detailed API setup and usage.

### 🔃 Common Dependencies

Install core dependencies using:

```bash
pip install requests matplotlib
```

**⚠️ Note: You’ll need to get free API keys from the respective services (NewsAPI, OpenWeatherMap, OpenRouteService, Polygon.io) and add them in config files or directly in the code (as instructed).**

---

## 🚀 Ideas for Future Improvements
- 🖼️ Add GUI versions with Tkinter or Flask

- 💾 Save outputs (JSON, text, plots) to local files

- 🔐 Move API keys to .env and use python-dotenv

- 🧪 Add unit tests for key components

- 🌐 Convert CLI projects into web apps

---

## ⚠️ Disclaimer
`These projects are for educational purposes only. Data may be subject to rate limits and may not be suitable for real-time or commercial use.`

---

## ☕ Support Me

If you find my work useful and would like to support me, you can buy me a coffee! Your support helps me keep creating and improving my projects. Thank you! 😊

<a href="https://www.buymeacoffee.com/andredisa" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>

---

### 👨‍💻 Happy coding and have fun exploring APIs with Python!
