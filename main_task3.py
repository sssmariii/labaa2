import sys
from PySide6.QtWidgets import QApplication, QMainWindow

from ui_task3 import Ui_MainWindow

class NotebookApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        
        self.ui.btn_add.clicked.connect(self.add_contact)

    def add_contact(self):
        #
        name = self.ui.lineEdit_name.text().strip()
        phone = self.ui.lineEdit_phone.text().strip()
        
       
        if not name or not phone:
            return
            
        
        contact_info = f"{name} - {phone}"
        
        
        self.ui.listWidget_contacts.addItem(contact_info)
        
        
        self.ui.lineEdit_name.clear()
        self.ui.lineEdit_phone.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NotebookApp()
    window.show()
    sys.exit(app.exec())