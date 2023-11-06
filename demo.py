from PySide6.QtCore import Qt, QThread, Signal
from PySide6.QtWidgets import QApplication, QDialog, QProgressBar, QVBoxLayout, QPushButton

class ProgressDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Progress Dialog')

        # 创建进度条和取消按钮
        self.progressBar = QProgressBar()
        self.cancelButton = QPushButton('Cancel')

        # 布局控件
        layout = QVBoxLayout()
        layout.addWidget(self.progressBar)
        layout.addWidget(self.cancelButton)
        self.setLayout(layout)

    def setProgress(self, percentage):
        # 更新进度条的值
        self.progressBar.setValue(percentage)

    def closeEvent(self, event):
        # 关闭窗口时发送cancel信号
        self.cancelSignal.emit()

    cancelSignal = Signal()

class WorkerThread(QThread):
    progressSignal = Signal(int)  # 进度信号

    def run(self):
        for i in range(101):
            if self.isInterruptionRequested():
                break

            # 发送当前进度信号
            self.progressSignal.emit(i)

            # 模拟一些工作时间
            QThread.msleep(50)
if __name__ == '__main__':
    app = QApplication([])

    dialog = ProgressDialog()

    thread = WorkerThread()
    thread.progressSignal.connect(dialog.setProgress)
    dialog.cancelButton.clicked.connect(thread.requestInterruption)
    dialog.cancelSignal.connect(thread.requestInterruption)

    thread.start()

    dialog.exec()

    thread.wait()

    app.exit()