from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_Form(object):



    # ********************************************
    # Tworzenie klasy "Rejestr"
    # ********************************************
    class Rejestr():
        def zwrocWartosc(self):
            return self.value
        def __init__(self, imie_rej):
            self.nazwa = imie_rej
            self.value = 0
        def sub(self, value, LH):
            self.value = self.value - value
            if self.value < 0:
                self.value = abs(self.value)
        def mov(self, value, LH):
            if LH == "L":
                self.value = self.value + value
            else:
                self.value = value
        def add(self, value,LH):
            self.value = self.value + value

    # ********************************************
    # Tworzenie Rejestrow A,B,C,D
    # ********************************************
    def createRejestrs(self):
        rejestA = self.Rejestr("A")
        rejestB = self.Rejestr("B")
        rejestC = self.Rejestr("C")
        rejestD = self.Rejestr("D")
        return rejestA,rejestB,rejestC,rejestD


    # ********************************************
    # Tworzenie tabeli rejestrow
    # ********************************************
    def createTabOfRejestr(self,createRejestrs):
        rejestA, rejestB, rejestC, rejestD = createRejestrs()
        tabRejestow = []
        tabRejestow.append(rejestA)
        tabRejestow.append(rejestB)
        tabRejestow.append(rejestC)
        tabRejestow.append(rejestD)
        return rejestA, rejestB, rejestC, rejestD, tabRejestow


    # ********************************************
    # Sprawdzanie czy rejestr jest A,B,C,D oraz czy jest L,H
    # ********************************************
    def sprawdzRejestrABCD(self,rej):
        if(str(rej)=="rAXh"):
            return self.rejestA,"H"
        elif(str(rej)=="rAXl"):
            return self.rejestA,"L"
        elif(str(rej)=="rBXh"):
            return self.rejestB,"H"
        elif(str(rej)=="rBXl"):
            return self.rejestB,"L"
        elif(str(rej)=="rCXh"):
            return self.rejestC,"H"
        elif(str(rej)=="rCXl"):
            return self.rejestC,"L"
        elif(str(rej)=="rDXh"):
            return self.rejestD,"H"
        elif(str(rej)=="rDXl"):
            return self.rejestD,"L"

    # ********************************************
    # Praca krokowa
    # ********************************************

    def uruchomPracaKrokowa(self):

        rozkaz = ""
        rej1 = ""
        rej2 = ""
        licz = 0
        ii = self.krokPK + 1
        krok=self.krok
        kontrola = self.krokConsole2
        self.krokConsole2=self.krokConsole2+1
        # self.tekst.__len__() ilosc znakow w tekscie
        for i in range(ii, self.tekst.__len__()):

            if self.tekst[i].isspace():
                licz = licz+1
            if licz == 1:
                if not(self.tekst[i].isspace() or self.tekst[i].isdigit()):
                    rozkaz = rozkaz + (self.tekst[i])
            if licz == 2:
                if not(self.tekst[i].isspace() or self.tekst[i].isdigit()):
                    rej1 = rej1 + (self.tekst[i])
            if licz == 3:
                if not(self.tekst[i].isspace()):
                    rej2 = rej2 + (self.tekst[i])
            if licz == 4:
                self.krokPK = i
                rejestr,LHrej1 = self.sprawdzRejestrABCD(rej1)
                dodaj = 0
                if rej2.isdigit():
                    dodaj = rej2
                else:
                    dodajR,LHrej2 = self.sprawdzRejestrABCD(rej2)
                    dodaj = dodajR.value

                if rozkaz == "ADD":
                    rejestr.add(int(dodaj),LHrej1)
                if rozkaz == "SUB":
                    rejestr.sub(int(dodaj), LHrej1)
                if rozkaz == "MOV":
                    rejestr.mov(int(dodaj), LHrej1)
                self.tekstConsole2 = self.tekstConsole2+ (str(self.krokConsole2) + " Rejestr " + rejestr.nazwa + "  " + str(rejestr.value) +"\n")
                self.textBrowser_2.setText(self.tekstConsole2)
                break
        if ii == 1 and licz == 0 and abs(self.krokConsole2-kontrola)==0:
            self.krokConsole2 = 0


    # ********************************************
    # Praca calkowita
    # ********************************************
    def uruchomPracaCalkowita(self):


        sting = self.tekst
        rozkaz = ""
        rej1 = ""
        rej2 = ""
        licz = 0

        for i in range(sting.__len__()):
            if sting[i].isspace():
                licz = licz+1

            if licz == 1:
                if not(sting[i].isspace() or sting[i].isdigit()):
                    rozkaz = rozkaz + (sting[i])
            if licz == 2:
                if not(sting[i].isspace() or sting[i].isdigit()):
                    rej1 = rej1 + (sting[i])
            if licz == 3:
                if not(sting[i].isspace()):
                    rej2 = rej2 + (sting[i])
            if licz == 4:
                rejestr, LHrej1 = self.sprawdzRejestrABCD(rej1)
                dodaj = 0
                if rej2.isdigit():
                    dodaj = rej2
                else:
                    dodajR, LHrej2 = self.sprawdzRejestrABCD(rej2)
                    dodaj = dodajR.value
                if rozkaz == "ADD":
                    rejestr.add(int(dodaj), LHrej1)
                if rozkaz == "SUB":
                    rejestr.sub(int(dodaj), LHrej1)
                if rozkaz == "MOV":
                    rejestr.mov((dodaj), LHrej1)

                rozkaz= ""
                rej1 = ""
                rej2 = ""
                licz = 0

        tekst = ""
        for i in range(4):
            tekst = tekst + "Rejestr " + self.tabRejestow[i].nazwa + "  " + str(self.tabRejestow[i].value) +"\n"

        self.textBrowser_2.setText(tekst)
        self.rejestA.value = 0
        self.rejestB.value = 0
        self.rejestC.value = 0
        self.rejestD.value = 0






    # ********************************************
    # CZYTANIE Z PLIKU
    # ********************************************

    def czytaj(self):
        self.tekst = open('save.txt').read()
        self.textBrowser.setText(self.tekst)
        self.krok = int(open('ilosc_krokow.txt').read())
        self.tekstConsole2 = ""
        self.textBrowser_2.setText(self.tekstConsole2)
        self.krokConsole2 = 0
        self.krokPK = 0
        self.rejestA.value = 0
        self.rejestB.value = 0
        self.rejestC.value = 0
        self.rejestD.value = 0



    # ********************************************
    # ZAPIS DO PLIKU
    # ********************************************


    def zapisz(self):
        plik = open('save.txt', 'w')
        plik.write(self.tekst)
        plik.close()
        plik = open('ilosc_krokow.txt', 'w')
        plik.write(str(self.krok))
        plik.close()




    # ********************************************
    # ADD/SUB/MOV
    # ********************************************
    def Add_Sub_Mov(self,tekst):
        if self.ADD.isChecked():
            tekst = tekst + "ADD "
            komenda = True
        elif self.SUB.isChecked():
            tekst = tekst + "SUB "
            komenda = True
        elif self.MOV.isChecked():
            tekst = tekst + "MOV "
            komenda = True
        else:
            self.textBrowser_2.setText("ERROR: Trzeba wybrac ADD lub SUB lub MOV")
            komenda = False
        return komenda,tekst

    # ********************************************
    # Rejestr1
    # ********************************************
    def rej1(self,tekst):
        if self.AXH.isChecked():
            tekst = tekst + "rAXh "
            rejestr1 = True
        elif self.AXL.isChecked():
            tekst = tekst + "rAXl "
            rejestr1 = True
        elif self.BXH.isChecked():
            tekst = tekst + "rBXh "
            rejestr1 = True
        elif self.BXL.isChecked():
            tekst = tekst + "rBXl "
            rejestr1 = True
        elif self.CXH.isChecked():
            tekst = tekst + "rCXh "
            rejestr1 = True
        elif self.CXL.isChecked():
            tekst = tekst + "rCXl "
            rejestr1 = True
        elif self.DXH.isChecked():
            tekst = tekst + "rDXh "
            rejestr1 = True
        elif self.DXL.isChecked():
            tekst = tekst + "rDXl "
            rejestr1 = True
        else:
            self.textBrowser_2.setText("ERROR: Nie wybrano nic w rejestrze 1")
            rejestr1 = False
        return rejestr1, tekst
    # ********************************************
    # Rejestr2
    # ********************************************

    def rej2(self,tekst):
        if self.AXH_2.isChecked():
            tekst = tekst + "rAXh"
            rejestr2 = True
            self.rejestr2HL = 'H'
        elif self.AXL_2.isChecked():
            tekst = tekst + "rAXl"
            rejestr2 = True
        elif self.BXH_2.isChecked():
            tekst = tekst + "rBXh"
            rejestr2 = True
        elif self.BXL_2.isChecked():
            tekst = tekst + "rBXl"
            rejestr2 = True
        elif self.CXH_2.isChecked():
            tekst = tekst + "rCXh"
            rejestr2 = True
        elif self.CXL_2.isChecked():
            tekst = tekst + "rCXl"
            rejestr2 = True
        elif self.DXH_2.isChecked():
            tekst = tekst + "rDXh"
            rejestr2 = True
        elif self.DXL_2.isChecked():
            tekst = tekst + "rDXl"
            rejestr2 = True
        elif self.liczba.isChecked():
            tekst = tekst + str(self.textEdit.toPlainText())
            rejestr2 = True
        else:
            self.textBrowser_2.setText("ERROR: Nie wybrano nic w rejestrze 2")
            rejestr2 = False
        return rejestr2, tekst
    # ********************************************
    # Tworzenie lini komendy
    # ********************************************
    def komenda(self):
        tekst = ""
        # ADD SUB MOV
        komenda,tekst = self.Add_Sub_Mov(tekst)
        # Rejestr 1
        rejestr1, tekst = self.rej1(tekst)
        # Rejestr 2
        rejestr2, tekst = self.rej2(tekst)
        # Obsluga bledu
        if self.MOV.isChecked() and self.liczba.isChecked():
            self.textBrowser_2.setText("ERROR: Nie można użyć MOV wraz z liczba!")
        else:
            if(komenda and rejestr1 and rejestr2):
                # self.textBrowser_2.setText("")
                tekst = str(self.krok)+ " " + tekst
                self.krok = self.krok + 1
                self.tekst = self.tekst + tekst +"\n"
                self.textBrowser.setText(self.tekst)



    def setupUi(self, Form):

        # *********************************************
        # Inicjalizacja zmiennych
        # **********************************************
        self.tekstConsole2 = "" #tekst w kosoli 2
        self.krok=1
        self.krokConsole2=0
        self.krokPK = 0
        self.tekst= ''
        self.rejestA, self.rejestB, self.rejestC, self.rejestD,self.tabRejestow = self.createTabOfRejestr(self.createRejestrs)

        # *********************************************
        # GUI - grafika
        # **********************************************


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
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(10, 100, 451, 80))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(Form)
        self.frame_3.setGeometry(QtCore.QRect(10, 190, 451, 80))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_4 = QtWidgets.QFrame(Form)
        self.frame_4.setGeometry(QtCore.QRect(470, 10, 221, 121))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.frame_5 = QtWidgets.QFrame(Form)
        self.frame_5.setGeometry(QtCore.QRect(10, 280, 681, 191))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.frame_6 = QtWidgets.QFrame(Form)
        self.frame_6.setGeometry(QtCore.QRect(10, 550, 681, 181))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.frame_7 = QtWidgets.QFrame(Form)
        self.frame_7.setGeometry(QtCore.QRect(470, 140, 221, 131))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        # Rejestr 1
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
        # Rejestr 2
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
        self.liczba = QtWidgets.QRadioButton(self.frame_2)
        self.liczba.setGeometry(QtCore.QRect(150, 20, 41, 17))
        self.liczba.setObjectName("liczba")
        # zadanie
        self.MOV = QtWidgets.QRadioButton(self.frame_3)
        self.MOV.setGeometry(QtCore.QRect(30, 20, 82, 41))
        self.MOV.setObjectName("MOV")
        self.SUB = QtWidgets.QRadioButton(self.frame_3)
        self.SUB.setGeometry(QtCore.QRect(180, 20, 82, 41))
        self.SUB.setObjectName("SUB")
        self.ADD = QtWidgets.QRadioButton(self.frame_3)
        self.ADD.setGeometry(QtCore.QRect(330, 20, 82, 41))
        self.ADD.setObjectName("ADD")
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 71, 31))
        self.label_3.setObjectName("label_3")
        # liczba
        self.textEdit = QtWidgets.QTextEdit(self.frame_4)
        self.textEdit.setGeometry(QtCore.QRect(20, 70, 171, 31))
        self.textEdit.setObjectName("textEdit")
        # wyswietlanie - 1 konsola
        self.textBrowser = QtWidgets.QTextBrowser(self.frame_5)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 451, 171))
        self.textBrowser.setObjectName("textBrowser")
        # wyswietlanie - 2 konsola
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.frame_6)
        self.textBrowser_2.setGeometry(QtCore.QRect(10, 10, 451, 161))
        self.textBrowser_2.setObjectName("textBrowser_2")
        # start
        self.start = QtWidgets.QPushButton(self.frame_5)
        self.start.setGeometry(QtCore.QRect(490, 10, 171, 171))
        self.start.setObjectName("start")
        # czytaj z pliku
        self.open = QtWidgets.QPushButton(self.frame_6)
        self.open.setGeometry(QtCore.QRect(490, 10, 171, 161))
        self.open.setObjectName("czytaj")
        # Praca:
        ## krokowa
        self.krokowa = QtWidgets.QPushButton(self.frame_7)
        self.krokowa.setGeometry(QtCore.QRect(20, 20, 181, 41))
        self.krokowa.setObjectName("krokowa")
        ## calosciowa
        self.calosciowa = QtWidgets.QPushButton(self.frame_7)
        self.calosciowa.setGeometry(QtCore.QRect(20, 70, 181, 41))
        self.calosciowa.setObjectName("calosciowa")
        # zapisz do pliku
        self.save = QtWidgets.QPushButton(Form)
        self.save.setGeometry(QtCore.QRect(10, 480, 681, 61))
        self.save.setObjectName("save")

        # *********************************************
        # Events handlers
        # **********************************************


        self.krokowa.clicked.connect(self.uruchomPracaKrokowa)
        self.calosciowa.clicked.connect(self.uruchomPracaCalkowita)
        self.start.clicked.connect(self.komenda)
        self.save.clicked.connect(self.zapisz)
        self.open.clicked.connect(self.czytaj)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    # *********************************************
    # NAZWY W BUTTONACH/LABELACH
    # **********************************************
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.DXH.setText(_translate("Form", "DXH"))
        self.liczba.setText(_translate("Form", "Liczba"))
        self.CXL.setText(_translate("Form", "CXL"))
        self.DXL.setText(_translate("Form", "DXL"))
        self.label.setText(_translate("Form", "Rejestry 1"))
        self.AXH.setText(_translate("Form", "AXH"))
        self.AXL.setText(_translate("Form", "AXL"))
        self.CXH.setText(_translate("Form", "CXH"))
        self.BXL.setText(_translate("Form", "BXL"))
        self.BXH.setText(_translate("Form", "BXH"))
        self.DXH_2.setText(_translate("Form", "DXH"))
        self.CXL_2.setText(_translate("Form", "CXL"))
        self.DXL_2.setText(_translate("Form", "DXL"))
        self.label_2.setText(_translate("Form", "Rejestry 2"))
        self.AXH_2.setText(_translate("Form", "AXH"))
        self.AXL_2.setText(_translate("Form", "AXL"))
        self.CXH_2.setText(_translate("Form", "CXH"))
        self.BXL_2.setText(_translate("Form", "BXL"))
        self.BXH_2.setText(_translate("Form", "BXH"))
        self.MOV.setText(_translate("Form", "MOV"))
        self.SUB.setText(_translate("Form", "SUB"))
        self.ADD.setText(_translate("Form", "ADD"))
        self.label_3.setText(_translate("Form", "LICZBA"))
        self.start.setText(_translate("Form", "Dodaj"))
        self.open.setText(_translate("Form", "CZYTAJ"))
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

