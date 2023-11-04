# BMKG API Scraper
# Ahmad Zaki Akmal
# All data is owned by BMKG

# Libs
import requests
import json
import csv

# Link BMKG API
baseUrl = "https://ibnux.github.io/BMKG-importer/"

# List of regions
import requests
import json

# Function to get region's weather data
def getWeatherData (kota ,regionId):
  # Get weather data
  weatherUrl = baseUrl + "cuaca/" + regionId + ".json"
  print("Getting data from " + weatherUrl)
  if(regionId == "0") :
    return None
  
  try:
    weatherData = requests.get(weatherUrl)
    # Check if the request was successful
    weatherData.raise_for_status()
    weatherData = weatherData.json()  # Parse JSON data directly
    # Append 'kota' attribute to each dictionary in weatherData
    for data in weatherData:
        data["kota"] = kota
    return weatherData
  except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
    return None
  except json.JSONDecodeError as json_err:
    print(f"JSON decoding error occurred: {json_err}")
    return None
  except requests.exceptions.RequestException as req_err:
    print(f"Request error occurred: {req_err}")
    return None
  except Exception as err:
    print(f"An error occurred (getWeatherData): {err}")
    return None

regionUrl = "https://ibnux.github.io/BMKG-importer/cuaca/wilayah.json"
try:
    regionData = requests.get(regionUrl)
    # Check if the request was successful
    regionData.raise_for_status()
    listOfRegions = regionData.json()  # Parse JSON data directly
    
    # Keys to extract
    regionKeys = ["id", "propinsi", "kota"]
    filteredRegions = []

    # Iterate over the loaded JSON data
    for region in listOfRegions:
      regionDict = {}
      for key in regionKeys:
          regionDict[key] = region.get(key)
      filteredRegions.append(regionDict)
      
    # ! trim to only first 10 regions
    filteredRegions = filteredRegions[:10]

    for region in filteredRegions:
      print(region)
      
    # Iterate each region and call their respective API    
    weatherData = []
    for region in filteredRegions:
      tempWeatherData = getWeatherData(region["kota"] ,region["id"])
      if tempWeatherData:
        weatherData.append(tempWeatherData)
        
    # Write to CSV  
    fileName = "weatherData.csv"
    csvHeader = ["kota", "jamCuaca", "kodeCuaca", "cuaca", "humidity", "tempC", "tempF"]
    
    # for data in weatherData:
    #   print(data)
    #   print("\n")
    
    with open(fileName, "w") as csvFile:
      csvWriter = csv.DictWriter(csvFile, fieldnames=csvHeader)
      csvWriter.writeheader()
      for data in weatherData:
          for subData in data:
            print(subData)
            csvWriter.writerow(subData)
            
    print("Written " + str(len(weatherData)) + " rows to " + fileName)

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except json.JSONDecodeError as json_err:
    print(f"JSON decoding error occurred: {json_err}")
except requests.exceptions.RequestException as req_err:
    print(f"Request error occurred: {req_err}")
except Exception as err:
    print(f"An error occurred (Write CSV): {err}")





