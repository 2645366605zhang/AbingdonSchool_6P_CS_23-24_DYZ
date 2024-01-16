from PyQt6 import QtWidgets as Widgets
from PyQt6 import QtGui as Gui
from PyQt6 import QtCore as Core

class MainWindow(Widgets.QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Text Editor")
        self.resize(1600,900)

        self.currentFilePath = ""
        self.currentFileName = ""
        self.currentContent = ""
        self.currentLength = 0
        self.notYetSaved = True

        #buttonLayout = Widgets.QHBoxLayout()
        mainLayout = Widgets.QVBoxLayout()

        #self.saveAction = Gui.QAction("Save", self)
        #self.saveAction.setShortcut("Ctrl+Shift+S")
        #self.saveAction.triggered.connect(self.saveText)
        self.saveFileAction = Gui.QAction("Save File", self)
        self.saveFileAction.setShortcut("Ctrl+S")
        self.saveFileAction.triggered.connect(self.saveButtonClicked)
        self.saveNewFileAction = Gui.QAction("Save As New File", self)
        self.saveNewFileAction.setShortcut("Ctrl+Shift+S")
        self.saveNewFileAction.triggered.connect(self.saveAsNewFile)
        self.loadFileAction = Gui.QAction("Load File", self)
        self.loadFileAction.setShortcut("Ctrl+O")
        self.loadFileAction.triggered.connect(self.loadButtonClicked)
        self.quitAction = Gui.QAction("Quit", self)
        self.quitAction.triggered.connect(self.quitButtonClicked)

        #self.addAction(self.saveAction)

        menuBar = self.menuBar()
        self.fileMenu = menuBar.addMenu("&File")

        self.fileMenu.addAction(self.saveFileAction)
        self.fileMenu.addAction(self.saveNewFileAction)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.loadFileAction)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.quitAction)

        self.fileTitle = Widgets.QLabel("")

        self.mainText = Widgets.QTextEdit(self.currentContent)
        self.mainText.textChanged.connect(self.saveText)

        self.extraInformation = Widgets.QLabel(f"Current Length: {self.currentLength}")

        #self.saveButton = Widgets.QPushButton("Save")
        #self.saveButton.clicked.connect(self.saveButtonClicked)
        #self.loadButton = Widgets.QPushButton("Load")
        #self.loadButton.clicked.connect(self.loadButtonClicked)
        #self.quitButton = Widgets.QPushButton("Quit")
        #self.quitButton.clicked.connect(self.quitButtonClicked)

        #buttonLayout.addWidget(self.saveButton)
        #buttonLayout.addWidget(self.loadButton)
        #buttonLayout.addWidget(self.quitButton)

        mainLayout.addWidget(self.fileTitle)
        mainLayout.addWidget(self.mainText)
        mainLayout.addWidget(self.extraInformation)

        #mainLayout.addLayout(buttonLayout)

        widget = Widgets.QWidget()
        widget.setLayout(mainLayout)
        self.setCentralWidget(widget)
    
    def saveText(self):
        self.currentContent = self.mainText.toPlainText()
        self.currentLength = len(self.currentContent)
        self.extraInformation.setText(f"Current Length: {self.currentLength}")
        self.notYetSaved = True
        print("Saved file changed internally.")

    def saveButtonClicked(self):
        if self.currentFilePath:
            with open(self.currentFilePath, "w") as userFile:
                userFile.write(self.currentContent)
            self.extraInformation.setText(f"{self.currentFileName} saved.")
            self.notYetSaved = False
            print(f"File {self.currentFileName} saved.\nPath: {self.currentFilePath}")
        else:
            filename, _ = Widgets.QFileDialog.getSaveFileName(self, "Save File", ".", "Text Files (*.txt *.html *.md *.markdown *.json)")
            if filename:
                self.overwriteConfirmationMessageBox = Widgets.QMessageBox.warning(self, "Confirmation", "This file will overwrite another file if they have the same name. Proceed?", Widgets.QMessageBox.StandardButton.Yes, Widgets.QMessageBox.StandardButton.No)
                if self.overwriteConfirmationMessageBox == Widgets.QMessageBox.StandardButton.Yes:
                    self.currentFileName = filename.split("/")[-1]
                    self.fileTitle.setText(self.currentFileName)
                    self.currentFilePath = filename
                    with open(filename, "w") as userFile:
                        userFile.write(self.currentContent)
                    self.extraInformation.setText(f"{self.currentFileName} saved.")
                    self.notYetSaved = False
                    print(f"File {self.currentFileName} saved.\nPath: {filename}")
                else:
                    print("File saving cancelled.")
            else:
                print("File saving cancelled.")
    
    def saveAsNewFile(self):
        filename, _ = Widgets.QFileDialog.getSaveFileName(self, "Save File", ".", "Text Files (*.txt *.html *.md *.markdown *.json)")
        if filename:
            self.overwriteConfirmationMessageBox = Widgets.QMessageBox.warning(self, "Confirmation", "This file will overwrite another file if they have the same name. Proceed?", Widgets.QMessageBox.StandardButton.Yes, Widgets.QMessageBox.StandardButton.No)
            if self.overwriteConfirmationMessageBox == Widgets.QMessageBox.StandardButton.Yes:
                self.currentFileName = filename.split("/")[-1]
                self.fileTitle.setText(self.currentFileName)
                self.currentFilePath = filename
                with open(filename, "w") as userFile:
                    userFile.write(self.currentContent)
                self.notYetSaved = False
                print(f"File {self.currentFileName} saved.\nPath: {self.currentFilePath}")
            else:
                print("File saving cancelled.")
        else:
            print("File saving cancelled.")

    def loadButtonClicked(self):
        filename, _ = Widgets.QFileDialog.getOpenFileName(self, "Open File", ".", "Text Files (*.txt *.html *.md *.markdown *.json)")
        if filename:
            self.currentFileName = filename.split("/")[-1]
            self.fileTitle.setText(self.currentFileName)
            self.currentFilePath = filename
            with open(filename, "r") as userFile:
                self.currentContent = userFile.read()
            self.mainText.setPlainText(self.currentContent)
            print(f"File {self.currentFileName} opened.\nPath: {self.currentFilePath}")
        else:
            print("File laoding cancelled.")

    def quitButtonClicked(self):
        self.quitConfirmMessageBox = Widgets.QMessageBox.warning(self, "Confirmation", "Are you sure you want to quit?", Widgets.QMessageBox.StandardButton.Yes, Widgets.QMessageBox.StandardButton.No)
        if self.quitConfirmMessageBox == Widgets.QMessageBox.StandardButton.Yes:
            if self.notYetSaved:
                self.saveConfirmMessageBox = Widgets.QMessageBox.warning(self, "Confirmation", "File not saved since last edit. Save?", Widgets.QMessageBox.StandardButton.Yes, Widgets.QMessageBox.StandardButton.No)
                if self.saveConfirmMessageBox == Widgets.QMessageBox.StandardButton.Yes:
                    self.saveButtonClicked()
            self.close()

application = Widgets.QApplication([])
window = MainWindow()
window.show()
application.exec()

print("Application stopped.")