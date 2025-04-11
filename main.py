import sys
from PySide6.QtWidgets import QApplication, QMainWindow,QVBoxLayout, QDialog
from ui_test2 import Ui_MainWindow


class Test_Window (Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_2.clicked.connect(lambda: self.print_test())
        self.checkBox.clicked.connect(lambda: self.check_test())

    def print_test(self):
        self.pushButton_2.setText("I am pressed")
        print("This worked")

    def  check_test(self):
        print("I'm checked")
        

    def date_update(self):
        print("Update")

   # idea for when I go home, Idea is to go ahead and have breakfast and dinner buttons pressed along wiht ok
   # Have them say at the end ok you have dinner left. (Goal is to set the remainder of calories I need)
   # --------------------------------------------------------------------------------------------------------------
   # def reminder (self):
    #    if self.pushButton.clicked


app = QApplication(sys.argv)
window = Test_Window()
window.show()
app.exec()