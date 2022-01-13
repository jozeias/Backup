from PyQt5.QtWidgets import *
import sys



class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        layout = QGridLayout()  # Cria o grid layout
        self.setLayout(layout)

        self.entrada_texto = QLineEdit()
        self.entrada_texto.returnPressed.connect(self.abre_dialog)
        layout.addWidget(self.entrada_texto, 0, 0)


    def abre_dialog(self):
        self.dialog = Dialog()
        self.dialog.show()

app = QApplication(sys.argv)

screen = Window()
screen.show()

sys.exit(app.exec_())