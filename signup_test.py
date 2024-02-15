from PyQt5 import QtCore, QtGui, QtWidgets,uic
#import login files toget all it's classes
import login_test
import sys

class SignupWindow(QtWidgets.QMainWindow):
    def __init__(self):
        #we are calling all the attributes from parent class
        super().__init__()
        uic.loadUi('signup.ui',self)#inbuilt uic method with attribute  so in string we want file name and then we call the uic method itself by self



        #implementing button
        self.signup_button.clicked.connect(self.get_signup_name)
        self.signup_button.clicked.connect(self.get_signup_email)
        self.signup_button.clicked.connect(self.get_signup_passwd)

        #calling the go back to login button
        self.back_to_login_btn.clicked.connect(self.go_back_to_login) # it works
        #to close the signup window when back to login is clickew with inbuilt pyqt close function
        self.back_to_login_btn.clicked.connect(self.close)
        

        

    def get_signup_name(self):
        #definig the variable to store calling the object and passing it as plaintext by using toPlainText() method
        signup_name = self.signup_name.toPlainText()
        print("signup_name:",signup_name)
    
    def get_signup_email(self):
        #same as above comment
        signup_email = self.signup_email.toPlainText()
        print("signup_email:",signup_email)
    
    def get_signup_passwd(self):
        #same as above comment
        signup_passwd = self.signup_passwd.toPlainText()
        check_confirm_pwd = self.signup_reconfirm_passwd.toPlainText()
        if signup_passwd == check_confirm_pwd:
            print(f"the password matches with confirmation return password is {signup_passwd}")
        else:
            print("false")
    
    #making a function to go backa to login page(@ successful)
    def go_back_to_login(self):
        from login_test import Login_Window
        self.show_login = Login_Window()
        self.show_login.show()
    
    
        


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = SignupWindow()
    
    window.show()
    sys.exit(app.exec_())
    
   