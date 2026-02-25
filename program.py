# weather_scraper.py

import requests
from bs4 import BeautifulSoup
import statistics

# URL for historical weather of Gandhinagar
url = "https://www.timeanddate.com/weather/india/gandhinagar/historic"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Lists to store temperature and humidity
temperatures = []
humidity = []

# Find weather table
table = soup.find("table", {"id": "wt-his"})

if table:
    rows = table.find_all("tr")[1:11]  # Last 10 entries
    
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

# Ensure we got data
if len(temperatures) == 0 or len(humidity) == 0:
    print("Could not fetch data properly. Website structure may have changed.")
else:
    # Calculate averages
    avg_temp = sum(temperatures) / len(temperatures)
    avg_humidity = sum(humidity) / len(humidity)

    # Calculate medians
    median_temp = statistics.median(temperatures)
    median_humidity = statistics.median(humidity)

    # Save results
    with open("results.txt", "w") as file:
        file.write("Weather Analysis for Gandhinagar (Last 10 Days)\n")
        file.write("------------------------------------------------\n")
        file.write(f"Average Temperature: {avg_temp:.2f} °C\n")
        file.write(f"Median Temperature: {median_temp:.2f} °C\n\n")
        file.write(f"Average Humidity: {avg_humidity:.2f} %\n")
        file.write(f"Median Humidity: {median_humidity:.2f} %\n")

    print("Analysis complete. Results saved in 'results.txt'.")