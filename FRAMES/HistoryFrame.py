from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QTreeWidget,
    QTreeWidgetItem,
    QLineEdit,
    QFrame
)

import PartnerStatic
from DATABASE import Database

from SendMessageBox import *

from FRAMES import PartnerInfoFrame



class HistoryClass(QFrame):
    def __init__(self, main_class_controller):
        QFrame.__init__(self)
        self.controller = main_class_controller
        self.db: Database.Database = main_class_controller.db

        self.main_frame_layout = QVBoxLayout(self)
        self.setup_ui()

    def setup_ui(self):
        title_label = QLabel("Добавление партнера")
        title_label.setObjectName("Title")
        self.main_frame_layout.addWidget(title_label)

        # Создание таблицы
        table = QTreeWidget()
        table.setHeaderLabels(['Продукция', 'Партнер', 'Количество продукции', 'Дата'])
        self.main_frame_layout.addWidget(table)

        for data in self.db.take_sales_info(PartnerStatic.Partner.get_name()):
            item = QTreeWidgetItem(table)
            item.setText(0, data['product'])
            item.setText(1, data['partner'])
            item.setText(2, str(data['count'])) # Перевод из int в str
            item.setText(3, str(data['date'])) # Перевод из date в str


        back_btn = QPushButton("Назад")
        back_btn.clicked.connect(
            lambda : self.controller.switch_frames(PartnerInfoFrame.PartnerInfoClass)
        )
        self.main_frame_layout.addWidget(back_btn)



