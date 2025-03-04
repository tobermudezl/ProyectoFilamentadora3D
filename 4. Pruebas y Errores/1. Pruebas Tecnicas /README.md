# Proyecto: Pruebas y Mejoras en la Filamentadora

## Cambios y Mejoras Implementadas  

### Cambio de Driver: A8119 → ULN2003A  
Inicialmente usamos el driver **A8119**, pero tuvimos dificultades para hacerlo funcionar correctamente debido a la falta de documentación clara y problemas en la implementación. Después de varias pruebas, decidimos reemplazarlo por el **ULN2003A**, un driver más accesible y ampliamente utilizado para motores paso a paso pequeños. Este cambio nos permitió simplificar la conexión y el control del motor.  

### Cambio de Motores: NEFA → 28BYJ-48  
En las primeras pruebas, utilizamos motores **NEFA**, pero eran costosos y tenían un consumo de corriente mayor del esperado. Esto generó dificultades al usarlos con las fuentes de alimentación disponibles. Optamos por cambiarlos por los motores **28BYJ-48**, que son más económicos y compatibles con el **ULN2003A**. Aunque estos motores tienen menor torque, se ajustaron mejor a los requerimientos del proyecto.  

### Problemas con el Sensor de Temperatura DS18B20  
Uno de los mayores desafíos fue obtener lecturas correctas del sensor de temperatura **DS18B20**. Inicialmente, el sensor no enviaba datos o mostraba valores erróneos. Los principales errores encontrados fueron:  
- Falta de una resistencia pull-up de **4.7kΩ** en la línea de datos, lo que impedía la comunicación con el microcontrolador.  
- Uso de librerías incompatibles, que no permitían la correcta lectura del sensor.  
- Conexiones incorrectas en el circuito, lo que dificultaba la transmisión de datos.  

Tras múltiples pruebas, logramos obtener lecturas estables utilizando las librerías basicas

### Problemas con la Velocidad del Motor Paso a Paso  
Desde el inicio del proyecto, tuvimos dificultades para lograr que el motor se moviera a la velocidad deseada. Entre los problemas identificados estaban:  
- Uso de la función `delay()`, lo que afectaba el rendimiento y velocidad del motor.  
- Configuración incorrecta de la frecuencia de pasos, lo que generaba movimientos erráticos.  
- Uso de la librería `Stepper.h`, que no nos permitió un control preciso de la velocidad y aceleración.

Simplemente le damos un tiempo de descanso entre cada 90 grados

## Conclusiones  
Durante el semestre, enfrentamos varios problemas técnicos que nos obligaron a investigar, probar diferentes soluciones y mejorar nuestra comprensión del funcionamiento de los motores paso a paso y sensores. Aunque en algunos momentos fue complicado, logramos resolver los errores y mejorar el desempeño del prototipo.  

Este proyecto nos permitió aprender sobre la importancia de la documentación técnica, la depuración de código y la selección adecuada de componentes.  



