import sys
from PyQt5.QtWidgets import QMainWindow,QAction,QApplication

class menuTest(QMainWindow):
  def __init__(self, parent=None):
    super().__init__(parent)
    menubar = self.menuBar()
    # menubar .setNativeMenuBar(False)
    fileMenu = menubar.addMenu("File")
    itemNew = QAction("New",self)
    itemNew.setShortcut("Ctrl+N")
    fileMenu.addAction(itemNew)
    itemNew.triggered.connect(self.doNew)

  def doNew(self):
    print("New is triggered")

def main():
  app = QApplication(sys.argv)
  ex = menuTest()
  ex.show()
  sys.exit(app.exec_())

if __name__ == "__main__":
    main()
