from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
Qt = QtCore.Qt

xl = pd.ExcelFile("SalesDataFull.xlsx")
OrdersOnlyData = xl.parse("Orders", index_col=0)
lines = "="*80

# date formating
headers = list(OrdersOnlyData.columns.values)
date_headers = headers[1:3]
for head in headers[:16]:
    if head in date_headers:
        OrdersOnlyData[head] = pd.to_datetime(OrdersOnlyData[head])


class Ui_analytics(object):
    #category method
   def category(self):
        SalesDataFull = pd.ExcelFile("SalesDataFull.xlsx")
        df = SalesDataFull.parse("Orders", index_col=0)
        category_column = df['Category']
        c = category_column.value_counts()
        c = category_column.value_counts().reset_index()
        c.columns = ['Category', 'Number of Sales']
        #pandas method conversion
        model = PandasModel(c)
        self.tableView.setModel(model)
        print(c)

   #region method 
   def region(self):
        SalesDataFull = pd.ExcelFile("SalesDataFull.xlsx")
        df = SalesDataFull.parse("Orders", index_col=0)
        region_column = df['Region']
        r = region_column.value_counts()
        r = region_column.value_counts().reset_index()
        r.columns = ['Region', 'Number of Sales']
        #pandas method conversion
        model = PandasModel(r)
        self.tableView.setModel(model)

   # profitability method
   def profitable(self):
        year = self.txtYear.text()
        month = self.txtMonth.text()
        if year.isdigit() and month.isdigit():
                #Data filtering
                orders_year = OrdersOnlyData.loc[OrdersOnlyData["Order Date"].dt.year == int(year)]
                orders_month = orders_year.loc[orders_year["Order Date"].dt.month == int(month)]
                prod_prof_col = orders_month[["Product Name", "Profit"]]
                prod_prof = prod_prof_col.groupby(by="Product Name").sum(
                ).sort_values(by="Profit", ascending=False).reset_index()
                #set filtered data to the pandas class
                
                model = PandasModel(prod_prof.head(10))

                self.tableView.setModel(model)
        else:
                self.showMessage("Error","Please input an integer")

   # unprofitability method
   def unprofitable(self):
        year = self.txtYear.text()
        month = self.txtMonth.text()
        if year.isdigit() and month.isdigit():
                #Data filtering
                orders_year = OrdersOnlyData.loc[OrdersOnlyData["Order Date"].dt.year == int(year)]
                orders_month = orders_year.loc[orders_year["Order Date"].dt.month == int(month)]
                prod_prof_col = orders_month[["Product Name", "Profit"]]
                prod_prof = prod_prof_col.groupby(by="Product Name").sum(
                ).sort_values(by="Profit", ascending=False).reset_index()
                #set filtered data to the pandas class
                model = PandasModel(prod_prof.tail(10))
                self.tableView.setModel(model)
        else:
                self.showMessage("Error","Please input an integer")

   #message box
   def showMessage (self,title,message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setText(message)
        msgBox.setWindowTitle(title)
        msgBox.exec_()

   # UI setup
   def setupUi(self, analytics):
       #form layout
        analytics.setObjectName("analytics")
        analytics.resize(480, 720)
        analytics.setWindowOpacity(1.0)
        analytics.setAutoFillBackground(False)
        analytics.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.5221, y1:0.568, x2:1, y2:1, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(analytics)
        self.verticalLayout_2.setContentsMargins(50, 50, 50, 50)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        #table view
        self.tableView = QtWidgets.QTableView(analytics)
        self.tableView.setAutoFillBackground(True)
        self.tableView.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)

        # label
        self.label_2 = QtWidgets.QLabel(analytics)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(67, 67, 67);\n" "background-color: rgba(255,255,255,0);")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)

        # year Text
        self.txtYear = QtWidgets.QLineEdit(analytics)
        self.txtYear.setMinimumSize(QtCore.QSize(0, 30))
        self.txtYear.setStyleSheet("background-color: rgba(255, 255, 255,.8)")
        self.txtYear.setObjectName("txtYear")
        self.verticalLayout.addWidget(self.txtYear)

        # label
        self.label_3 = QtWidgets.QLabel(analytics)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(67, 67, 67);\n" "background-color: rgba(255,255,255,0);")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)

        # Month text
        self.txtMonth = QtWidgets.QLineEdit(analytics)
        self.txtMonth.setMinimumSize(QtCore.QSize(0, 30))
        self.txtMonth.setStyleSheet("background-color: rgba(255, 255, 255,.7)")
        self.txtMonth.setObjectName("txtMonth")
        self.verticalLayout.addWidget(self.txtMonth)

        # top 10 button
        self.btnTopTen = QtWidgets.QPushButton(analytics)
        self.btnTopTen.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        self.btnTopTen.setFont(font)
        self.btnTopTen.setAutoFillBackground(False)
        self.btnTopTen.setStyleSheet("color: rgb(255, 255, 255);\n" "background-color: rgb(109, 109, 109);")
        self.btnTopTen.setFlat(True)
        self.btnTopTen.setObjectName("btnTopTen")
        self.verticalLayout.addWidget(self.btnTopTen)
        # button event
        self.btnTopTen.clicked.connect(self.profitable) 

        # Bottom button
        self.btnBotTen = QtWidgets.QPushButton(analytics)
        self.btnBotTen.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        self.btnBotTen.setFont(font)
        self.btnBotTen.setStyleSheet("color: rgb(109, 109, 109);\n" "background-color: rgb(255, 255, 255);")
        self.btnBotTen.setFlat(True)
        self.btnBotTen.setObjectName("btnBotTen")
        self.verticalLayout.addWidget(self.btnBotTen)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        QtCore.QMetaObject.connectSlotsByName(analytics)
        # button event
        self.btnBotTen.clicked.connect(self.unprofitable) 

        # region
        self.btnRegion = QtWidgets.QPushButton(analytics)
        self.btnRegion.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        self.btnRegion.setFont(font)
        self.btnRegion.setAutoFillBackground(False)
        self.btnRegion.setStyleSheet("color: rgb(255, 255, 255);\n" "background-color: rgb(109, 109, 109);")
        self.btnRegion.setFlat(True)
        self.btnRegion.setObjectName("btnRegion")
        self.verticalLayout.addWidget(self.btnRegion)
        # button event
        self.btnRegion.clicked.connect(self.region)

        # category
        self.btnCat = QtWidgets.QPushButton(analytics)
        self.btnCat.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        self.btnCat.setFont(font)
        self.btnCat.setAutoFillBackground(False)
        self.btnCat.setStyleSheet("color: rgb(255, 255, 255);\n" "background-color: rgb(255, 255, 255);")
        self.btnCat.setFlat(True)
        self.btnCat.setObjectName("btnCat")
        self.verticalLayout.addWidget(self.btnCat)
        # button event
        self.btnCat.clicked.connect(self.category) 
        self.retranslateUi(analytics)



   #setting texts for UI elements
   def retranslateUi(self, analytics):
        _translate = QtCore.QCoreApplication.translate
        analytics.setWindowTitle(_translate("analytics", "Insights"))
        self.label_2.setText(_translate("analytics", "Year:"))
        self.label_3.setText(_translate("analytics", "Month:"))
        self.btnTopTen.setText(_translate("analytics", "Top 10 products"))
        self.btnBotTen.setText(_translate("analytics", "Bottom 10 products"))
        self.btnRegion.setText(_translate("analytics", "Top Region"))
        self.btnCat.setText(_translate("analytics", "Top Categories"))

#pandas model
class PandasModel(QtCore.QAbstractTableModel):
    def __init__(self, data, parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self._data = data

    def rowCount(self, parent=None):
        return len(self._data.values)

    def columnCount(self, parent=None):
        return self._data.columns.size

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return QtCore.QVariant(str(
                    self._data.values[index.row()][index.column()]))
        return QtCore.QVariant()
