from PyQt6 import QtWidgets as Widgets
from PyQt6 import QtGui as Gui
from PyQt6 import QtCore as Core

class MainWindow(Widgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Text Editor")
        self.resize(1600,900)

        buttonLayout = Widgets.QHBoxLayout()
        mainLayout = Widgets.QVBoxLayout()

        self.mainText = Widgets.QTextEdit()

        self.saveButton = Widgets.QPushButton("Save")
        self.saveButton.clicked.connect(self.saveButtonClicked)
        self.loadButton = Widgets.QPushButton("Load")
        self.loadButton.clicked.connect(self.loadButtonClicked)
        self.quitButton = Widgets.QPushButton("Quit")
        self.quitButton.clicked.connect(self.quitButtonClicked)

        buttonLayout.addWidget(self.saveButton)
        buttonLayout.addWidget(self.loadButton)
        buttonLayout.addWidget(self.quitButton)

        mainLayout.addWidget(self.mainText)

        mainLayout.addLayout(buttonLayout)

        widget = Widgets.QWidget()
        widget.setLayout(mainLayout)
        self.setCentralWidget(widget)
    
    def saveButtonClicked(self):
        filename, _ = Widgets.QFileDialog.getSaveFileName(self, "Save File", ".", "Text Files (*.txt *.html *.md *.markdown)")
        if filename == "":
            print("Cancelled.")
        else:
            print(f"File {filename} saved.")

    def loadButtonClicked(self):
        filename, _ = Widgets.QFileDialog.getOpenFileName(self, "Open File", ".", "Text Files (*.txt *.html *.md *.markdown)")
        if filename == "":
            print("Cancelled.")
        else:
            print(f"File {filename} opened.")

    def quitButtonClicked(self):
        self.quitConfirmMessageBox = Widgets.QMessageBox.warning(self, "Confirmation", f"Are you sure?", Widgets.QMessageBox.StandardButton.Yes, Widgets.QMessageBox.StandardButton.No)

application = Widgets.QApplication([])
window = MainWindow()
window.show() 
application.exec()

print("Application stopped.")