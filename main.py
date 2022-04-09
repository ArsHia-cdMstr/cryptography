import sys

from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow, QPushButton, QMessageBox

from Map import Map
from MathOperation import MathOperation
from Sort import Sort
from placement import placement


def processing(filename):
    file_r = open(filename, "r")  # read

    a = Map().getInt(file_r.read())
    print(a)

    b = MathOperation().functionX(a)
    print(b)

    c = Sort(b).sort_by_sign()
    print(c)

    d = Sort(b).bubbleSort()
    print(d)

    e = MathOperation().AbsoluteValue(d)
    print(e)

    f = placement(e)
    print(f)

    g = Map().getString(f)
    print(g)

    file_w = open('file_w.txt', "w")  # write
    file_w.write(g)

    return g


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
        file, check = QFileDialog.getOpenFileName(None, "selection file", "", "Text Files (*.txt)")
        result = processing(file)

        alert = QMessageBox()
        alert.setText("Encryption was successful\n"
                      "-------------------------\n\n" + result)
        alert.setWindowTitle("hmmmm")
        alert.exec()

    button.clicked.connect(on_button_clicked)

    win.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    ui()
