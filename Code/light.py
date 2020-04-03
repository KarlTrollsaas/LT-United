from flask import Flask
from flask_ask import Ask, statement, question, session
import RPi.GPIO as GPIO
import time

#GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)

# Load the driver and set it to "display"
# If you use something from the driver library use the "display." prefix first
app = Flask(__name__)
ask = Ask(app, '/')

#starting web application
@app.route('/')
def homepage():
    return "Hi"

#start question when the skill is trigered by Alexa
@ask.launch
def start_skill():
    message = "Do you want to turn the light on or off?"
    return question(message)

#function to turn the light on
@ask.intent('LightOn')
def lightOn():
    GPIO.output(18, GPIO.HIGH)
    #time.sleep(1)   
    light = "Ok, the light is now on"
    return statement(light)

#function to turn the light off
@ask.intent('LightOff')
def lightOff():
    GPIO.output(18, GPIO.LOW)
    #time.sleep(1)
    light = "Ok, the light is now off"
    return statement(light)

if __name__ == '__main__':
    app.run(port=5001)
