from PyQt5.QtWidgets import *
from PyQt5 import QtCore
import sys


mensagem = 'Azul'
cont = 0
class Janela(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        layout = QGridLayout()
        self.setLayout(layout)

        texto = "Azul"

        botao = QPushButton(texto)
        botao.clicked.connect(self.quando_clicar)
        layout.addWidget(botao, 0, 0)


        botao02 = QPushButton('Branco')
        botao02.clicked.connect(self.clicado)
        layout.addWidget(botao02, 1, 0)

    def quando_clicar(self):
        print('Botão 01')
        self.setStyleSheet("background-color: rgb(23, 137, 213);")




    def clicado(self):
        mensagem = 'Você clicou'
        print('Botão 02')
        self.setStyleSheet("background-color: ")




app = QApplication(sys.argv)

tela = Janela()
tela.show()

sys.exit(app.exec_())