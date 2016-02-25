# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sys
import PyQt4.QtGui as QtGui


def on_click():
    pbutton.setText(" ^o^ ")
    
def main():
    global pbutton
    app = QtGui.QApplication(sys.argv)
    mainW = QtGui.QMainWindow()

    pbutton = QtGui.QPushButton("Hollo")
    def on_click():
        pbutton.setText("World!")

    pbutton.clicked.connect(on_click)
    mainW.setCentralWidget(pbutton)
    mainW.show()
    app.exec_()
    
if __name__ == '__main__':
    main()
