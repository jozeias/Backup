from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QVBoxLayout, QTableWidgetItem, QHeaderView, QPushButton
import sys


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)


        self.title = 'Janela com PyQt5'
        self.left = 500
        self.top = 500
        self.width = 500
        self.height = 400

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.layout = QVBoxLayout()

        table_widget = QTableWidget()
        table_widget.setRowCount(5)
        table_widget.setColumnCount(3)

        table_widget.horizontalHeader().setStretchLastSection(True)
        table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        botao = QPushButton("Carregar")


        self.layout.addWidget(table_widget)
        self.layout.addWidget(botao)
        self.setLayout(self.layout)


app = QApplication(sys.argv)
janela = Window()
janela.show()

sys.exit(app.exec_())

