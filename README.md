# eiotlib.py - MicroPython Library

`eiotlib.py` is a custom MicroPython library designed for managing various hardware components connected to a board, such as relays, buzzers, LEDs, buttons, and a photoresistor (LDR). The library abstracts the control of these components through a high-level interface.

## Features

- **Relay control:** Toggle a relay using a specific pin.
- **Buzzer control:** Control the buzzer with custom frequency and duration.
- **Play melodies:** Play predefined melodies using the buzzer.
- **LED control:** Manage red, green, blue, and yellow LEDs.
- **Button state reading:** Retrieve the state of a button connected to the board.
- **Photoresistor reading:** Read values from an LDR to measure light intensity.

## Pin Definitions

The pin definitions used for this board are configured according to the BOARD_TYPE (currently set to 1). Below are the pin mappings for the components:

| Component | Pin Assignment |
| --------- | -------------- |
| Reed Pin | 16 |
| Wake Pin | 16 |
| SDA Pin | 5 |
| DHT Pin | 5 |
| Latch Pin | GPIO 15 |
| SCK Pin | GPIO 4 |
| Data Pin | GPIO 5 |
| Buzzer Pin | 0 |
| Function Button | 0 |
| Red LED Pin | GPIO 12 |
| Yellow LED Pin | GPIO 14 |
| Blue LED Pin | GPIO 14 |
| Green LED Pin | GPIO 2 |
| Power Output Pin | GPIO 13 |
| Button Pin | GPIO 15 |
| SCL Pin | GPIO 15 |
| Light Sensor Pin | GPIO 2 |
| LED Switch Pin | 0 |
| Relay Pin | 1 |

### Constants

The following constants are defined for managing various hardware components:

- `BUZZER`: `0b00000001`
- `LEDS`: `0b00001110`
- `RGB`: `0b01001110`
- `BUTTON`: `0b00100000`
- `PWOUT`: `0b00100000`
- `RELAY`: `0b10000000`
- `ALL`: `0b11111111`
- `OFF`: `0b00000000`

### Pin Initialization

The library includes logic to ensure pins are initialized only once, preventing errors in hardware manipulation. Each component's pin will be initialized the first time it is accessed.

## Usage

Here are some examples of how to use the `eiotlib.py` library to control components:

### Relay Control

```python
# Initialize the board
board = Board()

# Set the relay to ON (1) or OFF (0)
board.relay_set(1)  # Turn the relay on
board.relay_set(0)  # Turn the relay off
```

### Buzzer Control

```python
# Set the buzzer to a specific frequency (in Hz) and duration (in seconds)
board.buzzer_set(1000, 1)  # Play a tone at 1000 Hz for 1 second
```


### Read Button State

```python
# Get the current state of the button (1 if pressed, 0 otherwise)
state = board.button_get()
print("Button state:", state)
```

### Read Light Intensity (LDR)

```python
# Read the value from the photoresistor (light sensor)
light_value = board.ldr_get()
print("Light intensity:", light_value)
```

## License

This project is licensed under the MIT License.
