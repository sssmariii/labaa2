import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_flag import Ui_MainWindow

class FlagApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.setFixedSize(self.size())
        
        self.ui.btn_draw.clicked.connect(self.draw_flag)

    def draw_flag(self):
        colors = []
        
    
        if self.ui.rb1_red.isChecked(): colors.append("Красный")
        elif self.ui.rb1_green.isChecked(): colors.append("Зелёный")
        elif self.ui.rb1_white.isChecked(): colors.append("Белый")
        
    
        if self.ui.rb2_red.isChecked(): colors.append("Красный")
        elif self.ui.rb2_green.isChecked(): colors.append("Зелёный")
        elif self.ui.rb2_white.isChecked(): colors.append("Белый")
        
        
        if self.ui.rb3_red.isChecked(): colors.append("Красный")
        elif self.ui.rb3_green.isChecked(): colors.append("Зелёный")
        elif self.ui.rb3_white.isChecked(): colors.append("Белый")
        
        result_text = ", ".join(colors)
        
        
        self.ui.label_result.setText(result_text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FlagApp()
    window.show()
    sys.exit(app.exec())