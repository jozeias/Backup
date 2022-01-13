from PyQt5.QtWidgets import *
import sys

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        layout = QGridLayout()  # Cria o grid layout
        self.setLayout(layout)
        self.texto = 'Meu texto com self'

        botao = QPushButton(self.texto)

        botao.clicked.connect(self.quando_clicar)
        layout.addWidget(botao, 0, 0)

    def quando_clicar(self):
        self.texto = 'Texto mudou!'


app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())