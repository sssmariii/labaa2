import sys
import random
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTimer

from ui_task4 import Ui_MainWindow

class PseudoNimApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.total_stones = 0
        self.user_turn = True
        
        # Изначально кнопка "Взять" выключена, пока игра не начата
        self.ui.btn_take.setEnabled(False)
        
        # Подключение кнопки
        self.ui.btn_start.clicked.connect(self.start_game)
        self.ui.btn_take.clicked.connect(self.user_move)

    def start_game(self):
        # начальное количество камней
        self.total_stones = self.ui.spinBox_N.value()
        
        
        self.ui.textEdit_log.clear()
        self.ui.spinBox_N.setEnabled(False)
        self.ui.btn_start.setEnabled(False)
        self.ui.btn_take.setEnabled(True)
        self.user_turn = True
        
        self.update_display()
        self.log_message(f"Игра началась! В куче {self.total_stones} камней.")
        self.log_message("Ваш ход. Возьмите от 1 до 3 камней.")

    def user_move(self):
        if not self.user_turn:
            return
            
        take = self.ui.spinBox_take.value()
        
        # Проверка на ошибочные значения 
        if take > self.total_stones:
            self.log_message(f"Ошибка: нельзя взять {take} камней, в куче только {self.total_stones}.")
            return
            
        # Ход пользователя
        self.total_stones -= take
        self.log_message(f"Вы взяли: {take}. Осталось: {self.total_stones}")
        self.update_display()
        
        # Проверка на победу
        if self.total_stones == 0:
            self.end_game("Вы победили!")
            return
            
        
        self.user_turn = False
        self.ui.btn_take.setEnabled(False)
        self.log_message("Ход компьютера...")
        
        
        QTimer.singleShot(1000, self.ai_move)

    def ai_move(self):
        if self.total_stones == 0:
            return
            
        # СТРАТЕГИЯ ИИ: Выигрывает всегда, когда возможно.
        # Секрет: нужно оставлять противнику количество камней, кратное 4.
        # Если currently камней не кратно 4, ИИ берет столько, чтобы остаток стал кратен 4.
        # Если уже кратно 4, ИИ проигрывает при идеальной игре противника, поэтому берет случайно.
        
        remainder = self.total_stones % 4
        
        if remainder != 0:
            take = remainder  
        else:
        
            take = random.randint(1, min(3, self.total_stones))
            
        self.total_stones -= take
        self.log_message(f"Компьютер взял: {take}. Осталось: {self.total_stones}")
        self.update_display()
        
        if self.total_stones == 0:
            self.end_game("Компьютер победил!")
            return
            
        self.user_turn = True
        self.ui.btn_take.setEnabled(True)
        self.log_message("Ваш ход.")

    def update_display(self):
        self.ui.label_remaining.setText(f"Осталось камней: {self.total_stones}")

    def log_message(self, text):
        self.ui.textEdit_log.append(text)

    def end_game(self, winner_text):
        self.log_message(f"--- ИГРА ОКОНЧЕНА ---")
        self.log_message(winner_text)
        self.ui.btn_take.setEnabled(False)
        self.ui.spinBox_N.setEnabled(True)
        self.ui.btn_start.setEnabled(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PseudoNimApp()
    window.show()
    sys.exit(app.exec())