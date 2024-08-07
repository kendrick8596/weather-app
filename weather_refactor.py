import requests

api_key = "ac1d69c1d98523be1dfd8ee6e45bd8e2"
city_name = input("Enter name of city: ")
state_code = input("Enter state code: ")
base_url = "https://api.openweathermap.org/data/2.5/weather?"

#url = base_url + "q=" + city_name + "&appid=" + api_key
url = f"{base_url}q={city_name},{state_code}US&appid={api_key}"
print(url)

#checking the response of the url
response = requests.get(url)
print(response)

#parsing data from json file
data = response.json()
main = data['main']
wind = data['wind']
k_temp = main['temp']
humidity = main['humidity']
wind_speed = wind['speed']
direction = wind['deg']

#temperature conversions
f_temp = (k_temp - 273.15) * 9//5 + 32
f_temp = "{:.0f}".format(f_temp)
c_temp = (int(f_temp) - 32) / 1.8
c_temp = "{:.0f}".format(c_temp)
print(f"The temperature is, {f_temp} degrees Fahrenheit, {c_temp} degrees Celsius with humidity at {humidity}% .")

class WindConditions:
    def __init__(self, directions, description):
        self.directions = directions
        self.description = description
        
    def direction_match(self, direction):
        if isinstance(self.directions, range):
            return direction in self.directions
        return direction in self.directions
    
    def __str__(self):
        return self.description
    
conditions = [
    WindConditions([360, 350, 10], "north"),
    WindConditions(range(20, 71), "northeast"),
    WindConditions([80, 90, 100], "east"),
    WindConditions(range(110, 161), "southeast"),
    WindConditions([170, 180, 190], "south"),
    WindConditions(range(200, 251), "southwest"),
    WindConditions([260, 270, 280], "west"),
]

def get_wind_condition(direction):
    for condition in conditions:
        if condition.direction_match(direction):
            return condition
    #return None

condition = get_wind_condition(direction)
print(f"Winds are out of the {condition} with windspeeds of {wind_speed} mph.")