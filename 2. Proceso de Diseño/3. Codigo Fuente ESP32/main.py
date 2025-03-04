platform: micropython-esp32
# send: wifi
# ip_mpy: 192.168.4.1
# serialport: 
# filename: main.py

import machine
import onewire
import ds18x20
import time

# Configuración del sensor DS18B20
PIN_SENSOR = 12  # GPIO12
TEMP_MIN = 18  # 0% corresponde a 18°C
TEMP_MAX = 120  # Ajusta este valor según la temperatura máxima del dispositivo
PIN_LED = 2  # LED integrado en el ESP32

# Inicializar sensor
pin_sensor = machine.Pin(PIN_SENSOR)
ow = onewire.OneWire(pin_sensor)
ds = ds18x20.DS18X20(ow)

# Buscar sensores
roms = ds.scan()
if not roms:
    print("No se encontró ningún sensor DS18B20")
    while True:
        pass
print("Sensor DS18B20 encontrado:", roms)

def calcular_porcentaje(temp):
    """Convierte la temperatura en un porcentaje entre 0% y 100%"""
    if temp <= TEMP_MIN:
        return 0
    elif temp >= TEMP_MAX:
        return 100
    else:
        return ((temp - TEMP_MIN) / (TEMP_MAX - TEMP_MIN)) * 100

while True:
    ds.convert_temp()  
    time.sleep_ms(750)  
    temp = ds.read_temp(roms[0])  

    if temp is None:
        print("Error al leer la temperatura")
        continue
porcentaje = calcular_porcentaje(temp)
    print(f"Temperatura: {temp:.2f}°C | Porcentaje: {porcentaje:.2f}%")

    # Simulación de envío de datos a una aplicación vía comunicación serial
    print(f"DATA:{porcentaje:.2f}")  # La app puede leer este formato

    time.sleep(1)


