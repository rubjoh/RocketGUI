# Install pyqt6 on your system:
# 1. Open terminal 
# 2. Use command: pip3 install pyqt6
# 3. To open the designer, use command: pyqt6-tools designer
# NB: make sure python and pip is installed on your system 

# Alt method, if you can't install using terminal:
# Go to https://www.qt.io/download and download Qt
# Create accouunt using uit info
# Note that Qt takes a long time to install.

# Initialize QT
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
import sys


def main():
    app = QApplication(sys.argv)
    win = QMainWindow()
    # Define the window x, y, width, height
    win.setGeometry(500,500,600,600) 
    # Window title
    win.setWindowTitle("Test window") 

    # Create a test label
    label = QLabel(win)
    label.setText("Test label")
    # Define position (x,y) from the top left corner
    label.move(100, 100)  

    # Display window
    win.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    test the function:
    main()
