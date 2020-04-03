from flask import Flask
from flask_ask import Ask, statement, question, session
import lcddriver
import time
import requests, json


display = lcddriver.lcd()

app = Flask(__name__)
ask = Ask(app, '/')

#starting web application
@app.route('/')
def homepage():
    return "Hi"

#starting question when he skill is trigered by Alexa
@ask.launch
def start_skill():
    mes = "Tell me the city name for the wether information"
    return question(mes)




@ask.intent('weather')
def weather(city_name):
    display.lcd_clear()
    
    api_key = "your api key"

    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    complete_url = base_url + "q=" + city_name + "&units=metric" + "&appid=" + api_key

    response = requests.get(complete_url)

    x = response.json()

    if x["cod"] != "404": 
      
        # store the value of "main" 
        # key in variable y 
        y = x["main"] 
      
        # store the value corresponding 
        # to the "temp" key of y 
        current_temperature = y["temp"] 
      
        # store the value corresponding 
        # to the "pressure" key of y 
        current_pressure = y["pressure"] 
      
        # store the value corresponding 
        # to the "humidity" key of y 
        current_humidiy = y["humidity"] 
      
        # store the value of "weather" 
        # key in variable z 
        z = x["weather"] 
      
        # store the value corresponding  
        # to the "description" key at  
        # the 0th index of z 
        weather_description = z[0]["description"]
        
        display.lcd_display_string(city_name + ", " + str(int(current_temperature))+ " c", 1)
        display.lcd_display_string(weather_description, 2)
        mesage = "temperature in " + city_name + str(current_temperature)
        print (mesage)
        return statement ("Information is presented on the display")

    
if __name__ == '__main__':
    app.run(port=5001)
