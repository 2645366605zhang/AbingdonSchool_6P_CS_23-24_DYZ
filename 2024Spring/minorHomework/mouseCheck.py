from PyQt6 import QtWidgets as Widgets
from PyQt6 import QtGui as Gui
from PyQt6 import QtCore as Core

class MainWindow(Widgets.QMainWindow):

    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Mouse Checker")
        self.resize(800,450)

        layout = Widgets.QVBoxLayout()

        self.checkerButton = Widgets.QPushButton("Click here")
        self.checkerButton.pressed.connect(self.checkerButtonclicked)

        layout.addWidget(self.checkerButton)

        widget = Widgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    
    def checkerButtonclicked(self):
        self.successMessageBox = Widgets.QMessageBox.information(self, " ", "Congratulations! Your left mouse button works fine!", Widgets.QMessageBox.StandardButton.Ok)

application = Widgets.QApplication([])
window = MainWindow()
window.show() 
application.exec()

print("Application stopped.")