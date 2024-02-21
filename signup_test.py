from PyQt5 import QtCore, QtGui, QtWidgets,uic
#import login files toget all it's classes
import login_test
import sys
#importing pymongo for database connectivity
import pymongo

class SignupWindow(QtWidgets.QMainWindow):
    def __init__(self):
        #we are calling all the attributes from parent class
        super().__init__()
        uic.loadUi('signup_design.ui',self)#inbuilt uic method with attribute  so in string we want file name and then we call the uic method itself by self

       

        #implementing button
        self.signup_button.clicked.connect(self.get_signup_name)
        self.signup_button.clicked.connect(self.get_signup_email)
        self.signup_button.clicked.connect(self.get_signup_passwd)
        #calling the signin method to add all values in collection
        self.signup_button.clicked.connect(self.signin)

        #calling the go back to login button
        self.back_to_login_btn.clicked.connect(self.go_back_to_login) # it works
        #to close the signup window when back to login is clickew with inbuilt pyqt close function
        self.back_to_login_btn.clicked.connect(self.close)
        

    #writing a (msaked function for my password and confirm password field
    

        
        

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
        #we have use qline edit so to retrive text we will use text()
        signup_passwd = self.signup_passwd.text()
        check_confirm_pwd = self.signup_reconfirm_passwd.text()
        if signup_passwd == check_confirm_pwd:
            print(f"the password matches with confirmation return password is {signup_passwd}")
        else:
            print("false")
    
    #making a function to go backa to login page(@ successful)
    def go_back_to_login(self):
        from login_test import Login_Window
        self.show_login = Login_Window()
        self.show_login.show()
    
    #writing a method to fill signup details and creating new account
    def signin(self):
        #connecting with my client
        self.myclient = pymongo.MongoClient("mongodb://localhost:27017")
        #using my premade database auth_db 
        self.mydb = self.myclient["auth_db"]
        #using my premade collection
        account_collection = self.mydb["accounts"]
        #calling the pyqt input textboxes and filling it in to database
        self.name = self.signup_name.toPlainText()
        self.email = self.signup_email.toPlainText()
        self.pwd = self.signup_passwd.text()

        #making a dictionary to add all the credentials
        signin_add = {"user_name":self.name,"user_email":self.email,"user_pwd":self.pwd}

        #adding the values to my collection by using pymongo insert_one method
        add_to_collection = account_collection.insert_one(signin_add)


        
    
        


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = SignupWindow()
    
    window.show()
    sys.exit(app.exec_())
    
   