from machine import Pin, PWM
from time import sleep
import dht

class Board:
    BOARD_TYPE = 1
    
    # Add flags to check if pins have been initialized
    pin_initialized = {
        'relay': False,
        'buzzer': False,
        'ledsw': False,
        'rled': False,
        'gled': False,
        'yled': False,
        'bled': False,
        'pwout': False,
        'btn': False,
        'reed': False,
        'dht': False
        
    }
    
    if BOARD_TYPE == 1:
        reed_pin = 16  
        wake_pin = 16  
        sda_pin = 5  
        dht_pin = 5  
        latch_pin = Pin(15, Pin.OUT)  
        sck_pin = Pin(4, Pin.OUT)   
        data_pin = Pin(5, Pin.OUT)    
        buzzer_pin = 0  
        f_button = 0  
        rled_pin = 12  
        yled_pin = 14  
        bled_pin = 14  
        gled_pin = 2   
        pwout_pin = 13 
        btn_pin = 15   
        scl_pin = 15   
        lsens_pin = 2  
        ledsw_pin = 0  
        relay_pin = 1  

        # Define bit values as constants
        BUZZER = 0b00000001
        LEDS = 0b00001110
        RGB = 0b01001110
        BUTTON = 0b00100000
        PWOUT = 0b00100000
        RELAY = 0b10000000
        ALL = 0b11111111
        OFF = 0b00000000

    def __init__(self):
        # Initialize pins
        self.latch = self.latch_pin
        self.clock = self.sck_pin
        self.data = self.data_pin

    def shift_out(self, data):
        """Shift out 8 bits to the 74HC595 shift register."""
        for i in range(8):
            bit = (data >> (7 - i)) & 1  # Get the bit from MSB to LSB
            self.data.value(bit)  # Send the bit to data pin
            self.clock.value(1)    # Set clock high
            self.clock.value(0)    # Set clock low

    def set(self, data):
        """Write data to the shift register."""
        self.latch.value(0)  # Set latch low
        self.shift_out(data)  # Shift out the data
        self.latch.value(1)  # Set latch high to update output

    def relay_set(self, value):
        self.set(self.RELAY)
        """Control the relay pin."""
        if not self.pin_initialized['relay']:
            self.relay = Pin(self.relay_pin, Pin.OUT)
            self.pin_initialized['relay'] = True
        
        sleep(0.1)
        try:
            self.relay.value(bool(value))
        except:
            print("Relay value isn't right")

    def buzzer_set(self, frequency, duration):
        self.set(self.BUZZER)
        """Turn buzzer on or off."""
        if not self.pin_initialized['buzzer']:
            self.buzzer = PWM(Pin(self.buzzer_pin))
            self.pin_initialized['buzzer'] = True
        
        sleep(0.1)
        try:
            self.buzzer.freq(frequency)
            self.buzzer.duty(512)
            sleep(duration)
            self.buzzer.duty(0)
        except:
            print("Buzzer value isn't right")

    def play_melody(self):
        """Play a melody on the buzzer."""
        notes = {
                "a3f": 208,
                "b3f": 233,
                "b3": 247,
                "c4": 261,
                "c4s": 277,
                "e4f": 311,
                "f4": 349,
                "a4f": 415,
                "b4f": 466,
                "b4": 493,
                "c5": 523,
                "c5s": 554,
                "e5f": 622,
                "f5": 698,
                "f5s": 740,
                "a5f": 831,
                "rest": 0
            }
        melody = [(notes["b4f"], 0.2), (notes["b4f"], 0.2), (notes["a4f"], 0.2), (notes["a4f"], 0.2),
                  (notes["f5"], 0.3), (notes["f5"], 0.3), (notes["e5f"], 0.6), (notes["b4f"], 0.2),
                  (notes["b4f"], 0.2), (notes["a4f"], 0.2), (notes["a4f"], 0.2), (notes["e5f"], 0.3),
                  (notes["e5f"], 0.3), (notes["c5s"], 0.2), (notes["c5"], 0.2), (notes["b4f"], 0.2),
                  (notes["c5s"], 0.2), (notes["c5s"], 0.2), (notes["c5s"], 0.2), (notes["c5s"], 0.2),
                  (notes["c5s"], 0.3), (notes["e5f"], 0.2), (notes["c5"], 0.2), (notes["b4f"], 0.2),
                  (notes["a4f"], 0.2), (notes["a4f"], 0.2), (notes["a4f"], 0.2), (notes["e5f"], 0.3),
                  (notes["c5s"], 0.2), (notes["b4f"], 0.2), (notes["b4f"], 0.2), (notes["a4f"], 0.2),
                  (notes["a4f"], 0.2), (notes["f5"], 0.3), (notes["f5"], 0.3), (notes["e5f"], 0.6),
                  (notes["b4f"], 0.2), (notes["b4f"], 0.2), (notes["a4f"], 0.2), (notes["a4f"], 0.2),
                  (notes["f5"], 0.3), (notes["f5"], 0.3), (notes["e5f"], 0.6), (notes["b4f"], 0.2),
                  (notes["b4f"], 0.2), (notes["a4f"], 0.2), (notes["a4f"], 0.2), (notes["rest"], 0.4)
                ]
        for note, duration in melody:
            self.buzzer_set(note, duration)

    def leds_set(self, r, g, y):
        self.set(self.LEDS)
        """Control RGB LEDs."""
        if not self.pin_initialized['ledsw']:
            self.ledsw = Pin(self.ledsw_pin, Pin.OUT)
            self.rled = Pin(self.rled_pin, Pin.OUT)
            self.gled = Pin(self.gled_pin, Pin.OUT)
            self.yled = Pin(self.yled_pin, Pin.OUT)
            self.pin_initialized['ledsw'] = True
        
        sleep(0.1)
        try:
            self.rled.value(bool(r))
            self.gled.value(bool(g))
            self.yled.value(bool(y))
            sleep(0.2)
        except:
            print("LEDS value isn't right")

    def rgb_set(self, r, g, b):
        self.set(self.RGB)
        """Control RGB LEDs."""
        if not self.pin_initialized['ledsw']:
            self.ledsw = Pin(self.ledsw_pin, Pin.OUT)
            self.rled = Pin(self.rled_pin, Pin.OUT)
            self.gled = Pin(self.gled_pin, Pin.OUT)
            self.bled = Pin(self.bled_pin, Pin.OUT)
            self.pin_initialized['ledsw'] = True
        try:
            self.rled.value(not bool(r))
            self.gled.value(not bool(g))
            self.bled.value(not bool(b))
            sleep(0.2)
            self.ledsw.value(1)
        except:
            print("RGB value isn't right")

    def pwout_set(self, value):
        self.set(self.PWOUT)
        """Control the power output pin."""
        if not self.pin_initialized['pwout']:
            self.pwout = Pin(self.pwout_pin, Pin.OUT)
            self.pin_initialized['pwout'] = True
        
        try:
            self.pwout.value(bool(value))
        except:
            print("Power output value isn't right")

    def button_get(self):
        self.set(self.BUTTON)
        """Read the state of the button."""
        if not self.pin_initialized['btn']:
            self.btn = Pin(self.btn_pin, Pin.IN)
            self.pin_initialized['btn'] = True
        return self.btn.value()

    def reed_get(self):
        if not self.pin_initialized['reed']:
            self.reed = Pin(self.reed_pin, Pin.IN)
            self.pin_initialized['reed'] = True
        return self.reed.value()
    
    def dht_get(self):
        if not self.pin_initialized['dht']:
            # Initialize the DHT sensor pin
            self.dht = Pin(self.dht_pin, Pin.IN)
            self.pin_initialized['dht'] = True
            try:
                # Create an instance of the DHT11 sensor
                self.sensorDHT = dht.DHT11(self.dht)
                # Measure the temperature and humidity
                self.sensorDHT.measure()

                # Read the temperature in Celsius
                self.temp = self.sensorDHT.temperature()

                # Read the humidity
                self.humidity = self.sensorDHT.humidity()

                return self.temp, self.humidity  # Return temperature and humidity as a tuple

            except OSError as e:
                print('Failed to read sensor:', e)
                return None, None  # Return None values on failure
         
        


