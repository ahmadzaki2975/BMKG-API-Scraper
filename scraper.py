# BMKG API Scraper
# Ahmad Zaki Akmal
# All data is owned by BMKG

# Libs
import requests
import json

# Link BMKG API
baseUrl = "https://ibnux.github.io/BMKG-importer/"

# List of regions
import requests
import json

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

    for region in filteredRegions:
      print(region)

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except json.JSONDecodeError as json_err:
    print(f"JSON decoding error occurred: {json_err}")
except requests.exceptions.RequestException as req_err:
    print(f"Request error occurred: {req_err}")
except Exception as err:
    print(f"An error occurred: {err}")





