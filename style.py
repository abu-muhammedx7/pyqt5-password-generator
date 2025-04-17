from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Style(QWidget):
    def __init__(self, widget):
        super().__init__()
        self.widget = widget
        self.ImplementStyle()
        
    def ImplementStyle(self):
        self.widget.header_widget.setStyleSheet("""
                                                QWidget {
                                                    background-color: rgb(1, 1, 255);
                                                    border-radius:8px;
                                                    margin-top:5px;
                                                    margin-bottom:5px;
                                                    margin-right:5px;
                                                    margin-left:5px;
                                                }
                                        
                                               
                                                """)
        self.widget.label1.setStyleSheet("font-size:18px; font-weight:bold;")
        self.widget.setStyleSheet("""
                                  QWidget {
                                      background-color: transparent;
                                      font-size:14px;
                                  }
                                  QCheckBox {
                                            spacing: 4px;
                                            color: #333333;
                                            margin-right:2px;             
                                            margin-left: 14px;                          
                                            }
                                        
                                        QCheckBox::indicator {
                                            width: 18px;
                                            height: 18px;
                                            border: 2px solid #999999;
                                            border-radius: 3px;
                                            background: white;
                                        }
                                        
                                        QCheckBox::indicator:hover {
                                            border: 2px solid red;
                                        }
                                        
                                        QCheckBox::indicator:checked {
                                            background: #4a9df8;
                                            border: 2px solid #4a9df8;
                                            color: white;
                                        }
                                        
                                        QCheckBox::indicator:checked::after {
                                            content: "✓";
                                            font-weight: bold;
                                            font-size: 14px;
                                            padding-left: 2px;
                                        }
                                        
                                        QCheckBox::indicator:disabled {
                                            background: #eeeeee;
                                            border: 2px solid #cccccc;
                                        }
                                                                    
                                  """)
        self.widget.display_.setStyleSheet("""
                                           font-size:14px;
                                           font-weight:bold;
                                           color:rgb(0,55,20);
                                           background-color:rgb(250, 250, 250);
                                           border:1px solid white;
                                           border-radius:5px;
                                           height:50px;
                                           padding-left:10px;
                                           margin:5px;
                                           
                                           """)
        self.widget.copy_btn.setStyleSheet("""
                                           QPushButton {
                                                    background-color: transparent;
                                                    color: #1e88e5;  /* Blue text color */
                                                    border: 2px solid #1e88e5;
                                                    border-radius: 4px;
                                                    padding: 8px 16px;
                                                    font-weight: bold;
                                                }
                                                
                                                QPushButton:hover {
                                                    background-color: rgba(30, 136, 229, 0.1);  /* Light blue on hover */
                                                }
                                                
                                                QPushButton:pressed {
                                                    background-color: rgba(30, 136, 229, 0.2);  /* Slightly darker when pressed */
                                                    color: #1565c0;
                                                    border-color: #1565c0;
                                                }
                            
                                                QPushButton:disabled {
                                                    color: #90caf9;
                                                    border-color: #90caf9;
                                                }
                                            
                                           """)
        self.widget.quantity_.setStyleSheet("""
            QSlider{
                margin-left:30px;
                margin-right:30px;
            }
            /* Horizontal Groove */
            QSlider::groove:horizontal {
                height: 8px;
                background: #2d2d2d;
                
                border-radius: 3px;
            }

            /* Filled portion of the groove */
            QSlider::sub-page:horizontal {
                background: qlineargradient(x1:0, y1:0, x2:1, y1:0,
                    stop:0 #4a9df8, stop:0.5 #2e7cf6, stop:1 #1a5feb);
                border-radius: 4px;
            }

            /* Handle */
            QSlider::handle:horizontal {
                width: 20px;
                height: 20px;
                margin: -6px 0;
                background: qradialgradient(
                    cx:0.5, cy:0.5, radius: 0.5,
                    fx:0.5, fy:0.5,
                    stop:0 white, stop:0.6 #4a9df8, stop:1 #1a5feb);
                border: 2px solid rgba(255, 255, 255, 150);
                border-radius: 10px;
            }

            /* Handle when pressed */
            QSlider::handle:horizontal:pressed {
                background: qradialgradient(
                    cx:0.5, cy:0.5, radius: 0.5,
                    fx:0.5, fy:0.5,
                    stop:0 white, stop:0.4 #4a9df8, stop:1 #1a5feb);
                border: 2px solid rgba(255, 255, 255, 200);
            }

            /* Add tick marks if needed */
            QSlider::add-page:horizontal {
                background: #444;
            }
        """)
        
        self.widget.generate_btn.setStyleSheet("""
                                               QPushButton {
                                                    background-color: transparent;
                                                    color: #1e88e5;  /* Blue text color */
                                                    border: 2px solid #1e88e5;
                                                    border-radius: 4px;
                                                    padding: 8px 16px;
                                                    font-weight: bold;
                                                }
                                                
                                                QPushButton:hover {
                                                    background-color: rgba(30, 136, 229, 0.1);  /* Light blue on hover */
                                                }
                                                
                                                QPushButton:pressed {
                                                    background-color: rgba(30, 136, 229, 0.2);  /* Slightly darker when pressed */
                                                    color: #1565c0;
                                                    border-color: #1565c0;
                                                }
                            
                                                QPushButton:disabled {
                                                    color: #90caf9;
                                                    border-color: #90caf9;
                                                }
                                            
                                               """)
        
        print("Hello World")