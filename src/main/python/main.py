#imported dependencies
from PyQt5 import QtCore, QtGui, QtWidgets
from signUp import SignUpForm
import sqlite3

#UI
class LogInForm(object):
    # Login method
    def loginCheck(self):
        try:
            conn = sqlite3.connect("OS_Employee.db")
            EM = self.txtEM.text()
            PW = self.txtPW.text()
            result = conn.execute("SELECT * FROM Employee WHERE EMAIL = ? AND Password = ?",(EM,PW))
            if(len(result.fetchall()) != 0):
                #need to route to dashboard page
                print("user found")
            else:
                #need to alert the user that they are not in the system
                print("user not found")
        except sqlite3.Error as e:
            print(e)

    # sign up page method which will route to the sign up page
    def signUpPage(self):
        self.window = QtWidgets.QWidget()
        self.ui = SignUpForm()
        self.ui.setupUi(self.window)
        self.window.show()
        Form.close()

    #Form layout for responsive design, all objects are nested in this method
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(480, 720)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.5221, y1:0.568, x2:1, y2:1, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(50, 100, 50, 100)
        self.verticalLayout.setObjectName("verticalLayout")

        #labels
        self.label = QtWidgets.QLabel(Form)
        self.label.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("color: rgb(109, 109, 109);\n" "background-color: rgba(255,255,255,0);")
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        #Employee text box
        self.txtEM = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.txtEM.setFont(font)
        self.txtEM.setAutoFillBackground(False)
        self.txtEM.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtEM.setInputMask("")
        self.txtEM.setText("")
        self.txtEM.setAlignment(QtCore.Qt.AlignCenter)
        self.txtEM.setClearButtonEnabled(True)
        self.txtEM.setObjectName("txtEM")
        self.txtEM.setMinimumSize(QtCore.QSize(0, 30))
        self.verticalLayout.addWidget(self.txtEM)

        #label 2
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet("color: rgb(109, 109, 109);\n" "background-color: rgba(255,255,255,0);")
        self.label_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)

        #password textbox
        self.txtPW = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.txtPW.setFont(font)
        self.txtPW.setMinimumSize(QtCore.QSize(0, 30))
        self.txtPW.setCursor(QtGui.QCursor(QtCore.Qt.SizeVerCursor))
        self.txtPW.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtPW.setInputMask("")
        self.txtPW.setText("")
        self.txtPW.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtPW.setAlignment(QtCore.Qt.AlignCenter)
        self.txtPW.setReadOnly(False)
        self.txtPW.setPlaceholderText("")
        self.txtPW.setClearButtonEnabled(True)
        self.txtPW.setObjectName("txtPW")
        self.verticalLayout.addWidget(self.txtPW)

        #log in button
        self.btnLogIn = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.btnLogIn.setFont(font)
        self.btnLogIn.setAutoFillBackground(False)
        self.btnLogIn.setStyleSheet("color: rgb(255, 255, 255);\n" "background-color: rgb(109, 109, 109);")
        self.btnLogIn.setCheckable(False)
        self.btnLogIn.setAutoDefault(False)
        self.btnLogIn.setDefault(False)
        self.btnLogIn.setFlat(True)
        self.btnLogIn.setObjectName("btnLogIn")
        self.verticalLayout.addWidget(self.btnLogIn)
        # button click event for log in
        self.btnLogIn.clicked.connect(self.loginCheck)          

        #sign up button                       
        self.btnSignUp = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.btnSignUp.setFont(font)
        self.btnSignUp.setAutoFillBackground(False)
        self.btnSignUp.setStyleSheet("color: rgb(109, 109, 109);\n" "background-color: rgb(255, 255, 255)")
        self.btnSignUp.setFlat(True)
        self.btnSignUp.setObjectName("btnSignUp")
        self.verticalLayout.addWidget(self.btnSignUp)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        # button click event for sign up
        self.btnSignUp.clicked.connect(self.signUpPage)  

        #Form configurations
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    #setting texts for UI elements
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Log In"))
        self.label.setText(_translate("Form", "Employee ID:"))
        self.label_2.setText(_translate("Form", "Password:"))
        self.btnLogIn.setText(_translate("Form", "Log In"))
        self.btnSignUp.setText(_translate("Form", "Sign Up"))

#main argument to launch the page
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    Form = QtWidgets.QWidget()
    ui = LogInForm()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())