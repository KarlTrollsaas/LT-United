from flask import Flask
from flask_ask import Ask, statement, question, session
import lcddriver
import time
import datetime
import threading

# Load the driver and set it to "display"
# If you use something from the driver library use the "display." prefix first
display = lcddriver.lcd()

app = Flask(__name__)
ask = Ask(app, '/')

#starting web application
@app.route('/')
def homepage():
    return "Hi"

#writing startup message to display
display.lcd_display_string("Pomodoro time", 1)


def timer(m, s, message):
    """Timer function: it counts down time on the display. 
    Parameters:
    m - minuts to run,
    s - secconds to run, 
    message - String to display on the first line of display. Max 16 chars"""

    print("Writing to display")
    display.lcd_display_string(message, 1)
    while m>0 or s>0:
        if s < 10 and m < 10:
            text = "Left:0{}min 0{}sec".format(m, s)
            display.lcd_display_string(text, 2)
        elif s < 10 and m > 9:
            text = "Left:{}min 0{}sec".format(m, s)
            display.lcd_display_string(text, 2)
        elif s > 9 and m < 10:
            text = "Left:0{}min {}sec".format(m, s)
            display.lcd_display_string(text, 2)   
        else:
            text = "Left:{}min {}sec".format(m, s)
            display.lcd_display_string(str(text), 2)    
        if s == 0:
            m -= 1
            s = 59
        else:
            s -= 1
        
        # Program then loops with no delay (Can be added with a time.sleep)
        time.sleep(1)


    display.lcd_clear()
    display.lcd_display_string("Finish", 1)

def pomodoro(tm):
#function to start pomodoro loop. 
#tm - how many times to run the loop including study time and pause.
    t = tm
    while t > 0:
        timer(25, 0, "No time to waste")
        timer(5, 0, "Take a break")
        t -=1
        
#starting question when the skill is trigered by Alexa
@ask.launch
def start_skill():
    mes = "How many session you want to have?"
    return question(mes)


@ask.intent('times', convert={"num" : int})
def times(num):
    """Function for running pomodoro timer when its trigered by Alexa.
    It takes a inegere parameter to determen how many sesions you want to run.
    We run time counter on the seperate thread to avoid time out error on the Alexa."""
    th = threading.Thread(target=pomodoro, args=[num])
    th.start()
    m = "Study time"
    return statement(m)


if __name__ == '__main__':
    app.run(port=5001)
