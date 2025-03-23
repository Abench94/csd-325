#A program to gather information about the weather
import json
import requests
import re
#establish the url variable with the api destination and api key
base_url = "https://api.openweathermap.org/data/2.5/weather"
appid = "906b6939735602a519447e37a839d229"


def main():
  #begin a loop to allow the user to run the program multiple times
  again = '1'
  while (again == '1'):
    #get the zipcode
    zip_code = input("Enter the zip code for the weather look up: ")
    #Regex for input validation
    x = re.search("[0-9]{5}", zip_code)
    #error statement if the zipcode is not 5 digits
    if (x is None):
      print('Invalid zip code: ' + zip_code)
    #execution of the program if the zipcode is 5 digits
    else:
      url = f"{base_url}?q={zip_code}&units=imperial&APPID={appid}"
      response = requests.get(url)
      unformated_data = response.json()

      #print the json response if needed for debugging
      #print(unformated_data)

      #parse and print the desired data from the json response
      temp = unformated_data["main"]["temp"]
      print(f"The current temperature is: {temp}")
      temp_max = unformated_data["main"]["temp_max"]
      print(f"The high temperature is: {temp_max}")
      temp_min = unformated_data["main"]["temp_min"]
      print(f"The low temperature is: {temp_min}")

      again = input('Press 1 to look up another zip code or 2 to exit: ')

if __name__ == "__main__":
  main()