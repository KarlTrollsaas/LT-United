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

@app.route('/')
def homepage():
    return "Hi"

display.lcd_display_string("Pomodoro time", 1)

def timer(m, s, message):
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
    t = tm
    while t > 0:
        timer(1, 0, "No time to waste")
        timer(1, 0, "Take a break")
        t -=1
        

@ask.launch
def start_skill():
    mes = "How many times"
    return question(mes)


@ask.intent('times', convert={"num" : int})
def times(num):
    th = threading.Thread(target=pomodoro, args=[num])
    th.start()
    m = "Study time"
    return statement(m)


if __name__ == '__main__':
    app.run(port=5001)

