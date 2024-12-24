README - Hybrid Structures Model Generation Tool

DESCRIPTION
This tool is designed to process core-crust structure models in `.dump` format. It allows to separate the core from the cortex, apply constraints to the coordinates and generate output files ready to be validated and used in scientific visualization or 3D printing. The graphical interface, developed in PyQt6, makes it easy to use.

FEATURES
- Processes input files in `.dump` format.
- Separates the kernel from the cortex, working only with the kernel.
- Allows to configure constraints on the coordinates (X, Y, Z).
- Generates output files in `.dump` and `.stl` formats.

REQUIREMENTS
- Python 3.8 or higher.
- Required libraries: numpy, scipy, scikit-image, numpy-stl, PyQt6. 
 **Install the necessary dependencies:** **## Windows 10 or higher.
### Windows 10 or higher:

   - Open a terminal (you can use PowerShell).
   - Run the following command to install the required libraries:

     ```sh
     pip install numpy scipy scipy PyQt6==6.7.0 matplotlib numpy-stl
     ```

### macOS/Linux

1. **Install Python 3:**

   - On macOS, you can install Python 3 using Homebrew:

     ````sh
     brew install python
     brew install pyqt6

    or in official python installer:
     pip3 install pyqt6
     ```

   - On Linux, you can use the package manager of your distribution. For example, in Ubuntu:

     ````sh
     sudo apt update
     sudo apt install python3
     ```
2. Install the necessary dependencies:** **.

   - Open a terminal.
   - Run the following command to install the required libraries:

     ```sh
     pip3 install numpy scipy PyQt6==6.7.0 matplotlib numpy-stl
     ```
USE:

1. Place the input `.dump` files in the project folder.
2. Run the `main.py` file to start the process.

 When executed, a graphical interface will be displayed where the following instructions must be followed:
   
   The GUI allows you to load an input file using the **"Explore ”** button. This file must be of type LAMMPS , CU, TA, among other materials. In addition, the interface allows to configure constraints and output parameters in a simple way.

3. Configure the following parameters:
   - **Input File:** Select the input file .CU, .TA, etc.
   - E1 and E2:** Define the values and constraints (major or minor) for each data set.
   - Coordinates (X, Y, Z):** Enter the specific coordinates for the constraints, 100 1 100 is used for both cases.
   - Permutations F1 and F2:** Specifies the coordinate combinations for the generation of the files.
   - Output File Names:** Assigns names to the resulting files.
4. Press the **"Confirm ”** button to start processing. The program will generate the results automatically.

5. The results will be saved in:
   - `process_files/`: Intermediate files generated during the process.
   - results/`: Final files in `.dump` and `.stl` formats, ready for viewing or 3D printing.

OUTPUTS
- Dump files:** For molecular visualization in tools such as OVITO.
- .stl files:** For 3D printing.

VALIDATION
1. Scientific Visualization:
- Use OVITO to parse `.dump` files.
2. 3D Printing:
- Prepare the `.stl` files in Ultimaker Cura by adjusting orientation and parameters.
- The models can be printed with 3D printers, such as the Creality Ender-3.

PROJECT STRUCTURE
project/.
├── main.py # Main script.
├─── Soyarslan_no_cubico.py # Processing module
├─── process_files/ # Intermediate files
├── results/ # Output files
└─── README.txt # This documentation

AUTHORS
- **Luis Andaur** Luis.andaur@alu.ucm.cl
- **Felipe Morales** Felipe.morales.03@alu.ucm.cl

SUPPORT
For questions or problems, contact the authors of the project or check the comments inside the code.

LICENSE
This project is licensed under the MIT license.