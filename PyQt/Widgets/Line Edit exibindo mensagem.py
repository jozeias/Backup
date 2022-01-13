import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit, QMessageBox

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Exibindo mensagem com LineEdit'
        self.left = 500
        self.top = 500
        self.width = 400
        self.height = 140
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Cria uma linha de texto
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280, 40)

        # Create a button in the window
        self.button = QPushButton('Exibir mensagem', self)
        self.button.move(20, 80)

        # connect button to function on_click
        self.button.clicked.connect(self.mensagem)
        self.show()


    def mensagem(self):
        textboxValue = self.textbox.text()
        QMessageBox.question(self, 'Message - pythonspot.com', "Você escreveu: " + textboxValue, QMessageBox.Ok, QMessageBox.Ok)
        self.textbox.setText("")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())