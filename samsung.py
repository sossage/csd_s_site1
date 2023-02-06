import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP) # button
GPIO.setup(12, GPIO.OUT) # LED string

num_leds = 300
led_string = [(0, 0, 0) for i in range(num_leds)]

def show_leds(led_string):
    for i in led_string:
        for j in range(3):
            GPIO.output(12, i[j])
            time.sleep(0.002)

def gradient(led_string, start, end, step_size):
    for i in range(0, end - start + 1, step_size):
        led_string[start + i] = (255, 0, 0) # red
    for i in range(step_size, end - start + 1, step_size):
        led_string[start + i] = (0, 0, 255) # blue
    return led_string

led_string = gradient(led_string, 0, 75, 5) # blue to red on leds 1 - 75
led_string = gradient(led_string, 76, 150, 5) # red to blue on leds 76 - 150
led_string = gradient(led_string, 151, 225, 5) # blue to red on leds 151-225
led_string = gradient(led_string, 226, 300, 5) # red to blue on leds 226-300

button_state = GPIO.input(5)
if button_state == False:
    led_string = [(0, 0, 0) for i in range(num_leds)]
    for i in range(num_leds):
        led_string[i] = gradient(led_string, 0, 75, 5)
        led_string[i] = gradient(led_string, 76, 150, 5)
        led_string[i] = gradient(led_string, 151, 225, 5)
        led_string[i] = gradient(led_string, 226, 300, 5)
        show_leds(led_string)
else:
    show_leds(led_string)

with open('/home/samsung/log_samsung.txt', 'a') as f:
    if button_state == False:
        f.write(f'Button was pressed at {time.ctime()}\n')
