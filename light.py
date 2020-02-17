from flask import Flask
from flask_ask import Ask, statement, question, session
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)

app = Flask(__name__)
ask = Ask(app, '/')

@app.route('/')
def homepage():
    return "Hi"

@ask.launch
def start_skill():
    message = "Do you want to turn the light on or off?"
    return question(message)


@ask.intent('LightOn')
def lightOn():
    GPIO.output(18, GPIO.HIGH)
    #time.sleep(1)   
    light = "Ok, the light is now on"
    return statement(light)

@ask.intent('LightOff')
def lightOff():
    GPIO.output(18, GPIO.LOW)
    #time.sleep(1)
    light = "Ok, the light is now off"
    return statement(light)

if __name__ == '__main__':
    app.run(port=5001)
