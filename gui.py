import sys
from PySide6 import QtCore, QtGui
from PySide6.QtWidgets import (QWidget,QFileDialog,QComboBox,QLabel,QTextEdit,QVBoxLayout,QApplication,QHBoxLayout,QPushButton)
from script import convertTextToXLSX

class FileConverter(QWidget):

    def __init__(self):
        super().__init__()

        # all widgets
        self.fileChooseButton = QPushButton("Choose a File")
        self.fileChooseButton.clicked.connect(self.onFileChoose)
        self.inputInstructionText = QLabel("Paste the delimited data or ",alignment=QtCore.Qt.AlignCenter)
        self.inputArea = QTextEdit()
        self.inputArea.textChanged.connect(self.onTextChange)
        self.delimiter = QComboBox(self)
        self.delimiter.addItem("Comma(,)",",")
        self.delimiter.addItem("Pipe(|)","|")
        self.downloadButton = QPushButton("Download")
        self.downloadButton.setEnabled(False)
        self.downloadButton.clicked.connect(self.onDownload)

        # layout
        self.inputLayout = QHBoxLayout()
        self.inputLayout.addWidget(self.inputInstructionText) 
        self.inputLayout.addWidget(self.fileChooseButton)

        self.optionLayout = QHBoxLayout()
        self.optionLayout.addWidget(self.delimiter)
        self.optionLayout.addWidget(self.downloadButton)   

        self.layout = QVBoxLayout()
        self.layout.addLayout(self.inputLayout)
        self.layout.addWidget(self.inputArea)
        self.layout.addLayout(self.optionLayout)
        self.setLayout(self.layout)


    @QtCore.Slot()
    def onFileChoose(self):
        print("choosing a file...")
        filename,_ = QFileDialog.getOpenFileName(self,("Open File"), "", ("Delimited Files(*.csv *.txt )"))
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                content = file.read()
                print("content of file",file," is ",content)
                self.inputArea.setPlainText(content)
        except FileNotFoundError:
            print(f"Error: The file '{filename}' was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    @QtCore.Slot()
    def onTextChange(self):
        text = self.inputArea.toPlainText();
        if(text and not text.isspace()):
            self.downloadButton.setEnabled(True)
        else:
            self.downloadButton.setEnabled(False)

    @QtCore.Slot()
    def onDownload(self):
        print("downloading a file...")
        filename,_ = QFileDialog.getSaveFileName(self,("Save File"), "untitled.xlsx", ("Excel File(*.xlsx)"))
        # assuming filename ends in xlsx
        seperator = self.delimiter.currentData()
        text = self.inputArea.toPlainText();
        convertTextToXLSX(text,seperator,filename)
        
        
app = QApplication(sys.argv)
widget = FileConverter()
widget.resize(800, 600)
widget.show()
sys.exit(app.exec())
