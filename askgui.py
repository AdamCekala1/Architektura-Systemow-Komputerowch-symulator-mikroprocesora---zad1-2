# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Adam\Desktop\ask_gui\ask.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    class Rejestr():
        wartosc = 0
        wartoscL = 0
        imie = ""


        def zwrocWartosc(self):
            return self.wartosc


        def __init__(self, imie_rej):
                self.imie = imie_rej
                self.wartosc = 0


        def grajImie(self):
            return self.imie


        def odejmnij(self, wart, ktoraCzesc):
            if (ktoraCzesc == "H"):
                liczba = self.zmienDlaH(wart)
            else:
                self.wartoscL = wart
                liczba = wart
            self.wartosc = self.wartosc - liczba
            if self.wartosc < 0:
                self.wartosc = abs(self.wartosc)


        def przesun(self, wart, lCzyH):
            self.wartosc = self.wartosc - self.wartoscL
            if lCzyH == "L":
                self.wartoscL = wart
                self.wartosc = self.wartosc + self.wartoscL
            else:
                self.wartosc = wart


        def add2(self, wart, ktoraCzesc):
            if (ktoraCzesc == "L"):
                self.wartoscL = self.wartoscL + wart
                if self.wartoscL > 255:
                    self.wartoscL = self.wartoscL%255
                self.wartosc = self.wartosc + wart
            if(ktoraCzesc == "H"):
                liczba = self.zmienDlaH(wart)
                self.wartosc = self.wartosc + liczba
            if self.wartosc >65535 :
                self.wartosc = abs(65535 - self.wartosc)


        def zmienDlaH(self, wartosc):
            slownik = {9:256, 8:512, 7:1024, 6:2048, 5:4096, 4:8192, 3:16384, 2:32768}
            sting = str(bin(wartosc))
            liczba = 0

            for i in range(2, sting.__len__()):
                if int(sting[i]) == 1:
                    liczba = liczba + slownik.get(i)
            return liczba
    def interpretujPracaKrok(self):


        slownikRej = {"rAXh": self.rejestA, "rAXl": self.rejestA, "rBXh": self.rejestB, "rBXl": self.rejestB, "rCXh": self.rejestC, "rCXl": self.rejestC, "rDXh": self.rejestD, "rDXl": self.rejestD }
        slownikMlodosci = {"rAXh": "H", "rAXl": "L", "rBXh": "H", "rBXl": "L", "rCXh": "H", "rCXl": "L", "rDXh":"H", "rADl": "L" }

        sting = self.tekst
        rozkaz = ""
        rejA = ""
        rejB = ""
        licz = 0
        numer = "0"
        ii = self.iPracaKrok + 1

        for i in range(ii, sting.__len__()):
            if sting[i].isspace():
                licz = licz+1

            if licz == 0 and sting[i].isdigit():
                    numer = sting[i]
            if licz == 1:
                if not(sting[i].isspace() or sting[i].isdigit()):
                    rozkaz = rozkaz + (sting[i])
            if licz == 2:
                if not(sting[i].isspace() or sting[i].isdigit()):
                    rejA = rejA + (sting[i])
            if licz == 3:
                if not(sting[i].isspace()):
                    rejB = rejB + (sting[i])
            if licz == 4:
                self.iPracaKrok = i
                rejestr = slownikRej.get(rejA)
                dodaj = 0
                if rejB.isdigit():
                    dodaj = rejB
                else:
                    dodajR = slownikRej.get(rejB)
                    dodaj = dodajR.zwrocWartosc()

                if rozkaz == "ADD":
                    lCzyH = slownikMlodosci.get(rejA)
                    #rejestr.dodaj(int(dodaj))
                    rejestr.add2(int(dodaj), slownikMlodosci.get(rejA))
                if rozkaz == "SUB":
                    lCzyH = slownikMlodosci.get(rejA)
                    rejestr.odejmnij(int(dodaj), lCzyH)
                if rozkaz == "MOV":
                    lCzyH = slownikMlodosci.get(rejA)
                    rejestr.przesun(int(dodaj), lCzyH)
                tekst = numer + " Rejestr " + rejestr.grajImie() + "  " + str(rejestr.zwrocWartosc()) +"\n"
                self.ui.textBrowser_2.setText(tekst)
                break


    def interpretuj(self):

        slownikRej = {"rAXh": self.rejestA, "rAXl": self.rejestA, "rBXh": self.rejestB, "rBXl": self.rejestB, "rCXh": self.rejestC, "rCXl": self.rejestC, "rDXh": self.rejestD, "rDXl": self.rejestD }
        slownikMlodosci = {"rAXh": "H", "rAXl": "L", "rBXh": "H", "rBXl": "L", "rCXh": "H", "rCXl": "L", "rDXh":"H", "rADl": "L" }

        sting = self.tekst
        rozkaz = ""
        rejA = ""
        rejB = ""
        licz = 0
        for i in range(sting.__len__()):
            if sting[i].isspace():
                licz = licz+1

            if licz == 1:
                if not(sting[i].isspace() or sting[i].isdigit()):
                    rozkaz = rozkaz + (sting[i])
            if licz == 2:
                if not(sting[i].isspace() or sting[i].isdigit()):
                    rejA = rejA + (sting[i])
            if licz == 3:
                if not(sting[i].isspace()):
                    rejB = rejB + (sting[i])
            if licz == 4:

                rejestr = slownikRej.get(rejA)
                dodaj = 0
                if rejB.isdigit():
                    dodaj = rejB
                else:
                    dodajR = slownikRej.get(rejB)
                    dodaj = dodajR.zwrocWartosc()

                if rozkaz == "ADD":
                    lCzyH = slownikMlodosci.get(rejA)
                    rejestr.add2(int(dodaj), slownikMlodosci.get(rejA))
                if rozkaz == "SUB":
                    lCzyH = slownikMlodosci.get(rejA)
                    rejestr.odejmnij(int(dodaj), lCzyH)
                if rozkaz == "MOV":
                    lCzyH = slownikMlodosci.get(rejA)
                    rejestr.przesun((dodaj), lCzyH)

                rozkaz= ""
                rejA = ""
                rejB = ""
                licz = 0

        tekst = ""
        for i in range(4):
            tekst = tekst + "Rejestr " + self.tabRejestow[i].grajImie() + "  " + str(self.tabRejestow[i].zwrocWartosc()) +"\n"

        self.ui.textBrowser_2.setText(tekst)


    def wpisz(self):
        self.tekst = open('instrukcje.txt').read()
        self.ui.textBrowser.setText(self.tekst)
        self.i = int(open('i.txt').read())

    def zapisz(self):
        plik = open('instrukcje.txt', 'w')
        plik.write(self.tekst)
        plik.close()
        plik = open('i.txt', 'w')
        plik.write(str(self.i))
        plik.close()


    def rozwiazuj(self):
        komenda = False
        rejestr1 = False
        rejestr2 = False
        tekst = ""
        if self.ui.ADD.isChecked():
            tekst = tekst + "ADD "
            komenda = True
        if self.ui.SUB.isChecked():
            tekst = tekst + "SUB "
            komenda = True
        if self.ui.MOV.isChecked():
            tekst = tekst + "MOV "
            komenda = True

        if self.ui.AXH.isChecked():
            tekst = tekst + "rAXh "
            rejestr1 = True
        if self.ui.AXL.isChecked():
            tekst = tekst + "rAXl "
            rejestr1 = True
        if self.ui.BXH.isChecked():
            tekst = tekst + "rBXh "
            rejestr1 = True
        if self.ui.BXL.isChecked():
            tekst = tekst + "rBXl "
            rejestr1 = True
        if self.ui.CXH.isChecked():
            tekst = tekst + "rCXh "
            rejestr1 = True
        if self.ui.CXL.isChecked():
            tekst = tekst + "rCXl "
            rejestr1 = True
        if self.ui.DXH.isChecked():
            tekst = tekst + "rDXh "
            rejestr1 = True
        if self.ui.DXL.isChecked():
            tekst = tekst + "rDXl "
            rejestr1 = True


        if self.ui.AXH_2.isChecked():
            tekst = tekst + "rAXh"
            rejestr2 = True
        if self.ui.AXL_2.isChecked():
            tekst = tekst + "rAXl"
            rejestr2 = True
        if self.ui.BXH_2.isChecked():
            tekst = tekst + "rBXh"
            rejestr2 = True
        if self.ui.BXL_2.isChecked():
            tekst = tekst + "rBXl"
            rejestr2 = True
        if self.ui.CXH_2.isChecked():
            tekst = tekst + "rCXh"
            rejestr2 = True
        if self.ui.CXL_2.isChecked():
            tekst = tekst + "rCXl"
            rejestr2 = True
        if self.ui.DXH_2.isChecked():
            tekst = tekst + "rDXh"
            rejestr2 = True
        if self.ui.DXL_2.isChecked():
            tekst = tekst + "rDXl"
            rejestr2 = True
        if self.ui.DXL_3.isChecked():
            tekst = tekst + str(self.ui.horizontalSlider.value())
            rejestr2 = True

        if self.ui.MOV.isChecked() and self.ui.DXL_3.isChecked():
            self.ui.textBrowser_2.setText("Niepoprawna komenda!")
        else:
            if(komenda and rejestr1 and rejestr2):
                self.ui.textBrowser_2.setText("")
                tekst = str(self.i)+ " " + tekst
                self.i = self.i + 1
                self.tekst = self.tekst + tekst +"\n"
                self.ui.textBrowser.setText(self.tekst)
            else:
                self.ui.textBrowser_2.setText("Niepoprawna komenda!")

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(700, 739)
        Form.setStyleSheet("QWidget{\n"
"background:#424f6d;\n"
"}\n"
"QFrame:hover{\n"
"border-width:5px;\n"
"border-style:solid;\n"
"border-color:    #69d28b;\n"
"}\n"
"QFrame,QRadioButton{\n"
"background:#299c9a;\n"
"}\n"
"QRadioButton{\n"
"color:#fff;\n"
"}\n"
"QRadioButton:hover{\n"
"background:#424f6d;\n"
"}\n"
"QPushButton{\n"
"background:#424f6d;\n"
"color:#fff;\n"
"}\n"
"#start,#save{\n"
"background:    #cc0033;\n"
"}\n"
"#start:hover,#save:hover{\n"
"background:    #e6334d;\n"
"}\n"
"QPushButton:hover{\n"
"background:#45637e;\n"
"}\n"
"QTextBrowser,QTextEdit{\n"
"background:#fff;\n"
"}\n"
"QLabel{\n"
"color:#fff;\n"
"border-style: solid;\n"
" border-width: 5px;\n"
"border-color:#424f6d;\n"
"}")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(10, 10, 451, 80))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.DXH = QtWidgets.QRadioButton(self.frame)
        self.DXH.setGeometry(QtCore.QRect(320, 50, 41, 17))
        self.DXH.setObjectName("DXH")
        self.CXL = QtWidgets.QRadioButton(self.frame)
        self.CXL.setGeometry(QtCore.QRect(270, 50, 41, 17))
        self.CXL.setObjectName("CXL")
        self.DXL = QtWidgets.QRadioButton(self.frame)
        self.DXL.setGeometry(QtCore.QRect(380, 50, 41, 17))
        self.DXL.setObjectName("DXL")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 10, 101, 31))
        self.label.setObjectName("label")
        self.AXH = QtWidgets.QRadioButton(self.frame)
        self.AXH.setGeometry(QtCore.QRect(20, 50, 41, 17))
        self.AXH.setObjectName("AXH")
        self.AXL = QtWidgets.QRadioButton(self.frame)
        self.AXL.setGeometry(QtCore.QRect(70, 50, 41, 17))
        self.AXL.setObjectName("AXL")
        self.CXH = QtWidgets.QRadioButton(self.frame)
        self.CXH.setGeometry(QtCore.QRect(220, 50, 41, 17))
        self.CXH.setObjectName("CXH")
        self.BXL = QtWidgets.QRadioButton(self.frame)
        self.BXL.setGeometry(QtCore.QRect(170, 50, 41, 17))
        self.BXL.setObjectName("BXL")
        self.BXH = QtWidgets.QRadioButton(self.frame)
        self.BXH.setGeometry(QtCore.QRect(120, 50, 41, 17))
        self.BXH.setObjectName("BXH")
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(10, 100, 451, 80))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.DXH_2 = QtWidgets.QRadioButton(self.frame_2)
        self.DXH_2.setGeometry(QtCore.QRect(320, 50, 41, 17))
        self.DXH_2.setObjectName("DXH_2")
        self.CXL_2 = QtWidgets.QRadioButton(self.frame_2)
        self.CXL_2.setGeometry(QtCore.QRect(270, 50, 41, 17))
        self.CXL_2.setObjectName("CXL_2")
        self.DXL_2 = QtWidgets.QRadioButton(self.frame_2)
        self.DXL_2.setGeometry(QtCore.QRect(380, 50, 41, 17))
        self.DXL_2.setObjectName("DXL_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 101, 31))
        self.label_2.setObjectName("label_2")
        self.AXH_2 = QtWidgets.QRadioButton(self.frame_2)
        self.AXH_2.setGeometry(QtCore.QRect(20, 50, 41, 17))
        self.AXH_2.setObjectName("AXH_2")
        self.AXL_2 = QtWidgets.QRadioButton(self.frame_2)
        self.AXL_2.setGeometry(QtCore.QRect(70, 50, 41, 17))
        self.AXL_2.setObjectName("AXL_2")
        self.CXH_2 = QtWidgets.QRadioButton(self.frame_2)
        self.CXH_2.setGeometry(QtCore.QRect(220, 50, 41, 17))
        self.CXH_2.setObjectName("CXH_2")
        self.BXL_2 = QtWidgets.QRadioButton(self.frame_2)
        self.BXL_2.setGeometry(QtCore.QRect(170, 50, 41, 17))
        self.BXL_2.setObjectName("BXL_2")
        self.BXH_2 = QtWidgets.QRadioButton(self.frame_2)
        self.BXH_2.setGeometry(QtCore.QRect(120, 50, 41, 17))
        self.BXH_2.setObjectName("BXH_2")
        self.frame_3 = QtWidgets.QFrame(Form)
        self.frame_3.setGeometry(QtCore.QRect(10, 190, 451, 80))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.MOV = QtWidgets.QRadioButton(self.frame_3)
        self.MOV.setGeometry(QtCore.QRect(30, 20, 82, 41))
        self.MOV.setObjectName("MOV")
        self.SUB = QtWidgets.QRadioButton(self.frame_3)
        self.SUB.setGeometry(QtCore.QRect(180, 20, 82, 41))
        self.SUB.setObjectName("SUB")

        # QtCore.QObject.connect(self.ui.DODAJ, QtCore.SIGNAL("clicked()"), self.rozwiazuj)
        # QtCore.QObject.connect(self.ui.ZapiszZm, QtCore.SIGNAL("clicked()"), self.zapisz)
        # QtCore.QObject.connect(self.ui.Wpisz, QtCore.SIGNAL("clicked()"), self.wpisz)
        # QtCore.QObject.connect(self.ui.Graj, QtCore.SIGNAL("clicked()"), self.interpretuj)
        # QtCore.QObject.connect(self.ui.PracaKrok, QtCore.SIGNAL("clicked()"), self.interpretujPracaKrok)


        self.ADD = QtWidgets.QRadioButton(self.frame_3)
        self.ADD.setGeometry(QtCore.QRect(330, 20, 82, 41))
        self.ADD.setObjectName("ADD")
        self.frame_4 = QtWidgets.QFrame(Form)
        self.frame_4.setGeometry(QtCore.QRect(470, 10, 221, 121))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 71, 31))
        self.label_3.setObjectName("label_3")
        self.textEdit = QtWidgets.QTextEdit(self.frame_4)
        self.textEdit.setGeometry(QtCore.QRect(20, 70, 171, 31))
        self.textEdit.setObjectName("textEdit")
        self.lcdNumber = QtWidgets.QLCDNumber(self.frame_4)
        self.lcdNumber.setGeometry(QtCore.QRect(110, 30, 64, 23))
        self.lcdNumber.setObjectName("lcdNumber")
        self.frame_5 = QtWidgets.QFrame(Form)
        self.frame_5.setGeometry(QtCore.QRect(10, 280, 681, 191))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.textBrowser = QtWidgets.QTextBrowser(self.frame_5)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 451, 171))
        self.textBrowser.setObjectName("textBrowser")
        self.start = QtWidgets.QPushButton(self.frame_5)
        self.start.setGeometry(QtCore.QRect(490, 10, 171, 171))
        self.start.setObjectName("start")
        self.frame_6 = QtWidgets.QFrame(Form)
        self.frame_6.setGeometry(QtCore.QRect(10, 550, 681, 181))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.frame_6)
        self.textBrowser_2.setGeometry(QtCore.QRect(10, 10, 451, 161))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.czytaj = QtWidgets.QPushButton(self.frame_6)
        self.czytaj.setGeometry(QtCore.QRect(490, 10, 171, 161))
        self.czytaj.setObjectName("czytaj")
        self.frame_7 = QtWidgets.QFrame(Form)
        self.frame_7.setGeometry(QtCore.QRect(470, 140, 221, 131))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.krokowa = QtWidgets.QPushButton(self.frame_7)
        self.krokowa.setGeometry(QtCore.QRect(20, 20, 181, 41))
        self.krokowa.setObjectName("krokowa")
        self.calosciowa = QtWidgets.QPushButton(self.frame_7)
        self.calosciowa.setGeometry(QtCore.QRect(20, 70, 181, 41))
        self.calosciowa.setObjectName("calosciowa")
        self.save = QtWidgets.QPushButton(Form)
        self.save.setGeometry(QtCore.QRect(10, 480, 681, 61))
        self.save.setObjectName("save")

        self.ADD.clicked.connect(self.rozwiazuj)
        self.save.clicked.connect(self.zapisz)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.DXH.setText(_translate("Form", "DXH"))
        self.CXL.setText(_translate("Form", "CXL"))
        self.DXL.setText(_translate("Form", "DXL"))
        self.label.setText(_translate("Form", "Rejestr A"))
        self.AXH.setText(_translate("Form", "AXH"))
        self.AXL.setText(_translate("Form", "AXL"))
        self.CXH.setText(_translate("Form", "CXH"))
        self.BXL.setText(_translate("Form", "BXL"))
        self.BXH.setText(_translate("Form", "BXH"))
        self.DXH_2.setText(_translate("Form", "DXH"))
        self.CXL_2.setText(_translate("Form", "CXL"))
        self.DXL_2.setText(_translate("Form", "DXL"))
        self.label_2.setText(_translate("Form", "Rejestr B"))
        self.AXH_2.setText(_translate("Form", "AXH"))
        self.AXL_2.setText(_translate("Form", "AXL"))
        self.CXH_2.setText(_translate("Form", "CXH"))
        self.BXL_2.setText(_translate("Form", "BXL"))
        self.BXH_2.setText(_translate("Form", "BXH"))
        self.MOV.setText(_translate("Form", "MOV"))
        self.SUB.setText(_translate("Form", "SUB"))
        self.ADD.setText(_translate("Form", "ADD"))
        self.label_3.setText(_translate("Form", "LICZBA"))
        self.start.setText(_translate("Form", "Start"))
        self.czytaj.setText(_translate("Form", "CZYTAJ"))
        self.krokowa.setText(_translate("Form", "Praca Krokowa"))
        self.calosciowa.setText(_translate("Form", "Praca Całościowa"))
        self.save.setText(_translate("Form", "ZAPISZ PROGRAM"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

