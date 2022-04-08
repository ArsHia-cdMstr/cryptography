import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QFileDialog

from main import processing


def dialog():
    file, check = QFileDialog.getOpenFileName(None, "selection file",
                                              "", "Text Files (*.txt)")
    result = processing(file)
    return result


def ui():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setFixedHeight(438)
    win.setFixedWidth(960)
    win.setStyleSheet("background-image : url(image.jpg)")
    win.setWindowTitle("Cryptography")

    button = QPushButton(win)
    button.setFixedWidth(200)
    button.setFixedHeight(50)
    button.setStyleSheet("background-image : url(select.png)")
    button.move((960 - 200) / 2, (432 - 50) / 2)

    def on_button_clicked():
        result = dialog()

        alert = QMessageBox()
        alert.setText("Encryption was successful\n"
                      "-------------------------\n\n" + g)
        alert.setWindowTitle("hmmmm")
        alert.exec()

    button.clicked.connect(on_button_clicked)

    win.show()
    sys.exit(app.exec_())
