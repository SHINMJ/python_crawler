import sys
import time
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QProgressBar, QMainWindow


class Test_ProgressBar(QMainWindow):

    def __init__(self):
        super(Test_ProgressBar, self).__init__()
        self.setGeometry(850, 300, 230, 120)
        self.setWindowTitle('Test_ProgressBar')
        self.ProgressBarShow()

    
    def ProgressBarShow(self):
        self.progressbar1 = QProgressBar(self)
        self.progressbar1.setGeometry(30, 40, 200, 25)
        self.progressbar1.setMinimum(0)
        self.progressbar1.setMaximum(10)

        self.bl = QPushButton('Start', self)
        self.bl.move(30, 65)
        self.bl.clicked.connect(self.action1)

    
    def action1(self):
        for i in range(11):
            if i == 10:
                self.bl.setText('Completed')
                self.progressbar1.setValue(i)
                time.sleep(1)

            else:
                self.progressbar1.setValue(i)
                time.sleep(1)
                i = i+1


    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Test_ProgressBar()
    ex.show()
    sys.exit(app.exec_())