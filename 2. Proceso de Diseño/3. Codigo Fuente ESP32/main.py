import machine
import onewire
import ds18x20
import time
from machine import Pin
import sys

# Configuración del sensor DS18B20
PIN_SENSOR = 12  # GPIO12
TEMP_MIN = 18  # 0% corresponde a 18°C
TEMP_MAX = 220  # Ajusta este valor según la temperatura máxima del dispositivo
TEMP_UMBRAL_ALTA = 100  # Temperatura máxima para activar motores
TEMP_UMBRAL_BAJA = 0  # Temperatura mínima para activar motores
PIN_LED = 2  # LED integrado en el ESP32

# Inicializar sensor
temp_sensor = machine.Pin(PIN_SENSOR)
ow = onewire.OneWire(temp_sensor)
ds = ds18x20.DS18X20(ow)

# Buscar sensores
roms = ds.scan()
if not roms:
    print("No se encontró ningún sensor DS18B20")
    while True:
        pass
print("Sensor DS18B20 encontrado:", roms)

# Definir los pines del ESP32 para controlar los drivers ULN2003
motor1_pins = [Pin(21, Pin.OUT), Pin(19, Pin.OUT), Pin(18, Pin.OUT), Pin(5, Pin.OUT)]
motor2_pins = [Pin(23, Pin.OUT), Pin(22, Pin.OUT), Pin(1, Pin.OUT), Pin(3, Pin.OUT)]
led = Pin(PIN_LED, Pin.OUT)

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

# Función para mover un motor "n" pasos
def mover_motor(pins, pasos, delay=2):
    for _ in range(pasos):
        for sec in secuencia:
            for pin, val in zip(pins, sec):
                pin.value(val)
            time.sleep_ms(delay)

while True:
    ds.convert_temp()
    time.sleep_ms(750)
    temp = ds.read_temp(roms[0])

    if temp is None:
        print("Error al leer la temperatura")
        continue
    
    print(f"Temperatura: {temp:.2f}°C")
    
    # Leer entrada serial para comando manual
    if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
        comando = sys.stdin.read(1).strip()
        if comando == "M":
            print("Comando manual recibido: Activando motores")
            mover_motor(motor1_pins, 128)
            mover_motor(motor2_pins, 128)
            led.value(1)

    # Activar motores si la temperatura es mayor a 100°C o menor a 0°C
    if temp >= TEMP_UMBRAL_ALTA or temp <= TEMP_UMBRAL_BAJA:
        print("Temperatura fuera de rango seguro, activando motores")
        mover_motor(motor1_pins, 128)
        mover_motor(motor2_pins, 128)
        led.value(1)  # Encender LED de estado
    else:
        led.value(0)  # Apagar LED cuando no está activo
    
    time.sleep(1)
