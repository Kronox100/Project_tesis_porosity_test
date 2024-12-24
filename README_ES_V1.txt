README - Herramienta de Generación de Modelos de Estructuras Híbridas

DESCRIPCIÓN
Esta herramienta está diseñada para procesar modelos de estructuras núcleo-corteza en formato `.dump`. Permite separar el núcleo de la corteza, aplicar restricciones a las coordenadas y generar archivos de salida listos para ser validados y utilizados en visualización científica o impresión 3D. La interfaz gráfica, desarrollada en PyQt6, facilita su uso.

CARACTERÍSTICAS
- Procesa archivos de entrada en formato `.dump`.
- Separa el núcleo de la corteza, trabajando solo con el núcleo.
- Permite configurar restricciones en las coordenadas (X, Y, Z).
- Genera archivos de salida en formatos `.dump` y `.stl`.

REQUISITOS
- Python 3.8 o superior.
- Librerías necesarias: numpy, scipy, scikit-image, numpy-stl, PyQt6. 
 **Instalar las dependencias necesarias:**
### Windows 10 o superior:

   - Abre una terminal (puedes usar PowerShell).
   - Ejecuta el siguiente comando para instalar las librerías requeridas:

     ```sh
     pip install numpy scipy PyQt6==6.7.0 matplotlib numpy-stl
     ```

### macOS/Linux

1. **Instalar Python 3:**

   - En macOS, puedes instalar Python 3 usando Homebrew:

     ```sh
     brew install python
     brew install pyqt6

    o en instalador de python oficial:
     pip3 install pyqt6
     ```

   - En Linux, puedes usar el gestor de paquetes de tu distribución. Por ejemplo, en Ubuntu:

     ```sh
     sudo apt update
     sudo apt install python3
     ```

2. **Instalar las dependencias necesarias:**

   - Abre una terminal.
   - Ejecuta el siguiente comando para instalar las librerías requeridas:

     ```sh
     pip3 install numpy scipy PyQt6==6.7.0 matplotlib numpy-stl
     ```
USO:

1. Coloca los archivos `.dump` de entrada en la carpeta del proyecto.
2. Ejecuta el archivo `main.py` para iniciar el proceso.

 Al ejecutarlo, se desplegará una interfaz gráfica donde se debe seguir las siguientes instrucciones:
   
   La interfaz gráfica permite cargar un archivo de entrada utilizando el botón **"Explore"**. Este archivo debe ser de tipo LAMMPS , CU, TA, entre otros materiales. Además, la interfaz permite configurar restricciones y parámetros de salida de manera sencilla.

3. Configura los siguientes parámetros:
   - **Input File:** Selecciona el archivo de entrada .CU, .TA, etc.
   - **E1 y E2:** Define los valores y restricciones (mayor o menor) para cada conjunto de datos.
   - **Coordenadas (X, Y, Z):** Ingresa las coordenadas específicas para las restricciones, se utilizan 100 1 100 para ambos casos.
   - **Permutations F1 y F2:** Especifica las combinaciones de coordenadas para la generación de los archivos.
   - **Output File Names:** Asigna nombres a los archivos resultantes.

4. Presiona el botón **"Confirm"** para iniciar el procesamiento. El programa generará los resultados automáticamente.

5. Los resultados se guardarán en:
   - `process_files/`: Archivos intermedios generados durante el proceso.
   - `results/`: Archivos finales en formatos `.dump` y `.stl`, listos para su visualización o impresión 3D.

SALIDAS
- **Archivos `.dump`:** Para visualización molecular en herramientas como OVITO.
- **Archivos `.stl`:** Para impresión 3D.

VALIDACIÓN
1. Visualización Científica:
- Usa OVITO para analizar los archivos `.dump`.
2. Impresión 3D:
- Prepara los archivos `.stl` en Ultimaker Cura ajustando orientación y parámetros.
- Los modelos pueden imprimirse con impresoras 3D, como la Creality Ender-3.

ESTRUCTURA DEL PROYECTO
project/
├── main.py                  # Main script
├── Soyarslan_no_cubico.py   # Processing module
├── process_files/           # Intermediate files
├── results/                 # Output files
└── README.txt               # This documentation

AUTORES
- **Luis Andaur**  		Luis.andaur@alu.ucm.cl
- **Felipe Morales**		Felipe.morales.03@alu.ucm.cl

SOPORTE
Para dudas o problemas, contacta a los autores del proyecto o revisa los comentarios dentro del código.

LICENCIA
Este proyecto está bajo la licencia MIT.

