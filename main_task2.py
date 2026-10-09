import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QDateTime

from ui_task2 import Ui_MainWindow

class PlannerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        
        self.events = []
        
        
        self.ui.btn_add.clicked.connect(self.add_event)

    def add_event(self):
       
        name = self.ui.lineEdit_event.text().strip()
        date = self.ui.calendarWidget.selectedDate()
        time = self.ui.timeEdit.time()
        
        
        if not name:
            return
            
     
        event_datetime = QDateTime(date, time)
        self.events.append({
            'name': name,
            'date': date,
            'time': time,
            'datetime': event_datetime
        })
        
       
        self.ui.lineEdit_event.clear()
        
        
        self.update_list()

    def update_list(self):
      
        self.events.sort(key=lambda x: x['datetime'])
        
        
        self.ui.listWidget_events.clear()
        
        for event in self.events:
            date_str = event['date'].toString("dd.MM.yyyy")
            time_str = event['time'].toString("hh:mm")
           
            item_text = f"{date_str} {time_str} - {event['name']}"
            self.ui.listWidget_events.addItem(item_text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PlannerApp()
    window.show()
    sys.exit(app.exec())