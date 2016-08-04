import sys
import subprocess
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):               
        
        self.setGeometry(50, 50, 375, 300)        
        self.setWindowTitle('Message box')
        self.center()
        self.setWindowTitle('Command Line GUI')

        playButton = QtGui.QPushButton("Play")
        pauseButton = QtGui.QPushButton("Pause")
        stopButton = QtGui.QPushButton("Stop")

        playButton.clicked.connect(lambda:self.run('t.py'))
        stopButton.clicked.connect(QtCore.QCoreApplication.instance().quit)

        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(playButton)
        hbox.addWidget(pauseButton)
        hbox.addWidget(stopButton)

        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.lbl = QtGui.QLabel("", self)

        combo = QtGui.QComboBox(self)
        combo.addItem("")
        combo.addItem("Google API")
        combo.addItem("Python Local API")
        combo.addItem("Sphinx API")
        combo.addItem("Local API")
        combo.addItem("Other API")

        combo.move(150, 150)
        self.lbl.move(50, 150)

        combo.activated[str].connect(self.onActivated)


        self.setLayout(vbox)
        self.show()

    def run(self, path):
        subprocess.call(['pythonw',path])

    def onActivated(self, text):
      
        self.lbl.setText(text)
        self.lbl.adjustSize()
        
    def closeEvent(self, event):
        
        reply = QtGui.QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QtGui.QMessageBox.Yes | 
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):
        
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


             
def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
