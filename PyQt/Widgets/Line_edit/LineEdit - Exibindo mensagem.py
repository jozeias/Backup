from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QMessageBox, QVBoxLayout
import sys

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.layout = QVBoxLayout()
        self.lineedit = QLineEdit()

        self.botao = QPushButton("Exibir mensagem")
        self.botao.clicked.connect(self.mensagem)

        self.layout.addWidget(self.lineedit)
        self.layout.addWidget(self.botao)
        self.setLayout(self.layout)

    def mensagem(self):
        valorDoLineEdit = self.lineedit.text()
        QMessageBox.question(self,'Python/PyQt5', "Você escreveu:" + valorDoLineEdit, QMessageBox.Ok, QMessageBox.Ok)
        self.lineedit.setText("")

app = QApplication(sys.argv)
janela = Window()
janela.show()
sys.exit(app.exec_())
