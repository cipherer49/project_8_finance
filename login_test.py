from PyQt5 import QtCore, QtGui, QtWidgets,uic
import signup_test # to make signup_test file classes available
import menu_test #to make menu_test classes available
 




class Login_Window(QtWidgets.QMainWindow): 
    def __init__(self):
        #we are calling all the attributes from parent class
        super().__init__()
        uic.loadUi('login.ui',self)#inbuilt uic method with attribute  so in string we want file name and then we call the uic method itself by self
       
       #@Login_button
        self.login_button.clicked.connect(self.take_login_name)# to get login_name when button is clicked
        self.login_button.clicked.connect(self.take_login_pwd) # to get login_pwd when button is clicked
        #calling the login button to show module menu
        self.login_button.clicked.connect(self.call_menu_page)

        
        #@signup_button
        #calling the signup button
        self.signup_link_button.clicked.connect(self.call_signup_page)#works

        
        
    def take_login_name(self):
        # assigning a variable so we are calling the plaintextedit object with its actual name and then adding toPlainText() method
        login_name = self.login_name_input.toPlainText()
        print(login_name)
        
        
        
    
    def take_login_pwd(self):
        login_pwd = self.login_pwd_input.toPlainText() 
        print(login_pwd)
    
    #trying a simple function to open signup page(@ it works)
    def call_signup_page(self):
        #calling the inbuilt uic.loadui method with design file name
        uic.loadUi('signup.ui',self)
        #referencing the signup_test file with it's class and then show method with self
        signup_test.SignupWindow.show(self)
    
    def call_menu_page(self):
        uic.loadUi('menu.ui',self)
        #calling the file then its class and then show method and then passig self so that the show function can called his attributes
        menu_test.Module_menu.show(self)



        
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
    app = QtWidgets.QApplication([])
    window = Login_Window()
    
    window.show()
    app.exec_()
