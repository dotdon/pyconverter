# Python Script to Executable Converter

## Description

This application provides a simple graphical user interface (GUI) to convert Python scripts (`.py` files) into standalone executables (`.exe` files) on Windows. It also offers an optional feature to include a custom icon for the executable.

## Features

- Convert Python scripts to Windows executables.
- Optional selection of a custom icon for the executable.
- User-friendly GUI built with Tkinter and ttk.

## Requirements

- Python 3.x
- `pyinstaller` package

## Installation

1. **Install Python 3.x:** Make sure you have Python 3.x installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install PyInstaller:** Install the `pyinstaller` package using pip.

   ```bash
   pip install pyinstaller
   ```

3. **Download the Script:** Download or clone the repository containing the `converter.py` script.

## Usage

1. **Run the Script:** Open a terminal or command prompt, navigate to the directory containing `converter.py`, and run the script.

   ```bash
   python converter.py
   ```

2. **Use the GUI:**
   - Click the "Browse" button to select the Python script (`.py` file) you want to convert.
   - (Optional) Click the "Browse" button to select an icon file (`.ico`) for the executable.
   - Click the "Convert to .exe" button.
   - Select the output directory where you want to save the executable.
   - Wait for the conversion process to complete. A success message will appear once the executable is created.

## Screenshots

### Main Interface

![Main Interface](path/to/screenshot1.png)

### File Selection

![File Selection](path/to/screenshot2.png)

## Troubleshooting

- **PyInstaller Not Found:** If the application cannot find `pyinstaller`, it will prompt you to manually locate the `pyinstaller.exe` file. Ensure `pyinstaller` is installed and try again.
- **Conversion Errors:** If the conversion process fails, ensure your Python script is error-free and compatible with PyInstaller. Check the error message for details.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [PyInstaller](https://www.pyinstaller.org/) for making Python script conversion easy.
- [Tkinter](https://docs.python.org/3/library/tkinter.html) and [ttk](https://docs.python.org/3/library/tkinter.ttk.html) for the GUI components.
