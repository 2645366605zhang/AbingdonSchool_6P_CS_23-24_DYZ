from PyQt6 import QtWidgets as Widgets
from PyQt6 import QtGui as Gui
from PyQt6 import QtCore as Core

class MainWindow(Widgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Placeholder")
        self.resize(800,450)

        layout = Widgets.QVBoxLayout()

        self.label = Widgets.QLabel("Widget Demo")

        self.comboBox = Widgets.QComboBox()
        self.comboBox.addItem("I")
        self.comboBox.addItem("II")
        self.comboBox.addItem("III")
        self.comboBox.addItem("IV")
        self.comboBox.addItem("V")

        self.checkBox0 = Widgets.QCheckBox("Choose this?")
        self.checkBox1 = Widgets.QCheckBox("And this?")
        self.checkBox2 = Widgets.QCheckBox("Maybe this?")

        self.lineEdit = Widgets.QLineEdit("Type here...")

        self.radioButton0 = Widgets.QRadioButton("This one?")
        self.radioButton1 = Widgets.QRadioButton("Or this one?")

        self.slider = Widgets.QSlider(Core.Qt.Orientation.Horizontal)
        self.slider.setMinimum(-100)
        self.slider.setMaximum(100)
        self.slider.setSingleStep(10)

        self.button0 = Widgets.QPushButton("Ok")
        self.button1 = Widgets.QPushButton("Cancel")

        layout.addWidget(self.label)
        layout.addWidget(self.comboBox)
        layout.addWidget(self.checkBox0)
        layout.addWidget(self.checkBox1)
        layout.addWidget(self.checkBox2)
        layout.addWidget(self.lineEdit)
        layout.addWidget(self.radioButton0)
        layout.addWidget(self.radioButton1)
        layout.addWidget(self.slider)
        layout.addWidget(self.button0)
        layout.addWidget(self.button1)

        widget = Widgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

application = Widgets.QApplication([])
window = MainWindow()
window.show() 
application.exec()

print("Application stopped.")