from PyQt6 import QtWidgets as Widgets
from PyQt6 import QtGui as Gui
from PyQt6 import QtCore as Core

class MainWindow(Widgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("20240112")
        self.resize(800,450)

        layout = Widgets.QVBoxLayout()

        self.openButton = Widgets.QPushButton("Open")
        self.openButton.clicked.connect(self.openButtonClicked)

        self.saveButton = Widgets.QPushButton("Save")
        self.saveButton.clicked.connect(self.saveButtonClicked)

        layout.addWidget(self.openButton)
        layout.addWidget(self.saveButton)

        widget = Widgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def openButtonClicked(self):
        filename, _ = Widgets.QFileDialog.getOpenFileName(self, "Open File", ".", "Text Files (*.txt *.html *.md *.markdown)")
        print(filename)

    def saveButtonClicked(self):
        filename, _ = Widgets.QFileDialog.getSaveFileName(self, "Save File", ".", "Text Files (*.txt *.html *.md *.markdown)")
        print(filename)

application = Widgets.QApplication([])
window = MainWindow()
window.show() 
application.exec()

print("Application stopped.")