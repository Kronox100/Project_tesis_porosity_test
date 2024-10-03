This project uses Python 3 and PyQt6 (version 6.7.0). Below are the instructions for installing the necessary dependencies on Windows and macOS/Linux.

## Requirements

- Python 3
- PyQt6 (version 6.7.0)

## Installation Instructions

### Windows

1. **Install Python 3:**

   - Download the Python 3 installer from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)
   - Run the installer and make sure to check the "Add Python to PATH" option before installing.

2. **Install PyQt6:**

   - Open a terminal (you can use the Windows Command Prompt or PowerShell).
   - Run the following command to install PyQt6:

     ```sh
     pip install PyQt6==6.7.0
     ```

### macOS/Linux

1. **Install Python 3:**

   - On macOS, you can install Python 3 using Homebrew:

     ```sh
     brew install python
     ```

   - On Linux, you can use your distribution's package manager. For example, on Ubuntu:

     ```sh
     sudo apt update
     sudo apt install python3
     ```

2. **Install PyQt6:**

   - Open a terminal.
   - Run the following command to install PyQt6:

     ```sh
     pip3 install PyQt6==6.7.0
     ```

## Verifying the Installation

To verify that both Python and PyQt6 are installed correctly, you can run the following commands in your terminal:

```sh
python --version
pip show PyQt6

## Initialization

To run the interface, execute the `main.py` script from a command prompt.

The interface provides the following options:

1. File 1 name (core):
   - Allows you to specify the name of the file to be used as the core. It should be located in the same folder as the code or can be selected using the "Explore" button.

2. Epsilon 1 value:
   - Allows you to enter a value for Epsilon 1, representing the core porosity, which should range from -2.6 to 2.6. Use the "<" button to toggle and choose whether to include values greater than or less than Epsilon 1.

3. File 2 name (shell):
   - Allows you to specify the name of the file to be used as the crust. It should be located in the same folder as the code or can be selected using the "Explore" button.

4. Epsilon 2 value:
   - Allows you to enter a value for Epsilon 2, representing the crust porosity, which should range from -2.6 to 2.6. Respect the greater-than or less-than symbols as required.

5. Permutations:
   - Specifies the permutations, which must be numbers that satisfy the equation x² + y² + z² = Permutations. Some valid examples include 9, 17, 21, and 22.

6. Result name:
   - Allows you to specify the name of the file where the results will be saved. By default, the name is "Result".

All results will be automatically saved in a folder named "results", created in the same location as the code.

