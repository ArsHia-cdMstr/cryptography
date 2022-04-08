import sys

from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow, QPushButton, QMessageBox

from IntToChar import intToChar
from MapCharToInt import MapCharToInt
from part2 import section2
from part5 import AbsoluteValue
from placement import placement
from sort import sort, bubbleSort


def processing(filename):
    file_r = open(filename, "r")  # read

    a = MapCharToInt(file_r.read()).get()
    print(a)

    b = section2(a)
    print(b)

    c = sort(b)
    print(c)

    d = bubbleSort(c)
    print(d)

    e = AbsoluteValue(d)
    print(e)

    f = placement(e)
    print(f)

    g = intToChar(f)
    print(g)

    file_w = open('file_w.txt', "w")  # write
    file_w.write(str(g))

    return g


def dialog():
    file, check = QFileDialog.getOpenFileName(None, "selection file", "", "Text Files (*.txt)")
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
                      "-------------------------\n\n" + result)
        alert.setWindowTitle("hmmmm")
        alert.exec()

    button.clicked.connect(on_button_clicked)

    win.show()

    sys.exit(app.exec_())


if __name__ == '__main__':

    ui()

