from PyQt6 import QtCore, QtGui, QtWidgets
import sys, os
import DialogWin
from pathlib import Path

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.getSettingValuesMain()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(311, 228)
        MainWindow.setMaximumSize(QtCore.QSize(315, 16777215))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(12, 12, 297, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(12, 57, 188, 16))
        self.label_2.setObjectName("label_2")
        self.organizeBtn = QtWidgets.QPushButton(self.centralwidget)
        self.organizeBtn.setGeometry(QtCore.QRect(10, 109, 291, 91))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.organizeBtn.setFont(font)
        self.organizeBtn.setStyleSheet("")
        self.organizeBtn.setObjectName("organizeBtn")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(13, 30, 288, 26))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(250, 21))
        self.lineEdit.setMaximumSize(QtCore.QSize(400, 30))
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.pushBtn.setMinimumSize(QtCore.QSize(0, 22))
        self.pushBtn.setMaximumSize(QtCore.QSize(30, 30))
        self.pushBtn.setObjectName("pushBtn")
        self.horizontalLayout.addWidget(self.pushBtn)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(12, 76, 168, 26))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.changeBtn = QtWidgets.QPushButton(self.layoutWidget1)
        self.changeBtn.setEnabled(True)
        self.changeBtn.setObjectName("changeBtn")
        self.horizontalLayout_2.addWidget(self.changeBtn)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 311, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Choose the folder where you want to organize files"))
        self.label_2.setText(_translate("MainWindow", "If you want to change folders name"))
        self.organizeBtn.setText(_translate("MainWindow", "Organize"))
        self.pushBtn.setText(_translate("MainWindow", "..."))
        self.label_3.setText(_translate("MainWindow", "for files, click ->"))
        self.changeBtn.setText(_translate("MainWindow", "Change"))

        self.pushBtn.clicked.connect(self.browseFolder)
        self.changeBtn.clicked.connect(self.openDialogWin)
        self.organizeBtn.clicked.connect(self.organizer)
        self.pathvalue = self.setting_variables.value('Path')
        self.lineEdit.setText(self.pathvalue)


    def browseFolder(self):
        folderPath = QtWidgets.QFileDialog.getExistingDirectory()
        if folderPath:
            self.lineEdit.setText(str(folderPath))
        

    def openDialogWin(self):
        self.window = QtWidgets.QDialog()
        self.ui = DialogWin.Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()
        self.setting_variables.setValue('line1', self.ui.textvalue)
        self.setting_variables.setValue('line2', self.ui.textvalue2)
        self.setting_variables.setValue('line3', self.ui.textvalue3)
        self.setting_variables.setValue('line4', self.ui.textvalue4)
        self.setting_variables.setValue('line5', self.ui.textvalue5)

    def getSettingValuesMain(self):
        self.setting_variables = QtCore.QSettings("AmanatPC", "Main Window Variables")


    def organizer(self):
        self.setting_variables.setValue('Path', self.lineEdit.text())        
        if not self.lineEdit.text():
            print('Enter a path')
        else:
            doc_types = ('.doc', '.docx', '.txt', '.pdf', '.xls', '.ppt', '.xlsx', '.pptx', '.csv')
            img_types = ('.jpg', '.jpeg', '.png', '.svg', '.gif')
            zip_types = ('.zip', '.tar', '.7z', '.rar', '.zipx')
            exe_types = ('.exe')
            copyPath = self.lineEdit.text()
            folder_elements = Path('{}'.format(copyPath))

            if str(self.setting_variables.value('line1')) == None or str(self.setting_variables.value('line1')) == '':
                docFolderName = 'Documents'
            else:
                docFolderName = self.setting_variables.value('line1')
            if str(self.setting_variables.value('line2')) == None or str(self.setting_variables.value('line2')) == '':
                imgFolderName = 'Images'
            else:
                imgFolderName = self.setting_variables.value('line2')
            if str(self.setting_variables.value('line3')) == None or str(self.setting_variables.value('line3')) == '':
                exeFolderName = 'Installers'
            else:
                exeFolderName = self.setting_variables.value('line3')
            if str(self.setting_variables.value('line4')) == None or str(self.setting_variables.value('line4')) == '':
                zipFolderName = 'Archives'
            else:
                zipFolderName = self.setting_variables.value('line4')
            if str(self.setting_variables.value('line5')) == None or str(self.setting_variables.value('line5')) == '':
                etcFolderName = 'Others'
            else:
                etcFolderName = self.setting_variables.value('line5')
                
            docFolder = '{}/{}'.format(copyPath, docFolderName)
            imgFolder = '{}/{}'.format(copyPath, imgFolderName)
            exeFolder = '{}/{}'.format(copyPath, exeFolderName)
            zipFolder = '{}/{}'.format(copyPath, zipFolderName)
            etcFolder = '{}/{}'.format(copyPath, etcFolderName)

            try:
                for files in folder_elements.iterdir():
                    if files.is_file():

                        fileformat = files.suffix
                        name = files.stem

                        doc_path = '{}/{}{}'.format(docFolder, name, fileformat)
                        img_path = '{}/{}{}'.format(imgFolder, name, fileformat)
                        exe_path = '{}/{}{}'.format(exeFolder, name, fileformat)
                        zip_path = '{}/{}{}'.format(zipFolder, name, fileformat)
                        etc_path = '{}/{}{}'.format(etcFolder, name, fileformat)

                        if not os.path.exists(docFolder):
                            os.makedirs(docFolder)
                        elif not os.path.exists(imgFolder):
                            os.makedirs(imgFolder)
                        elif not os.path.exists(exeFolder):
                            os.makedirs(exeFolder)
                        elif not os.path.exists(zipFolder):
                            os.makedirs(zipFolder)
                        elif not os.path.exists(etcFolder):
                            os.makedirs(etcFolder)

                        if fileformat in doc_types:
                            os.replace(files, doc_path)
                        elif fileformat in img_types:
                            os.replace(files, img_path)
                        elif fileformat in exe_types:
                            os.replace(files, exe_path)
                        elif fileformat in zip_types:
                            os.replace(files, zip_path)
                        else:
                            os.replace(files, etc_path)
                            
            except FileNotFoundError:
                pass
   

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())   