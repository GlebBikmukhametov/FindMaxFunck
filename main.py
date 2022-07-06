from math import pi, e, sin, cos, tan, sinh, cosh, tanh, asin, acos, atan, asinh, acosh, atanh, log, log2, log10
import random
import sys  # sys нужен для передачи argv в QApplication
###from PyQt5 import *
from PyQt5 import QtWidgets,Qt
from PyQt5.QtGui import QFont, QFontDatabase
import forma  # Это наш конвертированный файл дизайна forma.py (было 100 до этого)

class ExampleApp(QtWidgets.QMainWindow, forma.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  #
        self.ButtonClear.clicked.connect(self.ClearAll)    # Выполнить функцию ClearAll()
        self.formyla = self.TextEditFormula.toPlainText()
        self.lg = self.TextEdit_LG.toPlainText()
        self.pg = self.TextEdit_PG.toPlainText()
        self.kolper = self.TextEdit_KolPer.toPlainText()
        self.ButtonCalculate.clicked.connect(self.MaxFunc)
        self.label_3.move(70,150)
        self.label_4.move(70, 230)
        font = QFont("Roboto", pointSize=12, weight=QFont.Medium, italic=True)
        self.label.setText("")
        self.label.setFont(font)
        self.label_2.setFont(font)
        self.label_3.setFont(font)
        self.label_4.setFont(font)
        self.label_5.setFont(font)
        self.label_2.setText("")
        self.label_3.setText("")
        self.label_4.setText("")
        self.label_5.setText("")

    def ClearAll(self):                                     # Очистим контролы

        self.TextEditFormula.clear()
        self.TextEdit_LG.clear()
        self.TextEdit_PG.clear()
        self.TextEdit_KolPer.clear()
        self.label.clear()
        self.label_2.clear()
        self.label_3.clear()
        self.label_4.clear()
        self.label_5.clear()

    def MaxFunc(self):
        VsePopulat = []  # 3d
        Populat = []  # 2d
        individ = []  # 1d
        formyla = self.TextEditFormula.toPlainText()
        if (formyla == ""):
            self.label_5.setText("введи формулу!!!")
            self.label_5.adjustSize()
            self.label_5.show()
            return [0]

        if (self.TextEdit_LG.toPlainText()=="" or self.TextEdit_PG.toPlainText() ==""):
            self.label_5.setText("введи отрезок!!!")
            self.label_5.adjustSize()
            self.label_5.show()
            return [0]

        lg = int(self.TextEdit_LG.toPlainText())
        pg = int(self.TextEdit_PG.toPlainText())
        if (self.TextEdit_KolPer.toPlainText()==""):
            self.label_5.setText("введи количество переменных!!!")
            self.label_5.adjustSize()
            self.label_5.show()
            return [0]
        kolvoperemen = int(self.TextEdit_KolPer.toPlainText())
        nyli=[]
        for i in range (kolvoperemen):
            nyli.append(0)
        prov = self.Proverkafunction(formyla, nyli)
        if (prov==1):
            self.label_4.setText("формула некорректна")
            self.label_4.adjustSize()
            self.label_4.show()
            return [0]
        for j in range(50):
            for k in range(100):
                for i in range(kolvoperemen):
                    individ.append(random.uniform(lg, pg))
                Populat.append(individ)
                individ = []
            VsePopulat.append(Populat)
            Populat = []
        for iter in range(30):
            newVsePopulat = []
            for j in range(50):
                Populat = VsePopulat[j]
                Ostalos = self.otbor2(Populat)
                deti = []
                while (1 == 1):
                    p1 = random.uniform(0, len(Ostalos) + 1)
                    p1 = int(p1)
                    if (p1 >= len(Ostalos)):
                        p1 = len(Ostalos) - 1

                    p2 = random.uniform(0, len(Ostalos) + 1)
                    p2 = int(p2)
                    if (p2 >= len(Ostalos)):
                        p2 = len(Ostalos) - 1
                    rod1 = Ostalos[p1]
                    rod2 = Ostalos[p2]
                    reb = self.Screch(rod1, rod2)
                    if (len(deti) >= 100):
                        break
                    deti.append(reb)
                newVsePopulat.append(deti)
            VsePopulat = newVsePopulat

        SuperPopulat = []
        for j in range(50):
            Populat = VsePopulat[j]
            Prisp = self.function(formyla, Populat[0])
            individ = Populat[0]
            for i in range(len(Populat)):
                if (self.function(formyla, Populat[i]) > Prisp):
                    Prisp = self.function(formyla, Populat[i])
                    individ = Populat[i]
            SuperPopulat.append(individ)
        VsePopulat = []
        for j in range(10):
            Populat = []
            for i in range(100):
                p1 = random.randint(0, 49)
                p2 = random.randint(0, 49)
                reb = self.Screch(SuperPopulat[p1], SuperPopulat[p2])
                Populat.append(reb)
            VsePopulat.append(Populat)
        for iter in range(30):
            newVsePopulat = []
            for j in range(10):
                Populat = VsePopulat[j]
                Ostalos = self.otbor2(Populat)
                deti = []
                while (1 == 1):
                    p1 = random.uniform(0, len(Ostalos) + 1)
                    p1 = int(p1)
                    if (p1 >= len(Ostalos)):
                        p1 = len(Ostalos) - 1
                    p2 = random.uniform(0, len(Ostalos) + 1)
                    p2 = int(p2)
                    if (p2 >= len(Ostalos)):
                        p2 = len(Ostalos) - 1
                    rod1 = Ostalos[p1]
                    rod2 = Ostalos[p2]
                    reb = self.Screch(rod1, rod2)
                    if (len(deti) >= 100):
                        break
                    deti.append(reb)
                newVsePopulat.append(deti)
            VsePopulat = newVsePopulat
        SuperPopulat = []
        for j in range(10):
            Populat = VsePopulat[j]
            Prisp = self.function(formyla, Populat[0])
            individ = Populat[0]
            for i in range(len(Populat)):
                if (self.function(formyla, Populat[i]) > Prisp):
                    Prisp = self.function(formyla, Populat[i])
                    individ = Populat[i]
            SuperPopulat.append(individ)
        individ = SuperPopulat[0]
        for i in range(len(SuperPopulat)):
            if (self.function(formyla, SuperPopulat[i]) > self.function(formyla, individ)):
                individ = SuperPopulat[i]

        individ2=[]
        individideal=[]
        for i in range(len(individ)):
            individideal.append(pg)
        for z in range (100000):
            individ2=[]
            for i in range (len(individ)):
                k=random.randint(0,100)
                if (k%2==0):
                    individ2.append(lg)
                else:
                    individ2.append(pg)
            if (self.function(formyla, individ2)>self.function(formyla, individideal)):
                individideal=individ2
        if (self.function(formyla, individideal)>self.function(formyla, individ)):
            individ=individideal

        self.label.setText("Максимум =")
        self.label.adjustSize()
        self.label.show()

        self.label_2.setText(str(self.function(formyla, individ)))
        self.label_2.adjustSize()
        self.label_2.show()

        self.label_3.setText("переменные, при которых максимум" + str(individ))
        self.label_3.adjustSize()
        self.label_3.show()

        return individ

    def function(self, formyla, peremen):
        if (len(peremen) > 0):
            x1 = peremen[0]
        if (len(peremen) > 1):
            x2 = peremen[1]
        if (len(peremen) > 2):
            x3 = peremen[2]
        if (len(peremen) > 3):
            x4 = peremen[3]
        if (len(peremen) > 4):
            x5 = peremen[4]
        if (len(peremen) > 5):
            x6 = peremen[5]
        if (len(peremen) > 6):
            x7 = peremen[6]
        if (len(peremen) > 7):
            x8 = peremen[7]
        if (len(peremen) > 8):
            x9 = peremen[8]
        if (len(peremen) > 9):
            x10 = peremen[9]
        return eval(self.TextEditFormula.toPlainText())

    def Proverkafunction(self, formyla, peremen):
        if (len(peremen) > 0):
            x1 = peremen[0]
        if (len(peremen) > 1):
            x2 = peremen[1]
        if (len(peremen) > 2):
            x3 = peremen[2]
        if (len(peremen) > 3):
            x4 = peremen[3]
        if (len(peremen) > 4):
            x5 = peremen[4]
        if (len(peremen) > 5):
            x6 = peremen[5]
        if (len(peremen) > 6):
            x7 = peremen[6]
        if (len(peremen) > 7):
            x8 = peremen[7]
        if (len(peremen) > 8):
            x9 = peremen[8]
        if (len(peremen) > 9):
            x10 = peremen[9]

        try:
            k = eval(self.TextEditFormula.toPlainText())
        except:
            return 1
        return 0


    def cmp(self, individ):
        return self.function(self.TextEditFormula.toPlainText(), individ)

    def otbor2(self,Populat):

        Populat.sort(key=self.cmp)
        Ostalos = []
        nachalo = 80
        for i in range(len(Populat)):
            if (i > nachalo):
                Ostalos.append(Populat[i])
            if (i == 5 or i == 23 or i == 38 or i == 50):
                Ostalos.append(Populat[i])
        return Ostalos

    def Screch(self,rod1, rod2):
        reb = []
        lg = int(self.TextEdit_LG.toPlainText())
        pg = int(self.TextEdit_PG.toPlainText())
        for i in range(len(rod1)):
            k = random.uniform(0, 1)
            Ver = random.uniform(0, 100)
            if (Ver <= 1):
                reb.append(random.uniform(lg, pg))
            else:
                reb.append(rod1[i] * k + rod2[i] * (1 - k))
        return reb




def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    #app.exec_()  # и запускаем приложение
    sys.exit(app.exec_())

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()

