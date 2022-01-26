import sqlite3
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

current_page=1
menu_cur_condition=1
rezh_razr=False

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('1.ui', self)
        self.con = sqlite3.connect("Приложение.db")

        self.setWindowIcon(QIcon('1.jpg'))

        self.menu1.setIcon(QIcon('menu.jpg'))
        self.prilozh.setIcon(QIcon('2.jpg'))
        self.table.setIcon(QIcon('table.png'))
        self.info.setIcon(QIcon('info.jpg'))
        self.settings.setIcon(QIcon('settings.png'))

        self.hours.setVisible(False)
        self.text.setVisible(False)
        self.choose.setVisible(False)
        self.prev.setVisible(False)

        self.plata.setVisible(False)
        self.text2.setVisible(False)
        self.calculate.setVisible(False)

        self.text4.setVisible(False)
        self.text5.setVisible(False)
        self.text6.setVisible(False)
        self.text7.setVisible(False)
        self.text8.setVisible(False)

        self.text_type.setVisible(False)
        self.text_firm.setVisible(False)
        self.text_model.setVisible(False)
        self.text_mosh.setVisible(False)

        self.text_photo.setVisible(False)

        self.razrab.setVisible(False)
        self.text3.setVisible(False)
        self.razrab.stateChanged.connect(self.onAct_rezh_razr)

        self.tableData.setVisible(False)
        self.lineFind.setVisible(False)
        self.comboFind.setVisible(False)
        self.showFind.setVisible(False)
        self.AFrameTable.setVisible(False)

        self.deleteData.setVisible(False)
        self.addData.setVisible(False)
        
        self.menu.clicked.connect(self.onAct_menu)
        self.menu1.clicked.connect(self.onAct_menu)
        self.prilozh1.clicked.connect(self.onAct_pril)
        self.prilozh.clicked.connect(self.onAct_pril)
        self.table1.clicked.connect(self.onAct_table)
        self.table.clicked.connect(self.onAct_table)
        self.settings1.clicked.connect(self.onAct_settings)
        self.settings.clicked.connect(self.onAct_settings)
        self.info.clicked.connect(self.onAct_info)
        self.info1.clicked.connect(self.onAct_info)

        self.type.activated[str].connect(self.choosen_type)
        self.firm.activated[str].connect(self.choosen_firm)
        self.next.clicked.connect(self.onAct_next)

        self.choose.activated[str].connect(self.choosen_time)
        self.prev.clicked.connect(self.onAct_prev)

        self.calculate.clicked.connect(self.onAct_calculate)
        
        self.showFind.clicked.connect(self.onAct_find)

        self.addData.clicked.connect(self.onAct_add_elem)
        self.deleteData.clicked.connect(self.onAct_del_elem)
        self.tableData.itemChanged.connect(self.item_changed)
        self.modified = {}
        self.titles = None

        
        
        
    def onAct_rezh_razr(self): #Переключение между режимом разработчика и пользователя
        global rezh_razr
        if not rezh_razr:
            rezh_razr=True
        else:
            rezh_razr=False

    def onAct_menu(self): #Сужение/расширение бокового меню
        global menu_cur_condition
        if menu_cur_condition==0:
            self.menu.resize(221,491)
            self.menu.move(0,40)

            self.prilozh1.setVisible(True)
            self.table1.setVisible(True)
            self.settings1.setVisible(True)
            self.info1.setVisible(True)

            menu_cur_condition=1
        elif menu_cur_condition==1:
            self.menu.resize(41,491)
            self.menu.move(0,40)

            self.prilozh1.setVisible(False)
            self.table1.setVisible(False)
            self.settings1.setVisible(False)
            self.info1.setVisible(False)

            menu_cur_condition=0  
            
    def onAct_pril(self): #Переключение на основную вкладку приложния
        global current_page
        self.razrab.setVisible(False)
        self.text3.setVisible(False)

        self.tableData.setVisible(False)
        self.lineFind.setVisible(False)
        self.comboFind.setVisible(False)
        self.showFind.setVisible(False)
        self.deleteData.setVisible(False)
        self.addData.setVisible(False)
        self.AFrameTable.setVisible(False)

        self.text4.setVisible(False)
        self.text5.setVisible(False)
        self.text6.setVisible(False)
        self.text7.setVisible(False)
        self.text8.setVisible(False)

        self.text_type.setVisible(False)
        self.text_firm.setVisible(False)
        self.text_model.setVisible(False)
        self.text_mosh.setVisible(False)

        self.text_photo.setVisible(False)

        if current_page==2:
            self.hours.setVisible(True)
            self.text.setVisible(True)
            self.choose.setVisible(True)
            self.prev.setVisible(True)
            self.next.setVisible(True)
            self.prev.setVisible(True)
        elif current_page==3:
            self.plata.setVisible(True)
            self.text2.setVisible(True)
            self.calculate.setVisible(True)
            self.prev.setVisible(True)
        elif current_page==1:
            self.type.setVisible(True)
            self.firm.setVisible(True)
            self.model.setVisible(True)
            self.next.setVisible(True)
    
    def onAct_table(self): #Переключение на таблицу со всеми приборами
        global сurr_rezh
        self.type.setVisible(False)
        self.firm.setVisible(False)
        self.model.setVisible(False)
        self.next.setVisible(False)

        self.razrab.setVisible(False)
        self.text3.setVisible(False)

        self.text4.setVisible(False)
        self.text5.setVisible(False)
        self.text6.setVisible(False)
        self.text7.setVisible(False)
        self.text8.setVisible(False)

        self.text_type.setVisible(False)
        self.text_firm.setVisible(False)
        self.text_model.setVisible(False)
        self.text_mosh.setVisible(False)

        self.text_photo.setVisible(False)
        
        self.hours.setVisible(False)
        self.text.setVisible(False)
        self.choose.setVisible(False)
        self.prev.setVisible(False)

        self.plata.setVisible(False)
        self.text2.setVisible(False)
        self.calculate.setVisible(False)
        
        self.razrab.setVisible(False)
        self.text3.setVisible(False)

        self.tableData.setVisible(True)
        self.lineFind.setVisible(True)
        self.comboFind.setVisible(True)
        self.showFind.setVisible(True)
        self.AFrameTable.setVisible(True)

        if rezh_razr:
            self.addData.setVisible(True)
            self.deleteData.setVisible(True)

        self.show_data()

    def onAct_settings(self): #Переключение на настройки
        self.type.setVisible(False)
        self.firm.setVisible(False)
        self.model.setVisible(False)
        self.next.setVisible(False)
        
        self.hours.setVisible(False)
        self.text.setVisible(False)
        self.choose.setVisible(False)
        self.prev.setVisible(False)

        self.plata.setVisible(False)
        self.text2.setVisible(False)
        self.calculate.setVisible(False)

        self.razrab.setVisible(False)
        self.text3.setVisible(False)

        self.text4.setVisible(False)
        self.text5.setVisible(False)
        self.text6.setVisible(False)
        self.text7.setVisible(False)
        self.text8.setVisible(False)

        self.text_type.setVisible(False)
        self.text_firm.setVisible(False)
        self.text_model.setVisible(False)
        self.text_mosh.setVisible(False)

        self.text_photo.setVisible(False)

        self.tableData.setVisible(False)
        self.lineFind.setVisible(False)
        self.comboFind.setVisible(False)
        self.showFind.setVisible(False)
        self.AFrameTable.setVisible(False)

        self.deleteData.setVisible(False)
        self.addData.setVisible(False)
        
        self.razrab.setVisible(True)
        self.text3.setVisible(True)

    def onAct_info(self):
        self.type.setVisible(False)
        self.firm.setVisible(False)
        self.model.setVisible(False)
        self.next.setVisible(False)
        
        self.hours.setVisible(False)
        self.text.setVisible(False)
        self.choose.setVisible(False)
        self.prev.setVisible(False)

        self.plata.setVisible(False)
        self.text2.setVisible(False)
        self.calculate.setVisible(False)

        self.razrab.setVisible(False)
        self.text3.setVisible(False)

        self.tableData.setVisible(False)
        self.lineFind.setVisible(False)
        self.comboFind.setVisible(False)
        self.showFind.setVisible(False)
        self.AFrameTable.setVisible(False)

        self.deleteData.setVisible(False)
        self.addData.setVisible(False)

        curr_type=self.type.currentText()
        curr_firm=self.firm.currentText()
        curr_model=self.model.currentText()
        cur = self.con.cursor()
        curr_mosh = cur.execute("Select Энергопотрбление from Приложение WHERE Модель=?", (curr_model,)).fetchall()
        curr_mosh = str(curr_mosh)[:0] + str(curr_mosh)[2:]
        curr_mosh = str(curr_mosh)[:-3] + str(curr_mosh)[-1:]
        curr_mosh=curr_mosh.replace("]","")

        self.text_type.setText(curr_type)
        self.text_firm.setText(curr_firm)
        self.text_model.setText(curr_model)
        self.text_mosh.setText(curr_mosh)

        curr_photo = cur.execute("Select Фото from Приложение WHERE Модель=?", (curr_model,)).fetchall()
        curr_photo = str(curr_photo)[:0] + str(curr_photo)[3:]
        curr_photo = str(curr_photo)[:-4] + str(curr_photo)[-1:]
        curr_photo=curr_photo.replace("]","")

        self.text_photo.setText("")

        pix=QPixmap('Фото\\' + curr_photo + '.jpg')
        pix=pix.scaledToWidth(341)
        pix=pix.scaledToHeight(341)
        self.text_photo.setPixmap(pix)
        
        self.text4.setVisible(True)
        self.text5.setVisible(True)
        self.text6.setVisible(True)
        self.text7.setVisible(True)
        self.text8.setVisible(True)

        self.text_type.setVisible(True)
        self.text_firm.setVisible(True)
        self.text_model.setVisible(True)
        self.text_mosh.setVisible(True)

        self.text_photo.setVisible(True)


    def choosen_type(self,text): #Выбор типа прибора и подгрузка данных в comboBox с выбором фирмы прибора
        cur = self.con.cursor()
        if text=="Кофеварка":
            self.firm.clear()
            self.firm.addItem('Vitek')
            self.firm.addItem('Kitfort')
            result = cur.execute("Select Модель from Приложение WHERE Фирма=?", ("Vitek",)).fetchall()
            self.model.clear()

            for i, elem in enumerate(result):
                elem = str(elem)[:0] + str(elem)[2:]
                elem = str(elem)[:-3] + str(elem)[-1:]
                elem=elem.replace(")","")
                self.model.addItem(elem)

        elif text=="Посудомойка":
            self.firm.clear()
            self.firm.addItem('Bosch')
            self.firm.addItem('Electrolux')
            self.firm.addItem('Siemens')

            result = cur.execute("Select Модель from Приложение WHERE Фирма=?", ("Bosch",)).fetchall()
            self.model.clear()

            for i, elem in enumerate(result):
                elem = str(elem)[:0] + str(elem)[2:]
                elem = str(elem)[:-3] + str(elem)[-1:]
                elem=elem.replace(")","")
                self.model.addItem(elem)

    def choosen_firm(self,text): #Выбор фирмы прибора и подгрузка данных в comboBox с выбором модели прибора
        cur = self.con.cursor()
        result = cur.execute("Select Модель from Приложение WHERE Фирма=?", (text,)).fetchall()
        self.model.clear()

        for i, elem in enumerate(result):
            elem = str(elem)[:0] + str(elem)[2:]
            elem = str(elem)[:-3] + str(elem)[-1:]
            elem=elem.replace(")","")
            self.model.addItem(elem)

    def choosen_time(self,text): #Обработка ComboBox с выбором "В день"/"В неделю"/"В месяц"
        if text=="В день":
            self.hours.setMaximum(24)

        elif text=="В неделю":
            self.hours.setMaximum(168)

        elif text=="В месяц":
            self.hours.setMaximum(720)

    def onAct_next(self): #Обработка кнопки далее на всех страницах
        global current_page
        current_page+=1

        if current_page==2:
            self.type.setVisible(False)
            self.firm.setVisible(False)
            self.model.setVisible(False)
            self.hours.setVisible(True)
            self.text.setVisible(True)
            self.choose.setVisible(True)
            self.prev.setVisible(True)

        if current_page==3:
            self.hours.setVisible(False)
            self.text.setVisible(False)
            self.choose.setVisible(False)
            self.plata.setVisible(True)
            self.text2.setVisible(True)
            self.next.setVisible(False)
            self.calculate.setVisible(True)

    def onAct_prev(self): #Обработка кнопки Назад на всех страницах
        global current_page
        current_page-=1

        if current_page==1:
            self.type.setVisible(True)
            self.firm.setVisible(True)
            self.model.setVisible(True)
            self.hours.setVisible(False)
            self.text.setVisible(False)
            self.choose.setVisible(False)
            self.prev.setVisible(False)

        if current_page==2:
            self.hours.setVisible(True)
            self.text.setVisible(True)
            self.choose.setVisible(True)
            self.plata.setVisible(False)
            self.text2.setVisible(False)
            self.calculate.setVisible(False)
            self.next.setVisible(True)

    def onAct_calculate(self): #Рассчет платы
        plata=0
        h=self.hours.value()
        if self.choose.currentText()=="В неделю":
            h=h*4

        elif self.choose.currentText()=="В день":
            h=h*30

        mod=self.model.currentText()
        cur = self.con.cursor()
        mosh = cur.execute("Select Энергопотрбление from Приложение WHERE Модель=?", (mod,)).fetchall()
        mosh = str(mosh)[:0] + str(mosh)[2:]
        mosh = str(mosh)[:-3] + str(mosh)[-1:]
        mosh=mosh.replace("]","")
        mosh=int(mosh)

        pl=self.plata.value()
        plata=mosh*h*pl/1000

        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        if self.type.currentText()=="Кофеварка":
            msgBox.setText("Вам придется заплатить {} за месяц за Кофеварку {} {}".format(plata,self.firm.currentText(),self.model.currentText()))

        elif self.type.currentText()=="Посудомойка":
            msgBox.setText("Вам придется заплатить {} за месяц за Посудомойку {} {}".format(plata,self.firm.currentText(),self.model.currentText()))

        msgBox.setWindowTitle("Плата подсчитана")
        msgBox.setStandardButtons(QMessageBox.Ok)
        returnValue = msgBox.exec() 


    def show_data(self): #Отображение БД
        cur = self.con.cursor()
        result = cur.execute("Select ID,Тип,Фирма,Модель,Энергопотрбление from Приложение").fetchall()

        self.tableData.setRowCount(len(result))
        self.tableData.setColumnCount(len(result[0]))
        self.titles = [description[0] for description in cur.description]

        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableData.setItem(i, j, QTableWidgetItem(str(val)))

        self.modified = {}

    def update(self): #Обновление БД
        cur = self.con.cursor()
        result = cur.execute("Select ID,Тип,Фирма,Модель,Энергопотрбление from Приложение").fetchall()

        self.tableData.setRowCount(len(result))
        self.tableData.setColumnCount(len(result[0]))
        self.titles = [description[0] for description in cur.description]

        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableData.setItem(i, j, QTableWidgetItem(str(val)))

        self.modified = {}
        self.con.commit()

    def item_changed(self, item):  #Обновление элемента в таблице
        self.modified[self.titles[item.column()]] = item.text()

    def onAct_find(self): #Поиск по БД
        cur = self.con.cursor()

        if self.lineFind.text()=='':
            self.show_data()

        else:
            if self.comboFind.currentText()=='Тип прибора':
                result = cur.execute("Select ID,Тип,Фирма,Модель,Энергопотрбление from Приложение WHERE Тип=?", (self.lineFind.text(),)).fetchall()

            if self.comboFind.currentText()=='Фирма прибора':
                result = cur.execute("Select ID,Тип,Фирма,Модель,Энергопотрбление from Приложение WHERE Фирма=?", (self.lineFind.text(),)).fetchall()

            if self.comboFind.currentText()=='Модель прибора':
                result = cur.execute("Select ID,Тип,Фирма,Модель,Энергопотрбление from Приложение WHERE Модель=?", (self.lineFind.text(),)).fetchall()

            if self.comboFind.currentText()=='Энергопотрбление':
                result = cur.execute("Select ID,Тип,Фирма,Модель,Энергопотрбление from Приложение WHERE Энергопотрбление=?", (self.lineFind.text(),)).fetchall()

            if not result:
                QMessageBox.about(self,'','')

            if result:
                self.tableData.setColumnCount(len(result[0]))
                self.titles = [description[0] for description in cur.description]
                self.tableData.setRowCount(len(result))

                for i, elem in enumerate(result):
                    for j, val in enumerate(elem):
                        self.tableData.setItem(i, j, QTableWidgetItem(str(val)))

                self.tableData.resizeColumnsToContents()

    def onAct_add_elem(self): #Добавление элемента(в режиме разраб.)
        cur = self.con.cursor()
        id=cur.execute("SELECT ID FROM Приложение WHERE ID=(SELECT max(ID) FROM Приложение)").fetchall()

        id = str(id)[:0] + str(id)[2:]
        id = str(id)[:-3] + str(id)[-1:]
        id=id.replace("]","")
        id=int(id)

        idd, o = QInputDialog.getInt(self, 'Номер id','Введите номер id',id+1,id+1,1000,1)

        if o:
            typee, ok= QInputDialog.getText(self, 'Тип прибора','Введите тип прибора')

            if ok:
                firmm, okk= QInputDialog.getText(self, 'Фирма прибора','Введите фирму прибора')

                if okk:
                    modell, okkk= QInputDialog.getText(self, 'Модель прибора','Введите модель прибора')

                    if okkk:
                        energg, okkkk = QInputDialog.getInt(self, 'Мощность','Введите мощность прибора',500,100,2000,10)

                        cur.execute("INSERT INTO Приложение (ID, Тип, Фирма, Модель, Энергопотрбление) VALUES ({},'{}','{}','{}',{})".format(idd, typee, firmm, modell, energg))

                        self.show_data()
                        self.update()

    def onAct_del_elem(self): #Удаление элемента(в режиме разраб.)
        rows = list(set([i.row() for i in self.tableData.selectedItems()]))
        ids = [self.tableData.item(i, 0).text() for i in rows]

        valid = QMessageBox.question(self, '', "Действительно удалить элементы с id " + ",".join(ids), QMessageBox.Yes, QMessageBox.No)

        if valid == QMessageBox.Yes:
            cur = self.con.cursor()
            cur.execute("DELETE from Приложение WHERE ID in (" + ", ".join('?' * len(ids)) + ")", ids)
            self.con.commit()

        self.show_data()

    

app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
