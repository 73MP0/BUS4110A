#imported dependencies
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from logIn import LogInForm
import sqlite3

#UI 

class SignUpForm(object):
    #

    #sign up button method
    def signUp(self):
        try:
            conn = sqlite3.connect("OS_Employee.db") 
            #Text box variables
            EID = self.txtEID.text()
            PW = self.txtPW.text()
            FN = self.txtFname.text()
            LN = self.txtLname.text()
            EM = self.txtEmail.text()
            #SQL connection
            conn.execute("INSERT INTO Employee VALUES(?,?,?,?,?)",(EID, FN, LN, EM, PW))
            conn.commit()
            conn.close()
            #message box
            self.showMessage("Success","Success! You've been added to the database.")
        except sqlite3.Error as e:
            self.showMessage("Error",str(e))
        
    #login button method
    def login(self):
            self.window = QtWidgets.QWidget()
            self.ui = LogInForm()
            self.ui.setupUi(self.window)
            self.window.show()
            Form.close()

    #message box
    def showMessage (self,title,message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setText(message)
        msgBox.setWindowTitle(title)
        msgBox.exec_()

    #Form layout for responsive design
    def setupUi(self, Form):
        #form
        Form.setObjectName("Form")
        Form.resize(480, 720)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.5221, y1:0.568, x2:1, y2:1, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(50, 100, 50, 100)

        #label
        self.label = QtWidgets.QLabel(Form)
        self.label.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(67, 67, 67);\n""background-color: rgba(255,255,255,0);")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        #Employee ID text box
        self.txtEID = QtWidgets.QLineEdit(Form)
        self.txtEID.setMinimumSize(QtCore.QSize(0, 30))
        self.txtEID.setStyleSheet("background-color: rgba(255, 255, 255,1)")
        self.txtEID.setObjectName("txtEID")
        self.txtEID.setClearButtonEnabled(True)
        self.verticalLayout.addWidget(self.txtEID)

        #label 2
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(67, 67, 67);\n" "background-color: rgba(255,255,255,0);")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)

        #First name text box
        self.txtFname = QtWidgets.QLineEdit(Form)
        self.txtFname.setMinimumSize(QtCore.QSize(0, 30))
        self.txtFname.setStyleSheet("background-color: rgba(255, 255, 255,.9)")
        self.txtFname.setObjectName("txtFname")
        self.txtFname.setClearButtonEnabled(True)
        self.verticalLayout.addWidget(self.txtFname)

        #label 3
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(67, 67, 67);\n" "background-color: rgba(255,255,255,0);\n" "")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)

        #Last name text box
        self.txtLname = QtWidgets.QLineEdit(Form)
        self.txtLname.setMinimumSize(QtCore.QSize(0, 30))
        self.txtLname.setStyleSheet("background-color: rgba(255, 255, 255,.8)")
        self.txtLname.setObjectName("txtLname")
        self.txtLname.setClearButtonEnabled(True)
        self.verticalLayout.addWidget(self.txtLname)

        #label 4
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(67, 67, 67);\n" "background-color: rgba(255,255,255,0);")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)

        #E-mail text box
        self.txtEmail = QtWidgets.QLineEdit(Form)
        self.txtEmail.setMinimumSize(QtCore.QSize(0, 30))
        self.txtEmail.setStyleSheet("background-color: rgba(255, 255, 255,.7)")
        self.txtEmail.setObjectName("txtEmail")
        self.txtEmail.setClearButtonEnabled(True)
        self.verticalLayout.addWidget(self.txtEmail)

        #label 5
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(67, 67, 67);\n" "background-color: rgba(255,255,255,0);")
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)

        #password text box
        self.txtPW = QtWidgets.QLineEdit(Form)
        self.txtPW.setMinimumSize(QtCore.QSize(0, 30))
        self.txtPW.setStyleSheet("background-color: rgba(255, 255, 255,.6)")
        self.txtPW.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txtPW.setObjectName("txtPW")
        self.txtPW.setClearButtonEnabled(True)
        self.verticalLayout.addWidget(self.txtPW)

        #sign up button
        self.btnSignUp = QtWidgets.QPushButton(Form)
        self.btnSignUp.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        self.btnSignUp.setFont(font)
        self.btnSignUp.setAutoFillBackground(False)
        self.btnSignUp.setStyleSheet("color: rgb(255, 255, 255);\n" "background-color: rgb(109, 109, 109);")
        self.btnSignUp.setFlat(True)
        self.btnSignUp.setObjectName("btnSignUp")
        self.verticalLayout.addWidget(self.btnSignUp)
        # button click event for sign up
        self.btnSignUp.clicked.connect(self.signUp) 

        #Log In button 
        self.btnLogIn = QtWidgets.QPushButton(Form)
        self.btnLogIn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        self.btnLogIn.setFont(font)
        self.btnLogIn.setStyleSheet("color: rgb(109, 109, 109);\n" "background-color: rgb(255, 255, 255);")
        self.btnLogIn.setFlat(True)
        self.btnLogIn.setObjectName("btnLogIn")
        #Log In button click event
        self.btnLogIn.clicked.connect(self.login) 
        self.verticalLayout.addWidget(self.btnLogIn)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        #Form controls
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    #setting texts for UI elements
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Sign Up"))
        self.label.setText(_translate("Form", "Employee ID:"))
        self.label_2.setText(_translate("Form", "First Name:"))
        self.label_3.setText(_translate("Form", "Last Name:"))
        self.label_4.setText(_translate("Form", "E-mail:"))
        self.label_5.setText(_translate("Form", "Password"))
        self.btnSignUp.setText(_translate("Form", "Sign Up"))
        self.btnLogIn.setText(_translate("Form", "Log In"))

#initializing main page
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = SignUpForm()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
