import sys
from PyQt4 import QtGui
from PyQt4 import QtCore

class SystemTray(QtGui.QSystemTrayIcon):
    def __init__(self, icon, parent=None):
        super(SystemTray, self).__init__(icon, parent)

        self.menu = QtGui.QMenu(parent)
        settings_action = self.menu.addAction("Instructions")
        settings_action.triggered.connect(self.open_settings)

        self.menu.addSeparator()

        self.menu = QtGui.QMenu(parent)
        settings_action = self.menu.addAction("Instructions")
        settings_action.triggered.connect(self.open_settings)

        self.menu.addSeparator()

        exit_action = self.menu.addAction("Exit")
        exit_action.triggered.connect(QtCore.QCoreApplication.instance().quit)

        self.setContextMenu(self.menu)
        self.show()

    def open_settings(self):
        settings = SettingsDialog()
        settings.exec_()

class SettingsDialog(QtGui.QDialog):
    def __init__(self):
        super(SettingsDialog, self).__init__()

        self.resize(300, 300)
        self.setWindowTitle('Instructions')
        vbox = QtGui.QHBoxLayout()

        self.channels_list = QtGui.QListView(self)
        vbox.addWidget(self.channels_list)


        self.add_box = QtGui.QLineEdit(self)
        vbox.addWidget(self.add_box)

        self.setLayout(vbox)


class SettingsDialog(QtGui.QDialog):
    def __init__(self):
        super(SettingsDialog, self).__init__()

        self.resize(300, 300)
        self.setWindowTitle('Instructions')
        vbox = QtGui.QHBoxLayout()

        self.channels_list = QtGui.QListView(self)
        vbox.addWidget(self.channels_list)

        self.setLayout(vbox)

        

def main():

    app = QtGui.QApplication(sys.argv)
    widget = QtGui.QWidget()
    tw = SystemTray(QtGui.QIcon("Icon.png"), widget)

    app.exec_()

if __name__ == '__main__':
    main()
