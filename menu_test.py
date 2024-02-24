
from PyQt5 import QtCore, QtGui, QtWidgets,uic
class Module_menu(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('menu_design.ui',self)

        #calling the exp-tracker button
        self.exp_track_btn.clicked.connect(self.pop_easy_exp_tracker)
        #closing the menu screen when this button is press
        self.exp_track_btn.clicked.connect(self.close)

    #writing code to connect  Easy Expense Tracker
    def pop_easy_exp_tracker(self):
        #first importing expense tracker file
        from  expense_tracker import Expense_tracker
        #then creating an instance to open window
        self.exp_track = Expense_tracker()
        self.exp_track.show()
        #closing the Module_menu window in button
        

    




if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    window = Module_menu()
    window.show()
    app.exec_()


        
        
