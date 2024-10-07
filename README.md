Usage
Relay Control
To set the relay state:

python
Copy code
board.relay_set(value)  # value: True to turn on, False to turn off
Buzzer Control
To control the buzzer:

python
Copy code
board.buzzer_set(frequency, duration)  # frequency in Hz, duration in seconds
Play Melody
To play a predefined melody:

python
Copy code
board.play_melody()
LED Control
To set RGB LED values:

python
Copy code
board.rgb_set(r, g, b)  # r, g, b: Boolean values (True/False)
To control regular LEDs:

python
Copy code
board.leds_set(r, g, y)  # r, g, y: Boolean values (True/False)
Power Output Control
To set the power output:

python
Copy code
board.pwout_set(value)  # value: True to enable, False to disable
Button and Reed Switch States
To read the button state:

python
Copy code
button_state = board.button_get()  # Returns the state of the button (1 or 0)
To read the reed switch state:

python
Copy code
reed_state = board.reed_get()  # Returns the state of the reed switch (1 or 0)
DHT Sensor
To read temperature and humidity from a DHT11 sensor:

python
Copy code
temp, humidity = board.dht_get()  # Returns temperature and humidity values
Photoresistor
To read the value from a photoresistor (LDR):

python
Copy code
ldr_value = board.ldr_get()  # Returns the ADC value from the photoresistor
License
This library is licensed under the MIT License. Feel free to use it in your projects!

typescript
Copy code

You can save this content in a file named `README.md`. Let me know if you need any further modifications!
