# This Python file uses the following encoding: utf-8
import logging
import sys
from typing import List
from PySide6.QtWidgets import QApplication, QWidget, QAbstractItemView,QMessageBox
from PySide6.QtGui import QIntValidator,QDoubleValidator,QStandardItemModel, QRegularExpressionValidator
from PySide6.QtGui import  QStandardItem, QBrush, QColor, QIcon
from PySide6.QtCore import QItemSelectionModel
from PySide6.QtCore import Qt,QThread, Signal
from PySide6.QtSql import QSqlDatabase, QSqlQuery
from PySide6.QtWidgets import QApplication, QDialog, QProgressBar, QVBoxLayout, QPushButton



# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget


from bnwrapper.bn import BnUmWrapper
from binance.error import ClientError

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)


        self.setWindowTitle("合约一键下单工具v1.0")
        self.setWindowIcon(QIcon('logo.png'))
        #self.resize(800, 600)

        # 初始化数据库
        self.__initDatabase__()

        self.bnUmWrapper = None

        apiKey, secretKey = self.loadApiKey()
        if len(apiKey) == 64 or len(secretKey) == 64:
            self.bnUmWrapper = BnUmWrapper(apiKey=apiKey, secretKey=secretKey)


        # 禁用币本位
        self.ui.rbtnTokenBase.setDisabled(True)
        self.ui.btnMakeLong.setStyleSheet("background-color: #16E744")
        self.ui.btnMakeShort.setStyleSheet("background-color: #ED4333")

        # add token 输入框正则验证器
        # addTokenVal = QRegularExpressionValidator("[A-Za-z0-9]{2,20}", self.ui.leToken)
        # self.ui.leToken.setValidator(addTokenVal)


        # multiple validator
        leverageVal = QIntValidator()
        leverageVal.setRange(1, 99)
        self.ui.leLeverage.setValidator(leverageVal)


        # stop loss validator
        stopLossVal = QIntValidator()
        stopLossVal.setRange(0, 99)
        stopLossVal.setTop(99)
        self.ui.leStopLossRatio.setValidator(stopLossVal)

        # amount validator
        amountVal = QDoubleValidator()
        amountVal.setRange(1, 1000)
        self.ui.leAmount.setValidator(amountVal)


        self.ui.leToken.textChanged.connect(self.autoCapitalize)

        self.ui.lbPosition.setStyleSheet("color: #FFFFFF")
        self.ui.leAmount.textEdited.connect(self.updatePositionTip)
        self.ui.leLeverage.textEdited.connect(self.updatePositionTip)


        # 默认U本位
        self.ui.rbtnUsdtBase.setChecked(True)


        # 开多
        self.ui.btnMakeLong.clicked.connect(self.makeLong)

        # 开空
        self.ui.btnMakeShort.clicked.connect(self.makeShort)

        # 添加币种
        self.ui.btnAddToken.clicked.connect(self.addToken)


        # 删除币种
        self.ui.btnDeleteToken.clicked.connect(self.deleteToken)


        self.initTargetView()

        #  密钥添加
        self.ui.btnSaveApiKeySecret.clicked.connect(self.saveApiKeySecret)


        # 市价全平（选中）
        self.ui.btnClosePosition.clicked.connect( self.closePosition)

        # 获取当前仓位
        self.ui.btnGetCurrentPosition.clicked.connect(self.getCurrentPositionInfo)

        pass

    def updatePositionTip(self, txt):
        """更新可开仓位数据"""

        txtAmount = self.ui.leAmount.text()
        txtLeverage = self.ui.leLeverage.text()

        if len(txtAmount) > 0 and len(txtLeverage) > 0:
            position = float(txtAmount) * float(txtLeverage)
            if position >= 10:
                position = '%.1f'%position
                self.ui.lbPosition.setText('实际仓位: {} USDT'.format(position))
                self.ui.lbPosition.setStyleSheet("color: #000000")
            else:
                position = '%.1f'%position
                self.ui.lbPosition.setText('仓位无效! {} USDT'.format(position))
                self.ui.lbPosition.setStyleSheet("color: #FF0000")

        pass


    def getCurrentPositionInfo(self):
        """获取仓位信息"""
        if self.bnUmWrapper is None:
            QMessageBox.warning(self, '提示', f"请先添加账户API密钥", QMessageBox.Yes)
            return

        positions = self.bnUmWrapper.getCurrentPosition()


        # 币种, 方向, 杠杆倍数， 建仓价格， 盈亏，
        headers = ['交易对', '保证金模式', '方向', '杠杆倍数', '数量(币)', '估值($)', '开仓价','当前标记价', '预估强平价', '未实现盈亏($)']
        self.posModel = QStandardItemModel(len(positions), len(headers), self)
        self.posModel.setHorizontalHeaderLabels(headers)

        for row in range(len(positions)):
            self.posModel.setItem(row, 0, QStandardItem( str(positions[row]['symbol'] )))

            marginMode = '逐仓' if positions[row]['marginType'] == 'isolated' else '全仓'
            self.posModel.setItem(row, 1, QStandardItem( str(marginMode )))

            side = '空' if positions[row]['side'] == 'SELL' else '多'
            tmpItem = QStandardItem( side)
            if side == '空':
                tmpItem.setForeground(QBrush(QColor(189, 14, 3)))
            else:
                # tmpItem.setForeground()
                tmpItem.setForeground(QBrush(QColor(1, 150, 40)))
            self.posModel.setItem(row, 2, tmpItem)

            self.posModel.setItem(row, 3, QStandardItem( str(positions[row]['leverage'] + 'x' )))

            amt = str(positions[row]['positionAmt']).replace('-', '')
            self.posModel.setItem(row, 4, QStandardItem( str(amt)))
            self.posModel.setItem(row, 5, QStandardItem( str(positions[row]['notional'] )))

            self.posModel.setItem(row, 6, QStandardItem( str(positions[row]['entryPrice'] )))
            self.posModel.setItem(row, 7, QStandardItem( str(positions[row]['markPrice'] )))
            self.posModel.setItem(row, 8, QStandardItem( str(positions[row]['liquidationPrice'] )))


            profit = str(positions[row]['unRealizedProfit'] )
            xItem = QStandardItem( profit )
            if float(profit) < 0:
                xItem.setForeground(QBrush(QColor(189, 14, 3)))
            else:
                xItem = QStandardItem( '+' + profit )
                xItem.setForeground(QBrush(QColor(1, 150, 40)))
            self.posModel.setItem(row, 9, xItem)

        self.ui.tableViewCurPositions.setModel(self.posModel)
        self.ui.tableViewCurPositions.show()


        pass


    def saveApiKeySecret(self):
        """保存密钥信息"""


        if not self.testApiKey():
            return

        ak  = self.ui.leApiKey.text()
        sk = self.ui.leSecretKey.text()

        query = QSqlQuery(self.db)
        query.exec("""DELETE from tb_account WHERE tag='default'""")


        tmpAk = ak[-37:] + ak[:-37]
        tmpSk = sk[-27:] + sk[:-27]
        if query.exec("""INSERT INTO tb_account(tag, ak, sk) VALUES('default','{0}','{1}')""".format(tmpAk, tmpSk)):
            QMessageBox.information(self, '提示', f"操作成功", QMessageBox.Yes)
            self.bnUmWrapper = BnUmWrapper(apiKey=ak, secretKey=sk)

            self.ui.leApiKey.setText('')
            self.ui.leSecretKey.setText('')



        else:
            QMessageBox.warning(self, '提示', f"操作失败", QMessageBox.Yes)

    def testApiKey(self):
        """测试api密钥是否可用"""
        apikey  = self.ui.leApiKey.text()
        apiSecret = self.ui.leSecretKey.text()

        if not len(apikey) == 64:
            QMessageBox.warning(self, '提示', f"API密钥长度不为64, 请检查", QMessageBox.Yes)
            return True
        if not len(apiSecret) == 64:
            QMessageBox.warning(self, '提示', f"密钥长度不为64,请检查", QMessageBox.Yes)
            return False
        tmpBnUmWrapper = BnUmWrapper(apiKey=apikey, secretKey=apiSecret)

        try:
            tmpBnUmWrapper.getTokenBalance('USDT')
            return True
        except ClientError as error:
            logging.error("error_code: {}, error_msg:{}".format(error.error_code, error.error_message))
            QMessageBox.warning(self, '提示', "测试失败, 错误码:{} 错误信息: {}".format(error.error_code, error.error_message), QMessageBox.Yes)
            return False

    def loadApiKey(self):
        """加载apikey"""
        query = QSqlQuery(self.db)
        if not query.exec("""SELECT * from tb_account WHERE tag='default'"""):
            print("查询tb_tokenlist失败")
            raise Exception('查询tb_tokenlist失败')
        if query.next():
            ak = query.value("ak")
            sk = query.value("sk")

            if len(ak) == 64 and len(sk) == 64:
                ak = ak[37:] + ak[:37]
                sk = sk[27:] + sk[:27]
                return ak, sk
        else:
            return '', ''


    def closeEvent(self,event):
        """重载窗口关闭事件， 关闭数据库"""

        # reply = QMessageBox.question(self, '警告',"系统将退出，是否确认?", QMessageBox.Yes |QMessageBox.No, QMessageBox.No)

        # if reply == QMessageBox.Yes:
        #     event.accept()
        # else:
        #     event.ignore()

        print('=====close db===========')
        self.db.close()

        super().closeEvent(event)

    def autoCapitalize(self, txts):
        txts = str(txts).strip()
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
        # print('OnSelectionChanged')
        #选择项改变后，遍历选择的行，将第一列设置为Qt.Checked状态，遍历未选择的行，将未选择的行设置为Qt.Unchecked状态。
        for item in selectlist.indexes():
            rowNum = item.row()
            colNum = item.column()
            if self.targetItemModel.item(rowNum, colNum) is not None:
                # 0:Qt.Unchecked, 1:Qt.PartiallyChecked, 2:Qt.Checked
                self.targetItemModel.item(rowNum, colNum).setCheckState(Qt.CheckState.Checked)

        for item in deselectlist.indexes():
            rowNum = item.row()
            colNum = item.column()
            if self.targetItemModel.item(rowNum, colNum) is not None:
                self.targetItemModel.item(rowNum, colNum).setCheckState(Qt.CheckState.Unchecked)

    def OnCheckBoxItemChanged(self, item):
        # print('OnCheckBoxItemChanged')
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
        self.targetlist = self.loadTokenAsTableviewTargets()
        print(self.targetlist)

        # 列头，用数字表述
        columnHears = []
        if len(self.targetlist) > 0 :
            cols = len(self.targetlist[0])
            for i in range(1, cols):
                columnHears.append( f'{i}')

        #每次导入时将Model中的数据清除，重新初始化
        self.targetItemModel.clear()
        #第一列没有名称，为CheckBox
        self.targetItemModel.setHorizontalHeaderLabels(tuple(columnHears))
        # self.ui.tableView.verticalHeader().hide()  #列表头不显示
        self.ui.tableView.horizontalHeader().setHighlightSections(False)


        for row in range(len(self.targetlist)):
            for col in range(len(self.targetlist[0])):
                if col <  len(self.targetlist[row]):
                    cell = QStandardItem(str(self.targetlist[row][col]))
                    cell.setCheckable(True)
                    cell.setEditable(False)
                    self.targetItemModel.setItem(row, col, cell)
                else:
                    # 那些空白格子不能操作
                    cell = QStandardItem()
                    cell.setEnabled(False)
                    self.targetItemModel.setItem(row, col, cell)

        self.ui.tableView.show()


    def __initDatabase__(self):
        self.db  = QSqlDatabase.addDatabase('QSQLITE')#指定数据库类型
        #指定SQLite数据库文件名
        self.db.setDatabaseName('future.db')
        self.db.setUserName("futurebitcoin2023")
        self.db.setPassword("makemoremoney2023")
        if not self.db.open():
            raise Exception('无法建立与数据库的连接')

        if len(self.db.tables()) == 0:
            query = QSqlQuery(self.db)
            # self.sqlQuery = query

            # 创建tokenlist表
            ret = query.exec("""CREATE TABLE tb_tokenlist (
                token VARCHAR(10) PRIMARY KEY
            )""")
            if False == ret:
                raise Exception("创建表tb_tokenlist失败")

            ret = query.exec("""CREATE TABLE tb_account(
                tag VARCHAR(10) PRIMARY KEY,
                ak VARCHAR(100),
                sk VARCHAR(100)
            )""")
            if False == ret:
                raise Exception("创建表失败")

            print('数据库创建成功')
        else:
            print("数据库已经存在")

    def loadTokens(self):
        """加载代币"""
        query = QSqlQuery(self.db)
        if not query.exec("""SELECT * from tb_tokenlist WHERE 1=1"""):
            print("查询tb_tokenlist失败")

        tokens = []
        while query.next():
            t = query.value("token")
            print(t)
            tokens.append(t)

        print(tokens)
        return tokens

    def loadTokenAsTableviewTargets(self):
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
        for i in range(1, len(tokens) + 1):
            row.append(tokens[i -1 ])
            if (i % 10) == 0:
                tables.append(row)
                row = []
        if len(row) > 0:
            tables.append(row)
        return tables


    def addToken(self):
        """添加币种"""
        if self.bnUmWrapper is None:
            QMessageBox.warning(self, '提示', f"请先添加账户API密钥", QMessageBox.Yes)
            return

        token = self.ui.leToken.text()

        if token.endswith('USDT'):
            token = token.replace('USDT', '')

        found = False
        if self.bnUmWrapper.exchangeInfo is None:
            self.bnUmWrapper.getPrecision('BTCUSDT')

        for x in self.bnUmWrapper.exchangeInfo['symbols']:
            if x['symbol'] == token+'USDT':
                found = True
                break
        if not found:
            QMessageBox.warning(self, '提示', f"{token}USDT交易对在币安不存在,请确认", QMessageBox.Yes)
            return

        print(f'add token {token}')
        reply = QMessageBox.question(self, '提示', f"是否添加: {token} ?", QMessageBox.Yes |QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.No:
            return

        query = QSqlQuery(self.db)
        query.exec("""SELECT * from tb_tokenlist WHERE `token`='{0}'""".format(token))
        if query.next():
            QMessageBox.warning(self, '提示',f"{token}已经存在", QMessageBox.Yes)
            return

        # 切换到逐仓模式
        if not self.bnUmWrapper.changeMarginTypeToIsolated(symbol=token+'USDT'):
            QMessageBox.warning(self, '提示',f"{token}切换逐仓模式失败", QMessageBox.Yes)
            return

        if not query.exec("""INSERT INTO tb_tokenlist(token) VALUES('{0}')""".format(token)):
            QMessageBox.warning(self, '错误',f"{token}添加失败", QMessageBox.Yes)

        self.ui.leToken.setText('')

        # 更新界面
        self.LoadTarget()
        pass

    def deleteToken(self):
        """删除币种"""
        print('delete token')

        if self.bnUmWrapper is None:
            QMessageBox.warning(self, '提示', f"请先添加账户API密钥", QMessageBox.Yes)
            return

        token = self.ui.leToken.text()

        if token.endswith('USDT'):
            token = token.replace('USDT', '')

        print(f'delete token {token}')
        reply = QMessageBox.question(self, '提示', f"是否删除: {token} ?", QMessageBox.Yes |QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.No:
            return

        query = QSqlQuery(self.db)
        if not query.exec("""DELETE from tb_tokenlist WHERE `token`='{0}'""".format(token)):
            errText = query.lastError().text()
            QMessageBox.warning(self, '错误',f"{token}删除失败: {errText}", QMessageBox.Yes)


        # 更新界面
        self.LoadTarget()
        self.ui.leToken.setText('')



    def checkOrderData(self, side: str):
        """检查订单参数"""
        if self.bnUmWrapper is None:
            QMessageBox.warning(self, '提示', f"请先添加账户API密钥", QMessageBox.Yes)
            return

        # 是否选择了币种
        symbols = self.getSelectedSymbols()
        print(symbols)
        if len(symbols) == 0:
            print("请选择币种")
            QMessageBox.question(self, '提示', f"请选择币种", QMessageBox.Yes)
            return False

        # 检查是否有重复仓位？
        positions = self.bnUmWrapper.getCurrentPosition()
        for pos in positions:
            if pos['symbol'] in symbols:
                token = str(pos['symbol']).replace('USDT', '')
                QMessageBox.warning(self, '提示', f"已存在{token}的仓位,不支持追加持仓或双向持仓，请平仓后继续", QMessageBox.Yes)
                return False

        # 有效性检查:
        # txType = ''
        # if self.ui.rbtnUsdtBase.isChecked():
        #     txType = 'U'
        # else:
        #     txType = '币'

        # if not self.ui.rbtnTokenBase.isChecked() and not self.ui.rbtnUsdtBase.isChecked():
        #     QMessageBox.question(self, '提示', f"请选择'类型'", QMessageBox.Yes)
        #     return False

        # 检查杠杆倍数
        txtLeverage = self.ui.leLeverage.text()
        if len(txtLeverage) == 0:
            QMessageBox.question(self, '提示', f"请输入'倍数'", QMessageBox.Yes)
            return False

        # 检查止损
        txtStoplossRatio = self.ui.leStopLossRatio.text()
        if len(txtStoplossRatio) == 0:
            QMessageBox.question(self, '提示', f"请输入'止损'", QMessageBox.Yes)
            return False

        # 检查数量
        txtAmout = self.ui.leAmount.text()
        if len(txtAmout) == 0:
            QMessageBox.question(self, '提示', f"请输入'数量'", QMessageBox.Yes)
            return False

        if float(txtAmout) * float(txtLeverage) < 10:
            QMessageBox.question(self, '提示', f"仓位必须大于10U,请增大保证金数量", QMessageBox.Yes)
            return False


        # 下单数据确认
        sideTip = '空' if side == 'SELL' else '多'
        positionAmount = '%.1f' %( float(txtAmout) * float(txtLeverage))
        if True:
            tips = f"\n一共{len(symbols)}个交易对\n类型: U本位\n方向: {sideTip}\n杠杆: {txtLeverage}x\n止损:{txtStoplossRatio}%\n仓位: {positionAmount} USDT"
            r = QMessageBox.question(self, '下单参数确认', tips, QMessageBox.Yes, QMessageBox.No)
            if r == QMessageBox.No:
                return False


        # 检查账户余额
        if True:
            usdtAmount = float(self.ui.leAmount.text())
            totalBalance = len(symbols) * usdtAmount
            usdtBalance = self.bnUmWrapper.getTokenBalance(token='USDT')
            if usdtBalance - totalBalance < 0.01 * len(symbols):
                QMessageBox.question(self, '提示', f"当前账户可用USDT余额{usdtBalance}不足, 请充值后重试!", QMessageBox.Yes)
                return False

        # 风险提醒
        if True:
            if int(txtLeverage) >= 10:
                r = QMessageBox.question(self, '提示', f"{int(txtLeverage)}倍杠杆是高风险交易,是否继续？", QMessageBox.Yes, QMessageBox.No)
                if r == QMessageBox.No:
                    return False
            if int(txtStoplossRatio) > 10:
                r = QMessageBox.question(self, '提示', f"{txtStoplossRatio}% 止损率过高, 当亏损超过{txtStoplossRatio}%才会出发止损, 是否继续？", QMessageBox.Yes, QMessageBox.No)
                if r == QMessageBox.No:
                    return False
            if self.ui.rbtnUsdtBase.isChecked() and int(txtAmout) > 100:
                r = QMessageBox.question(self, '提示', f"数量{txtAmout}, 较大, 是否继续？", QMessageBox.Yes, QMessageBox.No)
                if r == QMessageBox.No:
                    return False

         # 将所有币对,切换到逐仓模式
        tokens = self.loadTokens()
        for t in tokens:
            symbol = t + 'USDT'
            if not self.bnUmWrapper.changeMarginTypeToIsolated(symbol=symbol):
                # query.exec("""DELETE from tb_tokenlist WHERE token='{0}'""".format(t))
                QMessageBox.warning(self, '提示', f"切换{symbol}交易对到逐仓模式失败,请联系管理员!", QMessageBox.Yes)
                return False

        return True

    def getSelectedSymbols(self):
         # 获取下单
        symbols = []
        for row in range(self.targetItemModel.rowCount()):
            for col in range(self.targetItemModel.columnCount()):
                item  = self.targetItemModel.item(row, col)
                if item.checkState() == Qt.CheckState.Checked:
                    token = item.text() + 'USDT'
                    symbols.append( token.upper() )
        return symbols

    def makeLong(self ):
        """
        市价开多
        """
        print("makeLong")

        self.__makeOrder(side='BUY')



    def makeShort(self):
        """
        市价开空
        """
        print("makeShort")
        self.__makeOrder(side='SELL')




    def __makeOrder(self, side: str):

        try:
            self.processDialog = ProgressDialog(parent=self)


            self.disableAllButton()

            assert side in ['BUY', 'SELL']

            if not self.checkOrderData(side):
                return

            symbols = self.getSelectedSymbols()

            usdtAmount = float(self.ui.leAmount.text())
            stopRatio = float(self.ui.leStopLossRatio.text())/100
            leverage = int(self.ui.leLeverage.text())

            # 创建下单线程
            self.orderThread = CreateOrderThread(self.bnUmWrapper,
                                                symbols=symbols,
                                                usdtAmount=usdtAmount,
                                                side=side,
                                                stopRatio=stopRatio,
                                                leverage=leverage
            )
            self.orderThread.finishSignal.connect(self.showCreateOrdersThreadResult)
            self.orderThread.progressSignal.connect(self.processDialog.setProgress)

            self.orderThread.start()

            self.processDialog.exec()

            print('===========下单线程已启动============')

        except Exception as e:
            logging.error(" error:  {}".format(e))
            self.enableAllButton()
            pass

    def disableAllButton(self):
        # self.ui.btnMakeLong.setEnabled(False)
        # self.ui.btnMakeShort.setEnabled(False)
        # self.ui.btnAddToken.setEnabled(False)
        # self.ui.btnDeleteToken.setEnabled(False)
        # self.ui.btnClosePosition.setEnabled(False)
        # self.ui.btnSaveApiKeySecret.setEnabled(False)
        # self.ui.btnGetCurrentPosition.setEnabled(False)
        pass

    def enableAllButton(self):
        # self.ui.btnMakeLong.setEnabled(True)
        # self.ui.btnMakeShort.setEnabled(True)
        # self.ui.btnAddToken.setEnabled(True)
        # self.ui.btnDeleteToken.setEnabled(True)
        # self.ui.btnClosePosition.setEnabled(True)
        # self.ui.btnSaveApiKeySecret.setEnabled(True)
        # self.ui.btnGetCurrentPosition.setEnabled(True)
        pass

    def showCreateOrdersThreadResult(self, count, code, msg):
        """显示显示线程执行结果"""
        self.enableAllButton()
        if code == 0:
            QMessageBox.information(self, "提示", f"下单{count}笔成功!", QMessageBox.Yes)
        elif code == -4028:
            QMessageBox.warning(self, '提示', f"成功下单{count}笔,第{count+1}笔失败, 错误码:{code},信息：杠杆倍数无效，超过最大倍数,{msg}", QMessageBox.Yes)
        else:
            QMessageBox.warning(self, '提示', f"成功下单{count}笔,第{count+1}笔失败, 错误码:{code},信息：{msg}", QMessageBox.Yes)



    def showCloseAllPositionsThreadResult(self,  code, msg):
        """显示显示线程执行结果"""
        self.enableAllButton()
        if code == 0:
            QMessageBox.information(self, "提示", f"操作成功!", QMessageBox.Yes)
        else:
            QMessageBox.warning(self, '提示', f"操作失败, 错误码:{code},信息：{msg}", QMessageBox.Yes)
        self.getCurrentPositionInfo()



    def closePosition(self):
        """市价平仓"""

        if self.bnUmWrapper is None:
            QMessageBox.warning(self, '提示', f"请先添加账户API密钥", QMessageBox.Yes)
            return

        print("市价全平，并撤销所有委托单")
        reply = QMessageBox.question(self, '提示', f"所有币种按照市价平仓，并且撤销所有委托单，是否继续？", QMessageBox.Yes, QMessageBox.No)
        if reply != QMessageBox.Yes:
            return

        self.disableAllButton()

        self.orderThread = CloseAllPositionThread(self.bnUmWrapper)
        self.orderThread.finishSignal.connect(self.showCloseAllPositionsThreadResult)
        self.orderThread.start()


class ProgressDialog(QDialog):
    """进度条"""

    def __init__(self, parent:None):
        super().__init__(parent=parent)
        self.setWindowTitle('请耐心等待,当前操作进度:')

        # 创建进度条和取消按钮
        self.progressBar = QProgressBar()

        # 布局控件
        layout = QVBoxLayout()
        layout.addWidget(self.progressBar)
        self.setLayout(layout)

    def setProgress(self, percentage):
        # 更新进度条的值
        self.progressBar.setValue(percentage)
        if percentage == 100:
            self.close()



class CloseAllPositionThread(QThread):
    """全部平仓线程"""
    finishSignal = Signal(int,  str)

    def __init__(self, bnUmWrapper):
        self.bnUmWrapper = bnUmWrapper
        super().__init__()

    def run(self):
        try:
            self.bnUmWrapper.closeAllPositionMarket()
            self.bnUmWrapper.cancelAllOrders()
            self.finishSignal.emit(  0, '')
        except ClientError as error:
            logging.error("Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message))
            self.finishSignal.emit(  error.error_code, error.error_message)
        except Exception as e:
            logging.error("{}".format(e))
            self.finishSignal.emit(  -1, '{}'.format(e))


        pass


class CreateOrderThread(QThread):
    """下单线程"""

    finishSignal = Signal(int, int, str)
    progressSignal = Signal(int)  # 进度信号

    def __init__(self, bnUmWrapper, symbols, usdtAmount, side, stopRatio, leverage):
        self.bnUmWrapper = bnUmWrapper
        self.symbols = symbols
        self.usdtAmount = usdtAmount
        self.side = side
        self.stopRatio = stopRatio
        self.leverage = leverage
        super().__init__()

    def run(self):
        count = 0
        for symbol in self.symbols:
            try:
                resp = self.bnUmWrapper.createNewOrders(
                        usdtQuantity=self.usdtAmount,
                        symbol=symbol,
                        side=self.side,
                        stopRatio=self.stopRatio,
                        leverage=self.leverage
                    )
                if resp is not None:
                    if 'code' in resp[0] and resp[0]['code'] != 0:
                        raise ClientError(resp[0]['code'],resp[0]['code'], resp[0]['msg'], None )
            except ClientError as error:
                logging.error("Found error. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message))
                # QMessageBox.warning(self, '错误', f"{error.error_message}", QMessageBox.Yes)
                self.finishSignal.emit( count,  error.error_code, error.error_message)
                self.progressSignal.emit(100)
                return
            except Exception as e:
                logging.error("error: {}".format(e))
                self.progressSignal.emit(100)
                return

            count += 1
            process = int(count/len(self.symbols) * 100)
            self.progressSignal.emit(process)


        self.progressSignal.emit(100)
        self.finishSignal.emit( count,  0, '')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
