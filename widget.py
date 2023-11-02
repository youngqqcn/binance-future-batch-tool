# This Python file uses the following encoding: utf-8
import sys
from typing import List
import PySide6


from PySide6.QtWidgets import QApplication, QWidget, QAbstractItemView,QMessageBox
from PySide6.QtGui import QIntValidator,QDoubleValidator,QStandardItemModel, QRegularExpressionValidator
from PySide6.QtGui import  QStandardItem
from PySide6.QtCore import QItemSelectionModel
from PySide6.QtCore import Qt
from PySide6.QtSql import QSqlDatabase, QSqlQuery


# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)


        self.setWindowTitle("合约一键下单工具v1.0")
        #self.resize(800, 600)

        # 初始化数据库
        self.__initDatabase__()

        # add token 输入框正则验证器
        addTokenVal = QRegularExpressionValidator("[A-Za-z]{2,7}", self.ui.leToken)
        self.ui.leToken.setValidator(addTokenVal)


        # multiple validator
        multipleVal = QIntValidator()
        multipleVal.setRange(1, 100)
        self.ui.leMultiples.setValidator(multipleVal)


        # stop loss validator
        stopLossVal = QDoubleValidator()
        stopLossVal.setRange(0, 99.0)
        stopLossVal.setTop(99.0)
        stopLossVal.setDecimals(1)
        self.ui.leStopLossRatio.setValidator(stopLossVal)

        # amount validator
        amountVal =  QDoubleValidator()
        amountVal.setRange(0.0001, 99999999999.9)
        amountVal.setDecimals(4)
        self.ui.leAmount.setValidator(amountVal)


        self.ui.leToken.textChanged.connect(self.autoCapitalize)


        # 开多
        self.ui.btnMakeLong.clicked.connect(self.makeLong)

        # 开空
        self.ui.btnMakeShort.clicked.connect(self.makeShort)

        # 添加币种
        self.ui.btnAddToken.clicked.connect(self.addToken)


        # 删除币种
        self.ui.btnDeleteToken.clicked.connect(self.deleteToken)

        # 市价全平（选中）
        self.ui.btnClosePosition.clicked.connect( self.closePosition)






        self.initTargetView()

        pass

    def closeEvent(self,event):
        """重载窗口关闭事件， 关闭数据库"""

        reply = QMessageBox.question(self, '警告',"系统将退出，是否确认?", QMessageBox.Yes |QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

        print('=====close db===========')
        self.db.close()

        super().closeEvent(event)

    def autoCapitalize(self, txts):
        self.ui.leToken.setText(txts.upper())   #这是设置所有字母大写



    def initTargetView(self):
        print('initTargetView')

        self.targetItemModel = QStandardItemModel()
        self.ui.tableView.setModel(self.targetItemModel)

        #按照Items选择，可选择多个
        self.ui.tableView.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.ui.tableView.setSelectionMode(QAbstractItemView.MultiSelection)

        #初始化QStandardItemModel
        self.LoadTarget()

        #需要初始化设置QItemSelectionModel
        self.targetSelectModel = QItemSelectionModel(self.targetItemModel)
        self.ui.tableView.setSelectionModel(self.targetSelectModel)


        self.targetSelectModel.selectionChanged.connect(self.OnSelectionChanged)
        self.targetItemModel.itemChanged.connect(self.OnCheckBoxItemChanged)


    def OnSelectionChanged(self,selectlist, deselectlist):
        print('OnSelectionChanged')
        #选择项改变后，遍历选择的行，将第一列设置为Qt.Checked状态，遍历未选择的行，将未选择的行设置为Qt.Unchecked状态。
        for item in selectlist.indexes():
            rowNum = item.row()
            colNum = item.column()
            # 0:Qt.Unchecked, 1:Qt.PartiallyChecked, 2:Qt.Checked
            self.targetItemModel.item(rowNum, colNum).setCheckState(Qt.CheckState.Checked)

        for item in deselectlist.indexes():
            rowNum = item.row()
            colNum = item.column()
            self.targetItemModel.item(rowNum, colNum).setCheckState(Qt.CheckState.Unchecked)

    def OnCheckBoxItemChanged(self, item):
        print('OnCheckBoxItemChanged')
        #对于itemChanged的单元格，获取行的行号和索引，如果该行的checkState为Checked则选择整行，如果checkState为Unchecked，则整行变为不选择。
        rowNum = item.row()
        colNum = item.column()

        ModelIndex = self.targetItemModel.indexFromItem(item)

        if self.targetItemModel.item(rowNum,colNum).checkState() == Qt.CheckState.Checked:
            self.targetSelectModel.select(ModelIndex, QItemSelectionModel.Select)

        elif self.targetItemModel.item(rowNum,colNum).checkState() == Qt.CheckState.Unchecked:
            self.targetSelectModel.select(ModelIndex, QItemSelectionModel.Deselect)



    def LoadTarget(self):
        print('LoadTarget')
        #从数据库获取Target信息，类似表格表格数据
        # self.targetlist = [
        #     ['AAA1', 'AAA2', 'AAA3', 'AAA4', 'AAA5', 'AAA6', 'AAA7', 'AAA8', 'AAA9', 'AAA10'],
        #     ['BBB1', 'BBB2', 'BBB3', 'BBB4', 'BBB5', 'BBB6', 'BBB7', 'BBB8', 'BBB9', 'BBB10'],
        #     ['CCC1', 'CCC2', 'CCC3', 'CCC4', 'CCC5', 'CCC6', 'CCC7', 'CCC8', 'CCC9', 'CCC10'],
        #     ['DDD1', 'DDD2', 'DDD3', 'DDD4', 'DDD5', 'DDD6', 'DDD7', 'DDD8', 'DDD9', 'DDD10'],
        #     ['EEE1', 'EEE2', 'EEE3', 'EEE4', 'EEE5', 'EEE6', 'EEE7', 'EEE8', 'EEE9', 'EEE10'],
        #     ['FFF1', 'FFF2', 'FFF3', 'FFF4', 'FFF5', 'FFF6', 'FFF7', 'FFF8', 'FFF9', 'FFF10'],
        #     ['GGG1', 'GGG2', 'GGG3', 'GGG4', 'GGG5', 'GGG6', 'GGG7', 'GGG8', 'GGG9', 'GGG10'],
        #     ['HHH1', 'HHH2', 'HHH3', 'HHH4', 'HHH5', 'HHH6', 'HHH7', 'HHH8', 'HHH9', 'HHH10'],
        #     ['III1', 'III2', 'III3', 'III4', 'III5', 'III6', 'III7', 'III8', 'III9', 'III10'],
        #     ['JJJ1', 'JJJ2', 'JJJ3', 'JJJ4', 'JJJ5', 'JJJ6', 'JJJ7', 'JJJ8', 'JJJ9', 'JJJ10'],
        # ]
        self.targetlist = self.loadTokenFromDatabase()
        print(self.targetlist)

        #每次导入时将Model中的数据清除，重新初始化
        self.targetItemModel.clear()
        #第一列没有名称，为CheckBox
        self.targetItemModel.setHorizontalHeaderLabels(('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'))
        # self.ui.tableView.verticalHeader().hide()  #列表头不显示
        self.ui.tableView.horizontalHeader().setHighlightSections(False)
        # self.ui.tableView.setColumnWidth(0,10)    #设置各列宽度
        # self.ui.tableView.setColumnWidth(1,30)
        # self.ui.tableView.setColumnWidth(2,115)
        # self.ui.tableView.setColumnWidth(3,85)
        # self.ui.tableView.setColumnWidth(4,40)

        for row in range(len(self.targetlist)):
            for col in range(len(self.targetlist[0])):
                cell = QStandardItem(str(self.targetlist[row][col]))
                cell.setCheckable(True)
                cell.setEditable(False)
                self.targetItemModel.setItem(row, col, cell)

        self.ui.tableView.show()


    def __initDatabase__(self):
        self.db  = QSqlDatabase.addDatabase('QSQLITE')#指定数据库类型
        #指定SQLite数据库文件名
        self.db.setDatabaseName('future.db')
        self.db.setUserName("futurebitcoin2023")
        self.db.setPassword("makemoremoney2023")
        if not self.db.open():
            print('无法建立与数据库的连接')
            return False

        if len(self.db.tables()) == 0:
            query = QSqlQuery(self.db)
            # self.sqlQuery = query

            # 创建tokenlist表
            ret = query.exec("""CREATE TABLE tb_tokenlist (
                token VARCHAR(10) PRIMARY KEY
            )""")
            if False == ret:
                print("创建表失败")

            query.exec("""INSERT INTO tb_tokenlist(token) VALUES('AAAA')""")
            query.exec("""INSERT INTO tb_tokenlist(token) VALUES('BBBB')""")
            query.exec("""INSERT INTO tb_tokenlist(token) VALUES('CCCC')""")
            query.exec("""INSERT INTO tb_tokenlist(token) VALUES('DDDD')""")
            query.exec("""INSERT INTO tb_tokenlist(token) VALUES('EEEE')""")
            query.exec("""INSERT INTO tb_tokenlist(token) VALUES('FFFF')""")
            query.exec("""INSERT INTO tb_tokenlist(token) VALUES('GGGG')""")
        else:
            print("数据库已经存在")

    def loadTokenFromDatabase(self):
        """从数据库中加载tokenlist"""

        query = QSqlQuery(self.db)
        if not query.exec("""SELECT * from tb_tokenlist WHERE 1=1"""):
            print("查询tb_tokenlist失败")

        tokens = []
        while query.next():
            t = query.value("token")
            print(t)
            tokens.append(t)

        print(tokens)

        # 一维数组转 Nx10 二维数组
        tables = []
        row = []
        for i in range(len(tokens)):
            row.append(tokens[i ])
            if i != 0 and (i % 10) == 0:
                tables.append(row)
                row = []
        tables.append(row)
        return tables


    def addToken(self):
        """添加币种"""
        token = self.ui.leToken.text()
        print(f'add token {token}')

        query = QSqlQuery(self.db)
        query.exec("""SELECT * from tb_tokenlist WHERE `token`='{0}'""".format(token))
        if query.next():
            QMessageBox.warning(self, '提示',f"{token}已经存在", QMessageBox.Yes)
            return

        if not query.exec("""INSERT INTO tb_tokenlist(token) VALUES('{0}')""".format(token)):
            QMessageBox.warning(self, '错误',f"{token}添加失败", QMessageBox.Yes)
        pass

    def deleteToken(self):
        """删除币种"""
        print('delete token')
        pass

    def makeLong(self ):
        """
        市价开多
        """

        print("makeLong")

    def makeShort(self):
        """
        市价开空
        """
        print("makeShort")




    def closePosition(self):
        """市价平仓"""
        print("close position all selected p")
        pass



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
