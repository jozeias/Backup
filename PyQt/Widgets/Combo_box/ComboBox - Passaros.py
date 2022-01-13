from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QComboBox, QLabel
import sys

class Janela(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.combo_box = QComboBox()
        self.combo_box.addItem("Passaro")
        self.combo_box.addItem("Lagarto")
        self.combo_box.addItem("Peixe")
        self.combo_box.currentTextChanged.connect(self.Seleciona_Item_Combo_Box)

        self.label = QLabel("Escolha um animal")

        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.layout.addWidget(self.combo_box, 0,0)
        self.layout.addWidget(self.label, 1, 0)

    def Seleciona_Item_Combo_Box(self):
        text = self.combo_box.currentText()
        if text == 'Passaro':
            text = 'Você escolheu um animal que voa'
            self.label.setText(text)
            self.label.adjustSize()

        elif text == 'Lagarto':
            text = 'Você escolheu um animal que rasteja'
            self.label.setText(text)
            self.label.adjustSize()

        elif text == 'Peixe':
            text = 'Você escolheu um animal que nada'
            self.label.setText(text)
            self.label.adjustSize()


def Run_App():
    app = QApplication(sys.argv)
    janela = Janela()
    janela.show()
    sys.exit(app.exec_())

Run_App()


