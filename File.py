from PyQt5 import QtCore, QtGui, QtWidgets
import sys

latest_directories = ["C:/Descktop","Drive A","Drive B","Drive C","..."]
Items = ["Videos","Pictures","Program Files","Musics","Games","Film"]

class Ui_Window(object):

    def __init__(self):

        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)

        self.frame = QtWidgets.QFrame(self.centralwidget)

        self.label = QtWidgets.QLabel(self.frame)

        self.lineEdit = QtWidgets.QLineEdit(self.frame)

        self.pushButton_2 = QtWidgets.QPushButton(self.frame)

        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)

        self.comboBox = QtWidgets.QComboBox(self.frame)

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)

        self.scrollAreaWidgetContents = QtWidgets.QWidget()

        self.gridLayoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)

        self.menuFile = QtWidgets.QMenu(self.menubar)

        self.menuEdit = QtWidgets.QMenu(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)

        self.actionOpen = QtWidgets.QAction(MainWindow)

        self.actionNew_file = QtWidgets.QAction(MainWindow)

        self.actionQuit = QtWidgets.QAction(MainWindow)

        self.actionCopy_Crtl_C = QtWidgets.QAction(MainWindow)

        self.actionPaste_Ctrl_V = QtWidgets.QAction(MainWindow)

        self.actionExit = QtWidgets.QAction(MainWindow)

        self.actionCopy = QtWidgets.QAction(MainWindow)

        self.actionCut = QtWidgets.QAction(MainWindow)

        self.actionPaste = QtWidgets.QAction(MainWindow)

        self.actionZip = QtWidgets.QAction(MainWindow)
    

    def HotKeyUi(self, MainWindow):

        _translate = QtCore.QCoreApplication.translate

        MainWindow.setWindowTitle(_translate("MainWindow", "File Manager"))

        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "my drives"))

        __sortingEnabled = self.treeWidget.isSortingEnabled()

        self.treeWidget.setSortingEnabled(False)

        self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "C"))

        self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "progs"))

        self.treeWidget.topLevelItem(0).child(1).setText(0, _translate("MainWindow", "shet"))

        self.treeWidget.topLevelItem(1).setText(0, _translate("MainWindow", "D"))

        self.treeWidget.topLevelItem(2).setText(0, _translate("MainWindow", "E"))

        self.treeWidget.topLevelItem(2).child(0).setText(0, _translate("MainWindow", "sdc"))

        self.treeWidget.topLevelItem(3).setText(0, _translate("MainWindow", "F"))

        self.treeWidget.topLevelItem(4).setText(0, _translate("MainWindow", "G"))

        self.treeWidget.setSortingEnabled(__sortingEnabled)

        self.label.setText(_translate("MainWindow", "File Manager "))

        self.lineEdit.setAccessibleName(_translate("MainWindow", "address bar"))

        self.menuFile.setTitle(_translate("MainWindow", "File"))

        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))

        self.actionOpen.setText(_translate("MainWindow", "open               Ctrl+O"))

        self.actionNew_file.setText(_translate("MainWindow", "new file          Ctrl+N"))

        self.actionQuit.setText(_translate("MainWindow", "Quit"))

        self.actionCopy_Crtl_C.setText(_translate("MainWindow", "Copy              Crtl+C"))

        self.actionPaste_Ctrl_V.setText(_translate("MainWindow", "Paste              Ctrl+V"))

        self.actionExit.setText(_translate("MainWindow", "Exit"))

        self.actionCopy.setText(_translate("MainWindow", "Copy       Crtl+C"))

        self.actionCut.setText(_translate("MainWindow", "Cut          Crtl+X"))

        self.actionPaste.setText(_translate("MainWindow", "Paste       Crtl+V"))

        self.actionZip.setText(_translate("MainWindow", "Zip"))




    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")

        MainWindow.resize(721, 511)

        icon = QtGui.QIcon()

        icon.addPixmap(QtGui.QPixmap("Title-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        MainWindow.setWindowIcon(icon)

        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)



        self.centralwidget.setObjectName("centralwidget")



        self.treeWidget.setGeometry(QtCore.QRect(20, 50, 181, 401))

        self.treeWidget.setObjectName("treeWidget")



        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)

        item_1 = QtWidgets.QTreeWidgetItem(item_0)

        item_1 = QtWidgets.QTreeWidgetItem(item_0)

        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)

        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)

        item_1 = QtWidgets.QTreeWidgetItem(item_0)

        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)

        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)





        self.frame.setGeometry(QtCore.QRect(100, 0, 671, 51))

        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)

        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)

        self.frame.setObjectName("frame")



        font = QtGui.QFont()

        font.setFamily("Comic Sans MS")

        font.setPointSize(18)

        font.setBold(True)

        font.setItalic(False)

        font.setUnderline(False)

        font.setWeight(75)

        font.setStrikeOut(False)

        font.setKerning(True)

        font.setStyleStrategy(QtGui.QFont.PreferAntialias)



        self.label.setGeometry(QtCore.QRect(30, 0, 181, 51))

        self.label.setFont(font)

        self.label.setMouseTracking(True)

        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)

        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)

        self.label.setTextFormat(QtCore.Qt.PlainText)

        self.label.setWordWrap(False)

        self.label.setObjectName("label")



        self.lineEdit.setGeometry(QtCore.QRect(250, 20, 370, 21))


        icon1 = QtGui.QIcon()



        self.pushButton_2.setGeometry(QtCore.QRect(220, 20, 21, 21))

        self.pushButton_2.setText("GO")

        self.pushButton_2.setIcon(icon1)

        self.pushButton_2.setIconSize(QtCore.QSize(20, 20))

        self.pushButton_2.setDefault(False)

        self.pushButton_2.setFlat(True)

        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_2.clicked.connect(self.Back)



        icon2 = QtGui.QIcon()



        self.pushButton_1.setGeometry(QtCore.QRect(670, 20, 21, 21))


        self.pushButton_1.setIcon(icon2)

        self.pushButton_1.setIconSize(QtCore.QSize(20, 20))

        self.pushButton_1.setDefault(False)

        self.pushButton_1.setFlat(True)

        self.pushButton_1.setObjectName("pushButton_3")

        



        MainWindow.setCentralWidget(self.centralwidget)


        self.comboBox.setGeometry(QtCore.QRect(250, 20, 390, 20))

        self.comboBox.setObjectName("comboBox")

        self.comboBox.raise_()


        self.label.raise_()

        self.lineEdit.raise_()

        self.pushButton_2.raise_()



        self.scrollArea.setGeometry(QtCore.QRect(210, 50, 481, 401))

        self.scrollArea.setFrameShape(QtWidgets.QFrame.StyledPanel)

        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Plain)

        self.scrollArea.setLineWidth(5)

        self.scrollArea.setWidgetResizable(True)

        self.scrollArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)

        self.scrollArea.setObjectName("scrollArea")



        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 479, 399))

        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")



        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 10, 461, 381))

        self.gridLayoutWidget.setObjectName("gridLayoutWidget")



        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_2.setObjectName("gridLayout_2")

       

        MainWindow.setCentralWidget(self.centralwidget)



        self.menubar.setGeometry(QtCore.QRect(0, 0, 721, 21))

        self.menubar.setObjectName("menubar")



        self.menuFile.setObjectName("menuFile")



        self.menuEdit.setObjectName("menuEdit")



        MainWindow.setMenuBar(self.menubar)



        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)



        self.actionOpen.setObjectName("actionOpen")



        self.actionNew_file.setObjectName("actionNew_file")



        self.actionQuit.setObjectName("actionQuit")



        self.actionCopy_Crtl_C.setObjectName("actionCopy_Crtl_C")



        self.actionPaste_Ctrl_V.setObjectName("actionPaste_Ctrl_V")



        self.actionExit.setObjectName("actionExit")



        self.actionCopy.setObjectName("actionCopy")



        self.actionCut.setObjectName("actionCut")



        self.actionPaste.setObjectName("actionPaste")



        self.actionZip.setObjectName("actionZip")



        self.menuFile.addAction(self.actionOpen)

        self.menuFile.addAction(self.actionNew_file)

        self.menuFile.addSeparator()

        self.menuFile.addSeparator()

        self.menuFile.addAction(self.actionExit)

        self.menuEdit.addAction(self.actionCopy)

        self.menuEdit.addAction(self.actionCut)

        self.menuEdit.addAction(self.actionPaste)

        self.menuEdit.addSeparator()

        self.menuEdit.addAction(self.actionZip)

        self.menubar.addAction(self.menuFile.menuAction())

        self.menubar.addAction(self.menuEdit.menuAction())

        self.show_items()

        self.recent_directories()



        self.HotKeyUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def show_items(self):

        i,j = 0,0

        for Item in Items :

            if j == 6 :

                j = 0

                i += 1     #it shows the Items in their proper location

            j += 1

            self.item = QtWidgets.QPushButton(self.centralwidget)

            self.item.setGeometry(QtCore.QRect(150 + j*80, 60 + i*80, 50, 50))

            self.item.setText(Item)

            icon2 = QtGui.QIcon()

                      
            MainWindow.setCentralWidget(self.centralwidget)





    def recent_directories(self):

        for i,directory in enumerate(latest_directories[-5:]):

            self.comboBox.addItem("")

            self.comboBox.setItemText(i,directory)

        print("POUYA")


    def Back(self):

        global pointer

        if len(directories)>1:

            self.Go_to_directory(directories[-2])

            directories.pop()

        else :

            self.Go_to_directory(directories[-1])




if __name__ == "__main__":


    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()

    ui = Ui_Window()

    ui.setupUi(MainWindow)

    MainWindow.show()

    sys.exit(app.exec_())
