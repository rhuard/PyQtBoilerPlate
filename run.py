import sys
from UI import *

"""
create wrapper so we do not have to worry about UI overwrites
since this wrapper calls the constructor for mainwindow and since we have the setup ui called,
we do not need to modify the UI.py, so then if the UI.py is overwriten because of the pyuic then
no worries
"""
class UiWrapper(QtWidgets.QMainWindow):
    ui = None
    def __init__(self, parent=None):
        #call constuctor so we do not have to write anything in the UI.py file
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        #declare and then call setup ui
        self.ui.setupUi(self)

"""
This is a wrapper class so that we can make a logic engine, this wraps the UI so we can access the buttons to form connections.
This can be thought of an adaptor to the other pieces of the logic engine. You can include them and then connect buttons from the UI
to methods in this class which just delegate calls to the other logic engines.
"""
class logic(object):
    ex = None
    def __init__(self):
        self.ex = UiWrapper()
        #connect all the buttons and other things here
        self.ex.ui.pushButton.clicked.connect(self.stuff)
        
        #show the form
        self.ex.show()

    #methods for button connections
    def stuff(self):
        print("stuff")


#run if main
if __name__ == "__main__":
        #boiler plate for QT
        app = QtWidgets.QApplication(sys.argv)
        #declare the logic engine and let that handle the rest
        l = logic()
        #more boiler plate
        sys.exit(app.exec_())
