import CBT
import sys
from PySide6 import QtCore, QtWidgets, QtGui

profile = CBT.Profile("Victor", "2341234", 567, "02/22", "victor coo", "asdfasdf")
profile.AddCoin('ethereum', 1700, 1700, "xx", 'usd')

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("ethereum", alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.ShowCoinInfo)

    @QtCore.Slot()
    def ShowCoinInfo(self):
        self.text.setText(str(profile.aCoinList[0].GetCurrentPrice()))


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec_())