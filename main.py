import os
import sys

from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication


################################################################################################
# Convert UI to PyQt5 py file
################################################################################################

#os.system("pyuic5 -o interface_ui.py interface.ui")

################################################################################################
# Import the generated UI
################################################################################################
from interface_ui import *

################################################################################################
# MAIN WINDOW CLASS
################################################################################################
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        ################################################################################################
        # Setup the UI main window
        ################################################################################################
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.widget.units = "kg/m²"
        self.ui.widget.minValue = 0
        self.ui.widget.maxValue = 50
        self.ui.widget.setScalaCount(10)
        self.ui.widget.setGaugeTheme(3)
        self.ui.widget.updateValue(0)




        self.ui.widget.setScalePolygonColor(
            color1="red",
            color2="yellow",
            color3="green",
            color4="green"
            
            )
        ################################################################################################
        # Show window
        ################################################################################################
        self.show()




########################################################################
## EXECUTE APP
########################################################################
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ########################################################################
    ## 
    ########################################################################
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


########################################################################
## END===>
########################################################################  