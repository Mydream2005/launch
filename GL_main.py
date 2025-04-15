from PyQt5.QtGui import QCursor, QFont
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QFileDialog, QInputDialog, QLineEdit
from PyQt5.QtCore import Qt
from JsonIO import jsonIO
# from GameLuncher.QtUi.CmdUi import Ui_console
from TestMainUI import Ui_Form
import sys
import os


class MainUI(Ui_Form, QWidget):

    def __init__(self, parent=None):
        super(MainUI, self).__init__(parent=parent)
        self.gamePath = 'GameList.json'
        self.IO = jsonIO()
        self.datas = self.IO.jsoninput(self.gamePath)
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.resize(700, 900)
        self.addList()

    def addList(self):
        self.gameDict = {data['name']: data['path'] for data in self.datas}
        print('游戏目录')
        for key in self.gameDict.keys():
            print(key, '\t\t\t', self.gameDict[key])
        self.listWidget.addItems(self.gameDict.keys())
        self.listWidget.setFont(QFont("仿宋", 18))

    def gameAdd(self):
        dir = QFileDialog()
        dirlist = []
        gamedic = []
        dir.setFileMode(QFileDialog.ExistingFiles)
        dir.setDirectory("D:/Game")
        dir.setNameFilter('可执行程序(*.exe)')
        if dir.exec_():
            dirlist.extend(dir.selectedFiles())
            print(dirlist)
        try:
            for i in dirlist:
                text, ok = QInputDialog.getText(self, 'GameName', '游戏名', QLineEdit.Normal, os.path.splitext(os.path.basename(i))[0])
                if ok:
                    gamedic.append({'name': text, 'path': i, 'icon': ""})
            print(gamedic)
            for i in gamedic:
                self.IO.jsonoutput(self.gamePath, i)
                self.datas = self.IO.jsoninput(self.gamePath)
                self.listWidget.clear()
                self.addList()
        except Exception as e:
            print(str(e))


    def gameDelete(self, name: str):
        for elm in self.datas:
            if elm['name'] == name:
                self.IO.json_delete(self.gamePath, elm)
                break

    def launch(self):
        name = self.listWidget.currentItem().text()
        try:
            if name in self.gameDict.keys():
                print("选择游戏-》", name, self.gameDict[name])
                os.startfile(self.gameDict[name])
        except Exception as e:
            QMessageBox.information(self, '启动失败', f'文件路径不存在{e}', QMessageBox.Ok)
            print(name)
            self.gameDelete(name)
            self.listWidget.clear()
            self.addList()

    def mousePressEvent(self, event):
        """处理鼠标按下事件"""
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))

    def mouseMoveEvent(self, event):
        """处理鼠标移动事件"""
        if Qt.LeftButton and self.m_flag:
            self.move(event.globalPos() - self.m_Position)
            event.accept()

    def mouseReleaseEvent(self, event):
        """处理鼠标释放事件"""
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))


# class Start:
#
#     def __init__(self):
#         self.ui = Ui_console()
#         self.IO = jsonIO()
#
#         self.gamePath = 'GameList.json'
#         self.datas = self.IO.jsoninput(self.gamePath)
#         self.gameList = [data['name'] for data in self.datas]
#
#         self.ui.StartUi()
#         self.ui.Menu(self.gameList)


def main():
    app = QApplication(sys.argv)
    ui = MainUI()
    ui.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
