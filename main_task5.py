import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QColor

from ui_task5 import Ui_MainWindow

class AntiplagiatApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
       
        self.ui.btn_check.clicked.connect(self.check_texts)

    def check_texts(self):
        
        text1 = self.ui.textEdit_1.toPlainText().strip()
        text2 = self.ui.textEdit_2.toPlainText().strip()
        
       
        if not text1 or not text2:
            self.ui.statusbar.setStyleSheet("color: orange;")
            self.ui.statusbar.showMessage("Ошибка: Оба текста должны быть заполнены!")
            return

   
        lines1 = [line.strip() for line in text1.split('\n') if line.strip()]
        lines2 = [line.strip() for line in text2.split('\n') if line.strip()]
        
        
        if not lines1 or not lines2:
            self.ui.statusbar.setStyleSheet("color: orange;")
            self.ui.statusbar.showMessage("Ошибка: Тексты не должны состоять только из пустых строк!")
            return

        
        set1 = set(line.lower() for line in lines1)
        set2 = set(line.lower() for line in lines2)
        
        matching_lines = set1.intersection(set2)
        
        
        max_lines = max(len(lines1), len(lines2))
        match_percent = (len(matching_lines) / max_lines) * 100
        
        
        threshold = self.ui.doubleSpinBox_threshold.value()
        
    
        result_text = f"Совпадение: {match_percent:.1f}% (Порог: {threshold}%)"
        
        if match_percent >= threshold:
            self.ui.statusbar.setStyleSheet("color: red;") 
            self.ui.statusbar.showMessage(f"Текст НЕ уникален. {result_text}")
        else:
            self.ui.statusbar.setStyleSheet("color: green;") 
            self.ui.statusbar.showMessage(f"Текст уникален. {result_text}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AntiplagiatApp()
    window.show()
    sys.exit(app.exec())