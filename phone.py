import sys
from PyQt6.QtWidgets import *
class FlagMaker(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300, 200, 350, 300)

        self.name_text= QLabel("Имя", self)
        self.name_text.move(10,30 )
        self.name_str=QLineEdit(self)
        self.name_str.move(80,30)

        self.phone_text = QLabel("Телефон", self)
        self.phone_text.move(10, 70)
        self.phone_str = QLineEdit(self)
        self.phone_str.move(80, 70)

        self.btn = QPushButton('Добавить',self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(250, 50)
        self.btn.clicked.connect(self.hui)

        self.Text_list1 = QListWidget(self)
        self.Text_list1.move(10, 100)

    def hui(self):
        self.name=self.name_str.text()
        self.nomber = self.phone_str.text()

        self.print_text = f"{self.name} : {self.nomber}"
        self.Text_list1.addItem(self.print_text)

        self.name_str.clear()
        self.phone_str.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FlagMaker()
    ex.show()
    sys.exit(app.exec())
