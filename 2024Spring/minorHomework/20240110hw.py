from PyQt6 import QtWidgets as Widgets
from PyQt6 import QtGui as Gui
from PyQt6 import QtCore as Core

class MainWindow(Widgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.feetInput = None
        self.convertResult = None

        self.setWindowTitle("F2MCT")
        self.resize(400,225)

        layout = Widgets.QVBoxLayout()

        self.label = Widgets.QLabel("Feet to Metres Conversion Tool")

        self.feetInputBox = Widgets.QLineEdit("Enter a number...")
        self.feetInputBox.textChanged.connect(self.feetInputChanged)

        self.feetUnit = Widgets.QLabel("feet(s)")
        self.metreUnit = Widgets.QLabel("metre(s)")
        self.equalSymbol = Widgets.QLabel("=")

        self.emptyLine = Widgets.QLabel("")

        self.convertButton = Widgets.QPushButton("Convert")
        self.convertButton.clicked.connect(self.convertButtonClicked)

        self.resultLabel = Widgets.QLabel("No result")

        layout.addWidget(self.label)
        layout.addWidget(self.emptyLine)
        layout.addWidget(self.feetInputBox)
        layout.addWidget(self.feetUnit)
        layout.addWidget(self.emptyLine)
        layout.addWidget(self.equalSymbol)
        layout.addWidget(self.emptyLine)
        layout.addWidget(self.resultLabel)
        layout.addWidget(self.metreUnit)
        layout.addWidget(self.emptyLine)
        layout.addWidget(self.convertButton)

        widget = Widgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
    
    def feetInputChanged(self, content):
        self.feetInput = content

    def convertButtonClicked(self):
        try:
            self.convertResult = (float(self.feetInput) / 3.281)
        except TypeError:
            self.convertResult = "error"
        except ValueError:
            self.convertResult = "error"
        self.resultLabel.setText(str(self.convertResult))

application = Widgets.QApplication([])
window = MainWindow()
window.show() 
application.exec()

print("Application stopped.")