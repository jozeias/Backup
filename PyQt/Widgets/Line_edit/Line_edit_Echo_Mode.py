from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QWidget
from PyQt5.QtCore import Qt
import sys


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(QMainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle('Line edit com Echo Mode')

        label = QLabel("Texto")
        label.setAlignment(Qt.AlignHCenter)

        line_edit = QLineEdit()
        line_edit.setEchoMode(QLineEdit.Password)




        self.setCentralWidget(line_edit)




app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec_())
