import sys
from PyQt4 import QtGui, QtCore
from controllers import button

class Window( QtGui.QMainWindow ):

    def __init__( self, title ):
        super( Window, self ).__init__()
        self.setWindowTitle( title )
        self.setGeometry( 700, 700, 1000, 1000 )
        self.home()

    def home( self ):
        quit_btn = button("Quit")
        #quit_btn.clicked.connect( button.quit() )
        quit_btn.move( 300, 300 )
        self.show()
