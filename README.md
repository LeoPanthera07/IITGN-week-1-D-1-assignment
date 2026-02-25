# Gandhinagar Weather & AQI Scraper 🌤️🌫️

A Python-based web scraping project that collects the **last 10 days of weather data** for Gandhinagar, including:

- 🌡 Temperature (°C)  
- 💧 Humidity (%)  
- 🌫 AQI (Air Quality Index)  

The program calculates **Average** and **Median** for each parameter and saves the analysis to a `results.txt` file.

---

## 📌 Features

- Scrapes historical **Temperature & Humidity**
- Scrapes **AQI (Air Quality Index)**
- Performs statistical analysis:
  - Average Temperature
  - Median Temperature
  - Average Humidity
  - Median Humidity
  - Average AQI
  - Median AQI
- Automatically generates `results.txt`
- Clean and structured output

---

## 🛠 Requirements

- Python 3.x
- Internet connection
- Required libraries:

```bash
pip install requests beautifulsoup4