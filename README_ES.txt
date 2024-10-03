Este proyecto utiliza Python 3 y PyQt6 (versión 6.7.0). A continuación se detallan las instrucciones para instalar las dependencias necesarias en Windows y macOS/Linux.

## Requisitos

- Python 3
- PyQt6 (versión 6.7.0)

## Instrucciones de Instalación

### Windows

1. **Instalar Python 3:**

   - Descarga el instalador de Python 3 desde la página oficial: [https://www.python.org/downloads/](https://www.python.org/downloads/)
   - Ejecuta el instalador y asegúrate de seleccionar la opción "Add Python to PATH" antes de instalar.

2. **Instalar PyQt6:**

   - Abre una terminal (puedes usar la terminal de Windows o PowerShell).
   - Ejecuta el siguiente comando para instalar PyQt6:

     ```sh
     pip install PyQt6==6.7.0
     ```

### macOS/Linux

1. **Instalar Python 3:**

   - En macOS, puedes instalar Python 3 usando Homebrew:

     ```sh
     brew install python
     ```

   - En Linux, puedes usar el gestor de paquetes de tu distribución. Por ejemplo, en Ubuntu:

     ```sh
     sudo apt update
     sudo apt install python3
     ```

2. **Instalar PyQt6:**

   - Abre una terminal.
   - Ejecuta el siguiente comando para instalar PyQt6:

     ```sh
     pip3 install PyQt6==6.7.0
     ```

## Verificación de la Instalación

Para verificar que tanto Python como PyQt6 están instalados correctamente, puedes ejecutar los siguientes comandos en tu terminal:

```sh
python --version
pip show PyQt6

## Inicialización

Para ejecutar la interfaz, es necesario ejecutar el script `main.py` desde una consola de comandos.

La interfaz proporciona las siguientes opciones:

1. Nombre del archivo 1 (núcleo):
   - Permite especificar el nombre del archivo que servirá como núcleo. Debe estar ubicado en la misma carpeta que el código o se puede seleccionar utilizando el botón "Explorar".

2. Valor de Épsilon 1:
   - Permite ingresar un valor para Épsilon 1, que representa la porosidad del núcleo y debe estar en el rango de -2.6 a 2.6. Utiliza el botón "<" para cambiar el símbolo y seleccionar si deseas mantener los valores mayores o menores que Épsilon 1.

3. Nombre del archivo 2 (corteza):
   - Permite especificar el nombre del archivo que servirá cómo corteza. Debe estar ubicado en la misma carpeta que el código o se puede seleccionar utilizando el botón "Explorar".

4. Valor de Épsilon 2:
   - Permite ingresar un valor para Épsilon 2, que representa la porosidad de la corteza y debe estar en el rango de -2.6 a 2.6. Debes respetar los símbolos de mayor o menor que según sea necesario.

5. Permutaciones:
   - Permite especificar las permutaciones, que deben ser números que cumplan con la función x² + y² + z² = Permutaciones. Algunos ejemplos válidos incluyen 9, 17, 21 y 22.

6. Nombre del resultado:
   - Permite especificar el nombre del archivo dónde se guardarán los resultados. Por defecto, el nombre es "Result".

Todos los resultados se guardarán automáticamente en una carpeta llamada "results", la cual será creada en la misma ubicación que el código.



