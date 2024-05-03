# Tarea 3.2 Caso practico Automata Finito

Un caso de uso real de un autómata finito es en el diseño y análisis de sistemas de control de acceso. Por ejemplo:

## Control de acceso a un edificio.

**Aplicación:** Control de acceso a un edificio.

**Implementación:** Se puede diseñar un autómata finito que represente el comportamiento del sistema de control de acceso. El autómata tendría estados que representan diferentes condiciones del sistema, como "Esperando tarjeta de acceso", "Verificando tarjeta", "Acceso permitido" y "Acceso denegado".

El autómata se implementaría utilizando un software de control de acceso que recibe entradas, como el escaneo de una tarjeta de acceso, y produce salidas, como la apertura de una puerta. Cada vez que se escanea una tarjeta, el autómata cambia de estado según las reglas definidas, por ejemplo, si la tarjeta es válida, el estado cambia a "Acceso permitido" y la puerta se abre; de lo contrario, cambia a "Acceso denegado" y la puerta permanece cerrada.

Esta implementación permite controlar el acceso al edificio de manera eficiente y segura, siguiendo un comportamiento predefinido que garantiza que solo las personas autorizadas puedan entrar. Además, el diseño del autómata facilita la comprensión y la modificación del sistema según sea necesario.

![image](https://github.com/UrielAhumada/Lenguajes_Automatas1/assets/160798678/09a376dd-9762-4b31-b6fd-2daf61df2473)

## Conclusion

Los autómatas finitos son una herramienta poderosa para diseñar sistemas de control de acceso eficientes y seguros, permitiendo una representación clara y concisa del comportamiento del sistema y facilitando su implementación y mantenimiento.
