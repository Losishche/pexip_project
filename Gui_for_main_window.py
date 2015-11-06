
import sys
from PyQt4 import QtGui, QtCore
from  start_file import dialing_a_participant_into_a_conference
from  start_file import Participant

obj = Participant('Dmitry', 'meet1@example.com', '185.35.201.84' )

class Pusher(QtGui.QMainWindow):

    def __init__(self, parent= None):
        QtGui.QMainWindow.__init__(self, parent)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Push')
        exit = QtGui.QAction(QtGui.QIcon('icons/exit.png'), 'Exit', self)
        exit.setShortcut('Ctrl+Q')
        exit.setStatusTip('Exit application')

        self.connect(exit, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))

        menubar = self.menuBar()
        file = menubar.addMenu('&File')
        file.addAction(exit)

        btnDial = QtGui.QPushButton('подключить', self)
        btnDial.setGeometry(75, 75, 150, 30)
        btnDisconnect = QtGui.QPushButton('отключить', self)
        btnDisconnect.setGeometry(100, 95, 150, 30)

        self.connect(btnDial, QtCore.SIGNAL('clicked()'), obj.dialing_a_participant_into_a_conference) # последний параметр - это пользовательская ф-я - обработчик.
                                                                                                   # Вместо ф-ии можно использовать метод класса или экземпляр класса
                                                                                                   # (в последнем случае, в классе должен быть опред. метод call)
        self.connect(btnDisconnect, QtCore.SIGNAL('clicked()'), quit)

app = QtGui.QApplication(sys.argv)
pusher = Pusher()
pusher.show()

sys.exit(app.exec_())