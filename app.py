# pip install PySide6
from PySide6.QtWidgets import (
    QWidget,
    QStackedWidget,
    QVBoxLayout,
    QApplication
)

import sys

from FRAMES import PartnersCardFrame

from DATABASE import Database

from PartnerStatic import Partner

from SendMessageBox import *

# главный класс
class MainApplicationClass(QWidget):
    def __init__(self):

        QWidget.__init__(self)

        self.setWindowTitle("Главное окно")
        self.resize(800, 600)

        self.db = Database.Database()

        self.frames_container = QStackedWidget()

        # открытие окна карточек партнеров
        partner_cards_frame = PartnersCardFrame.PartnerCardsClass(self)
        self.frames_container.addWidget(partner_cards_frame)

        layout = QVBoxLayout(self)
        layout.addWidget(
            self.frames_container)


    # поменять фрейм
    def switch_frames(self, need_frame_name, partner_name=None):
        if partner_name:
            Partner.set_name(partner_name)
        goal_frame = need_frame_name(self)
        self.frames_container.removeWidget(goal_frame)
        self.frames_container.addWidget(goal_frame)
        self.frames_container.setCurrentWidget(goal_frame)


# #67BA80 - Акцентирование внимания
# #F4E8D3 - Дополнительный фон
# #FFFFFF - Основной фон
# Segoe UI - Шрифт
styles_sheet = '''
QPushButton {
background: #67BA80;
color: #000000;
}

QLineEdit {
font-size: 15px;
}


#Title {
font-size: 30px;
qproperty-alignment: AlignCenter;
}

#Hint_label {
font-size: 18px;
padding: 10px, 0px, 0px, 0px;
font-weight: bold;
}

#Main_label {
font-size: 15px;
}

#Card_label {
font-size: 15px;
}

#Card {
border: 2px solid black;
}

#Top_lvl_label {
font-size: 30px;
}

'''

# запуск приложения
application = QApplication(sys.argv)
application.setStyleSheet(styles_sheet)
main_class_object = MainApplicationClass()
main_class_object.show()
application.exec()
