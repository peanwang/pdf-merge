import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import pdf


class MyQWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.initWidget()
        self.initlayout()

    def initUI(self):
        ##  初始化应用程序窗口
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Pdf-merge')
        self.setWindowIcon(QIcon('1.ico'))

    def initWidget(self):
        ## 创建应用需要的部件widget
        self.select = QLabel('选择文件', self)
        self.openfile = QPushButton("select", self)
        self.filelist = QTextEdit(self)
        self.outputfile = QLineEdit(self)
        self.merge = QPushButton('merge', self)
        self.quit = QPushButton('Quit', self)
        self.openfile.clicked.connect(self.slot_1)
        self.merge.clicked.connect(self.slot_2)
        self.quit.clicked.connect(QApplication.quit)

    def initlayout(self):
        ## 初始化布局
        grid = QGridLayout()
        self.setLayout(grid)
        grid.addWidget(self.select, 0, 0, 1, 1)
        grid.addWidget(self.openfile, 0, 3, 1, 1)
        grid.addWidget(self.filelist, 1, 0, 4, 4)
        grid.addWidget(self.outputfile, 6, 0, 1, 4)
        grid.addWidget(self.merge, 7, 2)
        grid.addWidget(self.quit, 7, 3)

    def slot_1(self):
        fileName_choose = QFileDialog.getOpenFileNames(self,
                                                        "select file"
                                                        r'C:\Users\HP\Desktop',
                                                       "*.pdf")
        selectfile = ''
        for i in fileName_choose[0]:
            selectfile +=i
            selectfile +='\n'
        self.filelist.setText(selectfile)

    def slot_2(self):
        selectfile = self.filelist.toPlainText()
        selectfile = selectfile[:-1]
        outfile = self.outputfile.text()

        if len(outfile) > 0:
            infilelist = selectfile.split('\n')
            pdf.Merge(infilelist, outfile)


app = QApplication(sys.argv)
w = MyQWidget()
w.show()
sys.exit(app.exec_())

