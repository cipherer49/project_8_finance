from PyQt5 import QtCore, QtGui, QtWidgets,uic
#import signup_test # to make signup_test file classes available

import menu_test #to make menu_test classes available
#adding extra sys module
import sys





class Login_Window(QtWidgets.QMainWindow): 
    def __init__(self):
        #we are calling all the attributes from parent class
        super().__init__()
        uic.loadUi('login.ui',self)#inbuilt uic method with attribute  so in string we want file name and then we call the uic method itself by self
       
       #@Login_button
        self.login_button.clicked.connect(self.take_login_name_and_pwd)# to get login_name when button is clicked
        #self.login_button.clicked.connect(self.take_login_pwd) # to get login_pwd when button is clicked
        #calling the login button to show module menu
        self.login_button.clicked.connect(self.call_menu_page)
        
        #closing the login_page when the logic is true
        #self.login_button.clicked.connect(sel)
        

        
        #@signup_button
        #calling the signup button
        self.signup_link_button.clicked.connect(self.call_signup_page)#works
        #mentioning close method in signup button to close login window by using pyqt inbuilt close methode
        self.signup_link_button.clicked.connect(self.close)

        
        
    def take_login_name_and_pwd(self):
        # assigning a variable so we are calling the plaintextedit object with its actual name and then adding toPlainText() method
        self.login_name = self.login_name_input.toPlainText()
        self.login_pwd = self.login_pwd_input.toPlainText()
        print(self.login_name)
        print(self.login_pwd)
        
        
        
        
    
    """def take_login_pwd(self):
        login_pwd = self.login_pwd_input.toPlainText() 
        print(login_pwd)"""
    
    #trying a simple function to open signup page(@ it works)
    def call_signup_page(self):
        from signup_test import SignupWindow
        # Create an instance of the SignupWindow class
        self.signup_window = SignupWindow()
        # Show the SignupWindow
        self.signup_window.show()
        
        

        
        

        
    
    def call_menu_page(self,take_login_name_and_pwd):
        from menu_test import Module_menu
        if self.login_name and self.login_pwd is not None:
            #creating an  instance for Module_menu class and using self to call it inside this method
            self.menu_page = Module_menu()
            #show the menu page
            self.menu_page.show()
            #when the logic is true calling the inbuilt qtwidget close method by self.close()
            self.close()
        else:
            print("input the abbove fields")
        



        
#for reference      
"""class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('login.ui', self)
        self.login_button.clicked.connect(self.print_something)
        

    def print_something(self):
        print("Button clicked")
        """        






if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Login_Window()
    window.show()
    sys.exit(app.exec_())

