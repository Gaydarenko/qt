import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


def func():
    print("Some function")


def application():
    app = QApplication(sys.argv)
    window = QMainWindow()

    window.setWindowTitle("Simple application")
    window.setGeometry(700, 400, 350, 200)

    main_text = QtWidgets.QLabel(window)
    main_text.move(100, 100)
    main_text.setText("This is main text")
    main_text.adjustSize()

    button = QtWidgets.QPushButton(window)
    button.move(70, 150)
    button.setText("Push me")
    button.setFixedWidth(200)
    button.clicked.connect(func)

    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    application()
