#encoding utf-8
import os,sys,time
from uipdfreader import Ui_MainWindow
from PyQt5.QtCore import QThread, QObject, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow



def write_line_2_txt(name,data):
    name = name.strip('.txt')+'.txt'
    str_data = data.strip('\n')+'\n'
    try:
        out_gcap = open(name,"a+")#文件不存在就会新建，a+读写模式，默认指针在末尾
        print(str_data)
        out_gcap.write(str_data)
        out_gcap.close()
    except IOError:
         print("File error")


def openpdf(pdf_reader,pdffile):
    cmd = 'start "{}" "{}"'.format(pdf_reader,pdffile)
    try:
        os.system(cmd)
    except Exception as erro:
        print(erro)

class fun_main(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.pushButton_callback)
        self.pushButton_2.clicked.connect(self.pushButton_2_callback)
        self.pushButton_3.clicked.connect(self.pushButton_3_callback)
        self.logifle='pdf_open_his.txt'
        self.pdfreader_file = 'pdfreader.txt'
        self.pdfreader = r"C:\Program Files (x86)\Adobe\Acrobat 10.0\Acrobat\Acrobat.exe"
        try:
            with open(self.logifle, 'r') as f:  # 打开文件
                lines = f.readlines()
                for lin in lines:
                    self.textBrowser.append(lin.strip('\n'))
        except Exception as erro:
            print(erro)
        try:
            with open(self.pdfreader_file, 'r') as f:  # 打开文件
                pdfreader = f.readlines()[-1].strip('\n')
                self.pdfreader = pdfreader
        except Exception as erro:
            print(erro)
        self.lineEdit_2.setText(self.pdfreader)


    def pushButton_callback(self):
        print(self.pushButton.text())
        pdffiles = self.plainTextEdit.toPlainText().split("\n")
        log = ''
        for pdffile in pdffiles:
            if pdffile:
                openpdf(self.pdfreader, pdffile)
                new_line = '{} {}'.format(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()), pdffile)
                self.textBrowser.append(new_line)
                log = log + new_line + '\n'
        write_line_2_txt(self.logifle, log)
        self.plainTextEdit.setPlainText("")

    def pushButton_2_callback(self):
        print(self.pushButton_2.text())
        try:
            opne_last_num  = int(eval(self.lineEdit.text()))
        except Exception as erro:
            print(erro)
            opne_last_num=10

        with open(self.logifle, 'r') as f:  # 打开文件
            lines = f.readlines()
        for index in range(1,opne_last_num+1):
            pdffile=lines[-index][20:].strip("\n")
            if pdffile:
                openpdf(self.pdfreader,pdffile)

    def pushButton_3_callback(self):
        print(self.pushButton_3.text())
        try:
            pdfreader  = self.lineEdit_2.text()
            self.pdfreader=pdfreader
            write_line_2_txt(self.pdfreader_file, pdfreader)
        except Exception as erro:
            print(erro)





if __name__=="__main__":
    app = QApplication(sys.argv)
    ui = fun_main()
    ui.show()
    sys.exit(app.exec())

    
