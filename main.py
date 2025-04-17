"""
Author: ABU MUHAMMED

Password Generator GUI Application

This script initializes and launches a PyQt5-based password generator.
It consists of a main window (`GeneratorMain`) that hosts a central widget
responsible for password generation functionality and styling.

Modules:
- PyQt5.QtWidgets: For GUI components.
- functionality.FuncGenerator: Handles the logic for generating passwords.
- style.Style: Applies styles and theming to the generator UI.

Classes:
- GeneratorMain: Main application window that sets up geometry, title, 
  and central functionality widget.

Functions:
- main(): Initializes the QApplication, creates and shows the main window.

Usage:
Run this script directly to launch the password generator GUI.

Example:
    python main.py
"""


from PyQt5.QtWidgets import *
from functionality import FuncGenerator
from PyQt5.QtGui import QIcon
from style import Style

class GeneratorMain(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 600, 600)
        self.setWindowTitle("Password Generator")
        self.setWindowIcon(QIcon("assets/20944201.jpg"))
        self.generator = FuncGenerator()
        self.styles = Style(self.generator)
        self.setCentralWidget(self.generator)
        
        
        
def main():
    from sys import argv
    app = QApplication(argv)
    window = GeneratorMain()
    window.show()
    app.exec_()
    
if __name__ == "__main__":
    main()