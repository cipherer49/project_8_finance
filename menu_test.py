
from PyQt5 import QtCore, QtGui, QtWidgets,uic
class Module_menu(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('menu.ui',self)
    




if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    window = Module_menu()
    window.show()
    app.exec_()


        
        
