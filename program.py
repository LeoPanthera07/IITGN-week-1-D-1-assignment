# weather_scraper.py

import requests
from bs4 import BeautifulSoup
import statistics

# Weather historical data URL (Temperature & Humidity)
weather_url = "https://www.timeanddate.com/weather/india/gandhinagar/historic"

# AQI source URL (example: AQI page for Gandhinagar)
aqi_url = "https://www.aqi.in/in/dashboard/india/gujarat/gandhinagar"

headers = {
    "User-Agent": "Mozilla/5.0"
}

temperatures = []
humidity = []
aqi_values = []

# ----------------------------
# Scrape Temperature & Humidity
# ----------------------------

weather_response = requests.get(weather_url, headers=headers)
weather_soup = BeautifulSoup(weather_response.text, "html.parser")

weather_table = weather_soup.find("table", {"id": "wt-his"})

if weather_table:
    rows = weather_table.find_all("tr")[1:11]  # Last 10 entries

    for row in rows:
        cols = row.find_all("td")
        if len(cols) > 6:
            try:
                temp = cols[1].text.strip().replace("°C", "")
                hum = cols[5].text.strip().replace("%", "")

                temperatures.append(float(temp))
                humidity.append(float(hum))
            except:
                continue

# ----------------------------
# Scrape AQI Data
# ----------------------------

aqi_response = requests.get(aqi_url, headers=headers)
aqi_soup = BeautifulSoup(aqi_response.text, "html.parser")

# Example: Attempt to find AQI values from span or div
aqi_spans = aqi_soup.find_all("span")

for span in aqi_spans:
    text = span.text.strip()
    if text.isdigit():
        value = int(text)
        if 0 < value < 500:  # Valid AQI range
            aqi_values.append(value)

# Take first 10 AQI values (if available)
aqi_values = aqi_values[:10]

# ----------------------------
# Check if data collected
# ----------------------------

if len(temperatures) == 0 or len(humidity) == 0 or len(aqi_values) == 0:
    print("Could not fetch complete data. Website structure may have changed.")
else:
    # Temperature calculations
    avg_temp = sum(temperatures) / len(temperatures)
    median_temp = statistics.median(temperatures)

    # Humidity calculations
    avg_humidity = sum(humidity) / len(humidity)
    median_humidity = statistics.median(humidity)

    # AQI calculations
    avg_aqi = sum(aqi_values) / len(aqi_values)
    median_aqi = statistics.median(aqi_values)

    # Save results
    with open("results.txt", "w") as file:
        file.write("Weather & AQI Analysis for Gandhinagar (Last 10 Days)\n")
        file.write("------------------------------------------------------\n\n")

        file.write("Temperature Analysis:\n")
        file.write(f"Average Temperature: {avg_temp:.2f} °C\n")
        file.write(f"Median Temperature: {median_temp:.2f} °C\n\n")

        file.write("Humidity Analysis:\n")
        file.write(f"Average Humidity: {avg_humidity:.2f} %\n")
        file.write(f"Median Humidity: {median_humidity:.2f} %\n\n")

        file.write("AQI Analysis:\n")
        file.write(f"Average AQI: {avg_aqi:.2f}\n")
        file.write(f"Median AQI: {median_aqi:.2f}\n")

    print("Analysis complete. Results saved in 'results.txt'.")