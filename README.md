# Proyecto Urban Routes



Comprobación de lista de pruebas para la página de Urban Routes para que el usuario pueda pedir un taxi.
Se especifica el modo comfort, y el pago con tarjeta, todos los campos debe llenarse con la información otorgada en el archivo data.
Además la reserva  tiene especificaciones de requerimientos, como el pedir una manta y pañuelos, dos healdos y un mensaje personalizado para el conductor

Se necesitan comprobar 9 acciones:
1. Configurar la dirección.
2. Seleccionar la tarifa Comfort.
3. Rellenar el número de teléfono.
4. Agregar una tarjeta de crédito
5. Escribir un mensaje para el controlador.
6. Pedir una manta y pañuelos.
7. Pedir 2 helados.
8. Aparece el modal para buscar un taxi.
9. Esperar a que aparezca la información del conductor en el modal (opcional).

Nota:La última prueba se exceptúa ya que no es posible abrir la ventana para detectar el elemento requerido,
por lo tanto, no se puede usar un localizador.

\##Tecnología

Se utilizó el siguiente ambiente:

SO Windows 11 Home
Google Chrome Versión 146.0.7680.178 (Build oficial) (64 bits)

* Pycharm 2025.3.3
* GitHub
* Git Bash

\##Técnicas

* Localizadores:
  * By.ID
  * By.CLASS_NAME
  * By.CSS_SELECTOR
  * By.XPATH
* Importaciones de métodos:
  * by
  * expected_conditions
  * .send_keys
  * .get_property
  * .click
  * .text
  * .get
* Esperas explicitas con WebDriverWait
* Modelo POM

