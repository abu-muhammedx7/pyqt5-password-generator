from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class FuncGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.ImplementUi()
        
    def ImplementUi(self):
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        
        # creating header 
        
        self.label1 = QLabel()
        self.label1.setText("Secure Password")
        self.label1.setAlignment(Qt.AlignCenter)
        label2 = QLabel()
        label2.setText("Generate strong, secure passwords instantly")
        label2.setFont(QFont("Arial", 10))
        label2.setAlignment(Qt.AlignCenter)
        self.header_widget = QWidget()
        header_layout = QVBoxLayout()
        self.header_widget.setLayout(header_layout)
        header_layout.addWidget(self.label1)
        header_layout.addWidget(label2)
        self.main_layout.addWidget(self.header_widget)
       
        # main box
        self.main_box = QWidget()
        self.main_box_layout = QVBoxLayout()
        self.main_box.setLayout(self.main_box_layout)
        self.main_layout.addWidget(self.main_box)
        # Horizontal layout for display and btn
        lay1 = QHBoxLayout()
        self.display_ = QLineEdit()
        self.display_.setReadOnly(True)
        
        self.copy_btn = QPushButton("Copy")
        self.copy_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.copy_btn.setIcon(QIcon("assets/copy.png"))
        self.copy_btn.setIconSize(QSize(20, 29))
        self.copy_btn.clicked.connect(self.Copy)
        
        lay1.addWidget(self.display_)
        lay1.addWidget(self.copy_btn)
        self.main_box_layout.addLayout(lay1)
        
        #
        lay2 = QGridLayout()
        label3 = QLabel()
        label3.setText("Password Length: ")
        label3.setStyleSheet("font-size:16px; font-weight:bold; color:rgb(4, 0, 3); margin-left:15px;")
        label3.setFont(QFont("Gabriola", 16))
        self.passw_length = QLabel()
        self.passw_length.setText("12")
        self.passw_length.setStyleSheet("color:rgb(0, 255, 0); font-size:30px; font-weight:bold;")
        lay2.addWidget(label3, 0, 0)
        lay2.addWidget( self.passw_length, 0, 1)
        self.main_layout.addLayout(lay2)
        
        #
        self.quantity_ = QSlider(Qt.Horizontal)
        self.quantity_.setRange(4, 64)
        self.quantity_.setValue(12)
        self.quantity_.valueChanged.connect(self.range)
        
   
        self.main_layout.addWidget(self.quantity_)
        #
        # Character gridlayou
        gridlayou1 = QGridLayout()
        label4 = QLabel("Character types:")
        label4.setStyleSheet("font-size:19px; font-weight:bold; color:rgb(4, 0, 3); margin-left:15px;")
        label4.setFont(QFont("Gabriola", 19))
        self.chkA_Z = QCheckBox("Uppercase (A-Z)")
        self.chkA_Z.setChecked(True)
        self.chka_z = QCheckBox("Lowercase (a-z)")
        self.chka_z.setChecked(True)
        self.chk0_9 = QCheckBox("Numbers (0-9)")
        self.chk0_9.setChecked(True)
        self.chksymbol = QCheckBox("Symbols (#$?!&|@*%)")
        self.chksymbol.setChecked(True)
        
        gridlayou1.addWidget(label4, 0, 0)
        gridlayou1.addWidget(self.chkA_Z, 1, 0)
        gridlayou1.addWidget(self.chka_z, 1, 1)
        gridlayou1.addWidget(self.chk0_9, 1, 2)
        gridlayou1.addWidget(self.chksymbol, 1, 3)
        
        self.main_layout.addLayout(gridlayou1)
       
        # Generate buttton
        self.generate_btn = QPushButton("Generate Password")
        self.generate_btn.clicked.connect(self.generate_password)
        self.main_layout.addWidget(self.generate_btn, alignment=Qt.AlignCenter)
        self.generate_password()
        
     # Functionality function below 
    def Copy(self):
        clipboard = QGuiApplication.clipboard()
        clipboard.setText(self.display_.text())
        
    def generate_password(self):
            
        """Generate password based on current settings and ensure selected character types are included"""
        import random
        import string

        length = self.quantity_.value()
        has_upper = self.chkA_Z.isChecked()
        has_lower = self.chka_z.isChecked()
        has_number = self.chk0_9.isChecked()
        has_symbol = self.chksymbol.isChecked()

        symbol_chars = ['#', '$', '?', '!', '&', '|', '@', '*', '%']
        all_chars = ''
        password_chars = []

        # Ensure at least one character from each selected type is added
        if has_upper:
            password_chars.append(random.choice(string.ascii_uppercase))
            all_chars += string.ascii_uppercase
        if has_lower:
            password_chars.append(random.choice(string.ascii_lowercase))
            all_chars += string.ascii_lowercase
        if has_number:
            password_chars.append(random.choice(string.digits))
            all_chars += string.digits * 2
        if has_symbol:
            password_chars.append(random.choice(symbol_chars))
            all_chars += ''.join(symbol_chars * 2)

        if not all_chars:
            print("No character types selected.")
            return None, 0

        # Fill the rest of the password length with random choices from all allowed chars
        remaining_length = length - len(password_chars)
        password_chars += [random.choice(all_chars) for _ in range(remaining_length)]

        # Shuffle the final password to remove predictability
        random.shuffle(password_chars)
        password = ''.join(password_chars)

        self.display_.clear()
        self.display_.setText(password)
        
    def range(self):
        weak = [1, 2, 3, 4, 5, 6, 7]
        medium = [8, 9, 10, 11]
        strong = [i for i in range (12, 65)]
        if self.quantity_.value() in weak:
            self.passw_length.setText(str(self.quantity_.value()))
            self.passw_length.setStyleSheet("color:rgb(255, 4, 50); font-size:30px; font-weight:bold;")
        
        if self.quantity_.value() in medium:
            self.passw_length.setText(str(self.quantity_.value()))
            self.passw_length.setStyleSheet("color:rgb(252, 90, 10); font-size:30px; font-weight:bold;")
            
        if self.quantity_.value() in strong:
            self.passw_length.setText(str(self.quantity_.value()))
            self.passw_length.setStyleSheet("color:rgb(0, 255, 0); font-size:30px; font-weight:bold;")
