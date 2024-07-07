import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

def get_pyinstaller_path():
    try:
        result = subprocess.run(["where", "pyinstaller"], capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return None

class ConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Script to Executable Converter")

        self.frame = ttk.Frame(root, padding="10 10 10 10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.file_path = ""
        self.icon_path = ""
        self.pyinstaller_path = get_pyinstaller_path() or self.prompt_for_pyinstaller()
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.frame, text="Select a Python script to convert to .exe:").grid(column=1, row=1, sticky=tk.W)
        self.file_button = ttk.Button(self.frame, text="Browse", command=self.select_file)
        self.file_button.grid(column=2, row=1, sticky=tk.W)

        ttk.Label(self.frame, text="(Optional) Select an icon for the executable:").grid(column=1, row=2, sticky=tk.W)
        self.icon_button = ttk.Button(self.frame, text="Browse", command=self.select_icon)
        self.icon_button.grid(column=2, row=2, sticky=tk.W)

        self.convert_button = ttk.Button(self.frame, text="Convert to .exe", command=self.convert_to_exe)
        self.convert_button.grid(column=1, row=3, columnspan=2)

        for child in self.frame.winfo_children(): 
            child.grid_configure(padx=5, pady=5)

    def select_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Python files", "*.py")])
        if self.file_path:
            messagebox.showinfo("Selected File", f"Selected: {self.file_path}")

    def select_icon(self):
        self.icon_path = filedialog.askopenfilename(filetypes=[("Icon files", "*.ico")])
        if self.icon_path:
            messagebox.showinfo("Selected Icon", f"Selected: {self.icon_path}")

    def prompt_for_pyinstaller(self):
        path = filedialog.askopenfilename(title="Locate pyinstaller.exe", filetypes=[("Executable files", "*.exe")])
        if path:
            return path
        else:
            messagebox.showerror("Error", "PyInstaller not found. Please ensure it is installed and try again.")
            self.root.quit()

    def convert_to_exe(self):
        if not self.file_path:
            messagebox.showerror("Error", "Please select a Python script to convert.")
            return

        if not self.pyinstaller_path or not os.path.exists(self.pyinstaller_path):
            messagebox.showerror("Error", f"PyInstaller not found. Please ensure it is installed.")
            return

        output_dir = filedialog.askdirectory(title="Select Output Directory")
        if not output_dir:
            return

        command = [self.pyinstaller_path, "--onefile", "--noconsole", self.file_path, "--distpath", output_dir]
        if self.icon_path:
            command.extend(["--icon", self.icon_path])

        try:
            subprocess.run(command, check=True)
            messagebox.showinfo("Success", f"Executable created at {output_dir}")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Failed to create executable: {e}")
        except FileNotFoundError as e:
            messagebox.showerror("Error", f"File not found: {e}")

def main():
    root = tk.Tk()
    style = ttk.Style(root)
    style.theme_use('clam')  # Use 'clam' or other themes like 'alt', 'default', or 'classic'
    app = ConverterApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
