import sys
from PyQt5 import QtCore, QtGui,QtWidgets
from askgui import Ui_Form





class Procesor():

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




    tekst =""
    i = 0
    iPracaKrok = 0

    rejestA = Rejestr("A")
    rejestB = Rejestr("B")
    rejestC = Rejestr("C")
    rejestD = Rejestr("D")

    tabRejestow = []
    tabRejestow.append(rejestA)
    tabRejestow.append(rejestB)
    tabRejestow.append(rejestC)
    tabRejestow.append(rejestD)

    czyPracaKrok = 3


    def __init__(self, parent=None):

        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.DODAJ, QtCore.SIGNAL("clicked()"), self.rozwiazuj)
        QtCore.QObject.connect(self.ui.ZapiszZm, QtCore.SIGNAL("clicked()"), self.zapisz)
        QtCore.QObject.connect(self.ui.Wpisz, QtCore.SIGNAL("clicked()"), self.wpisz)
        QtCore.QObject.connect(self.ui.Graj, QtCore.SIGNAL("clicked()"), self.interpretuj)
        QtCore.QObject.connect(self.ui.PracaKrok, QtCore.SIGNAL("clicked()"), self.interpretujPracaKrok)

        self.show()

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


if __name__ == "__main__":


    app = QtWidgets.QApplication(sys.argv)
    myapp = Procesor()
    myapp.show()
    sys.exit(app.exec_())
