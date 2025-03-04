# platform: micropython-esp32
# send: wifi
# ip_mpy: 192.168.4.1
# serialport: 
# filename: main.py

import machine
from machine import Pin
from time import sleep_ms

# Definir los pines del ESP32 para controlar el driver ULN2003
pins = [Pin(21, Pin.OUT), Pin(19, Pin.OUT), Pin(18, Pin.OUT), Pin(5, Pin.OUT)]

# Secuencia para el motor paso a paso (modo de media fase)
secuencia = [
    [1, 0, 0, 1],
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1]
]

# Función para mover el motor "n" pasos
def mover_motor(pasos, delay=2):
    for _ in range(pasos):
        for sec in secuencia:
            for pin, val in zip(pins, sec):
                pin.value(val)
            sleep_ms(delay)

# Loop infinito para avanzar 90 grados cada 50ms
while True:
    mover_motor(128)  # Avanza 90 grados
    sleep_ms(50)  # Espera
