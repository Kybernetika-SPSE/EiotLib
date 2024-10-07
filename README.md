# eiotlib.py

## Overview
`eiotlib.py` is a custom MicroPython library designed for ESP8266-based projects, particularly for IoT applications involving various sensors and actuators. This library facilitates easy interaction with hardware components like relays, buzzers, LEDs, buttons, reed switches, and DHT11 temperature and humidity sensors.

## Features
- Control relays and buzzers
- Read button and reed switch states
- Measure temperature and humidity using the DHT11 sensor
- Control RGB LEDs and standard LEDs
- Shift register interfacing using 74HC595
- Initialize and manage multiple pins efficiently

## Installation
1. Clone the repository or download the `eiotlib.py` file.
2. Upload the `eiotlib.py` file to your ESP8266 board using an appropriate tool (e.g., `mpfshell`, `ampy`, or `rshell`).

## Usage

### Example Code
```python
from eiotlib import Board

# Initialize the board
board = Board()

# Set relay on
board.relay_set(1)

# Control the buzzer
board.buzzer_set(frequency=1000, duration=1)

# Read DHT sensor
temp, humidity = board.dht_get()
print("Temperature:", temp, "°C")
print("Humidity:", humidity, "%")

# Get reed switch value
reed_value = board.reed_get()
print("Reed Switch State:", reed_value)

# Control LEDs
board.leds_set(r=1, g=0, y=0)  # Turn on red LED
