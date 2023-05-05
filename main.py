import gui
import sys
from PyQt5.QtWidgets import QMainWindow, QDialog, QApplication
if __name__ == '__main__':
    app = QApplication(sys.argv)

    #creat mainwindow
    mainwindow = QMainWindow()
    main_ui = gui.Ui_MainWindow()
    main_ui.setupUi(mainwindow)

    #create subwindow
    subwindow = QDialog()
    sub_ui = gui.Ui_Dialog()
    sub_ui.setupUi(subwindow)

    #after clicked, subwindow shows
    btn = main_ui.pushButton
    btn.clicked.connect( subwindow.show )#no parentheses() for function

    #show mainwindow or quit
    mainwindow.show()
    sys.exit(app.exec_())
