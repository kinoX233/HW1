import sys
from api import *
from gui import *
from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication
if __name__ == '__main__':
    app = QApplication(sys.argv)

    #creat mainwindow
    mainwindow = QMainWindow()
    main_ui = Ui_MainWindow()
    main_ui.setupUi(mainwindow)

    #create subwindow
    subwindow = QDialog()
    sub_ui = Ui_Dialog()
    sub_ui.setupUi(subwindow)

    #after clicked, subwindow shows
    btn = main_ui.pushButton
    btn.clicked.connect( subwindow.show )#no parentheses() for function

    #post ip
    text = main_ui.textEdit.toPlainText()
    atom = atom()
    btn.clicked.connect( lambda: atom.get_loc(text) )

    #show mainwindow or quit
    mainwindow.show()
    sys.exit(app.exec_())

