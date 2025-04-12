import sys
from PySide6.QtWidgets import QApplication, QMainWindow,QVBoxLayout, QDialog
from ui_test2 import Ui_MainWindow


class Test_Window (Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_2.clicked.connect(lambda: self.canceled())
        self.checkBox.clicked.connect(lambda: self.check_test())

        self.ok= self.pushButton.clicked

        # self.checkBox_is_checked = True
        # self.checkBox_2_is_checked = True

        self.B_checked= self.checkBox.clicked
        self.L_checked= self.checkBox_2.clicked

    def canceled(self):
        self.pushButton_2.setText("I am pressed")
        print("You canceled")

    def  check_test(self):
        print("I'm checked")
    
    def ok_dinner(self):
        print ("You only have dinner left")
    

    def two_checkboxes (self):
        while self.B_checked and self.L_checked:
            if self.ok:
                self.ok.connect(lambda: self.ok_dinner())
            else:
                self.canceled
    

# idea for when I go home, Idea is to go ahead and have breakfast and dinner buttons pressed along wiht ok
# Have them say at the end ok you have dinner left. (Goal is to set the remainder of calories I need)
# --------------------------------------------------------------------------------------------------------------
"""
    def check_morning(self):
        self.checkBox.setCheckable(True)
        self.checkBox.setChecked(self.checkBox_is_checked)
    
    def lunch_check(self):
        self.checkBox_2.setCheckable(True)
        self.checkBox_2.setChecked(self.checkBox_2_is_checked)
"""
#So update, if statement doesn't work. Idea is setting the checkboxes to checkable


app = QApplication(sys.argv)
window = Test_Window()
window.show()
app.exec()