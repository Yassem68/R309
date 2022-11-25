import sys 
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        widget = QWidget()
        self.setCentralWidget(widget)
        grid = QGridLayout()
        widget.setLayout(grid)
        self.__lab = QLabel("Saississez votre prénom")
        grid.addWidget(self.__lab, 1,1)
        ok = QPushButton("Ok")
        self.__text = QLineEdit()
        self.labprenom = QLabel("")
        self.resize(250, 100)
        quit = QPushButton("Quitter")
        grid.addWidget(self.__text, 2, 1, 1,1)
        grid.addWidget(self.labprenom, 4, 1, 1,1)
        grid.addWidget(ok, 3, 1, 1,1)
        grid.addWidget(quit, 5, 1, 1,1)
        ok.clicked.connect(self.__actionOk)
        self.setWindowTitle("Mon prénom")
        quit.clicked.connect(self.__actionQuitter)
    def __actionOk(self):
        prenom = self.__text.text()
        self.labprenom.setText(f"Salut {prenom}")
    def __actionQuitter(self):
        QCoreApplication.exit(0)
        


