import sys
from PyQt4 import QtGui
from views import Window

def main():
    app = QtGui.QApplication( [] )
    MainScreen = Window( "Epidemic Simulator" )
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
