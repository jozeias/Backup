from PyQt5.QtWidgets import *

app = QApplication([])
class Janela(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Meu app com PyQt5')

        layout = QGridLayout()
        self.setLayout(layout)

        botao = QPushButton('texto')
        layout.addWidget(botao, 0, 0)


window = Janela()
window.show()
app.exec_()