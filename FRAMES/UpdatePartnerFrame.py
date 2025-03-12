from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QScrollArea,
    QLabel,
    QPushButton,
    QComboBox,
    QLineEdit,
    QFrame
)

import PartnerStatic

from DATABASE import Database

from SendMessageBox import *

from FRAMES import PartnersCardFrame



class UpdatePartnerClass(QFrame):
    def __init__(self, main_class_controller):  #
        QFrame.__init__(self)
        self.controller = main_class_controller
        self.db: Database.Database = main_class_controller.db

        self.main_frame_layout = QVBoxLayout(self)
        self.setup_ui()

    def setup_ui(self):
        title_label = QLabel("Добавление партнера")
        title_label.setObjectName("Title")
        self.main_frame_layout.addWidget(title_label)

        partners_data = self.db.take_partner_info(PartnerStatic.Partner.get_name())

        # Создание полей для ввода и подсказок
        self.create_hint_label("Обновите Имя партнера")
        self.partner_name = self.create_edit_line(partners_data['name'], 100)

        self.create_hint_label("Обновите Телефон партнера")
        self.partner_phone = self.create_edit_line(partners_data['phone'], 13)
        self.partner_phone.setInputMask('+7 000 000 00 00') # Добавление маски для ввода

        self.create_hint_label("Обновите ИНН партнера")
        self.partner_inn = self.create_edit_line(partners_data['inn'], 10)

        self.create_hint_label("Обновите Юридический адрес партнера")
        self.partner_ur_addr = self.create_edit_line(partners_data['addr'], 300)

        self.create_hint_label("Обновите ФИО директора партнера")
        self.partner_dir = self.create_edit_line(partners_data['dir'], 100)

        self.create_hint_label("Обновите Рейтинг (от 1 до 10) партнера")
        self.partner_rate = self.create_edit_line(partners_data['rate'], 2)

        self.create_hint_label("Обновите Электронную почту партнера")
        self.partner_mail = self.create_edit_line(partners_data['mail'], 100)

        self.create_hint_label("Укажите тип партнера")
        self.partner_type = QComboBox()
        self.partner_type.addItems(["ООО", "ОАО", "ПАО", "ЗАО"])
        self.main_frame_layout.addWidget(self.partner_type)

        # Создание кнопки для добавления партнера в БД
        add_btn = QPushButton("Обновить партнера")
        add_btn.clicked.connect(self.add_partner)
        self.main_frame_layout.addWidget(add_btn)


        back_btn = QPushButton("Назад")
        back_btn.clicked.connect(
            lambda : self.controller.switch_frames(PartnersCardFrame.PartnerCardsClass)
        )
        self.main_frame_layout.addWidget(back_btn)

    def add_partner(self):

        partner_input_data: dict = {
            "type": self.partner_type.currentText(),
            "name": self.partner_name.text(),
            "dir": self.partner_dir.text(),
            "mail": self.partner_mail.text(),
            "phone": self.partner_phone.text()[3:], #
            "inn": self.partner_inn.text(),
            "rate": self.partner_rate.text()
        }

        if self.db.update_partner(partner_input_data, PartnerStatic.Partner.get_name()):
            send_I_message("Партнер Обновлен!")
            PartnerStatic.Partner.set_name(self.partner_name.text())
            return
        send_C_message("Ошибка Обновления!")
        return


    def create_hint_label(self, text: str):
        label = QLabel(text)
        label.setObjectName("Hint_label")

        self.main_frame_layout.addWidget(label)

    def create_edit_line(self, text: str, max_length: int):

        edit = QLineEdit()
        edit.setText(text)
        edit.setMaxLength(max_length)
        self.main_frame_layout.addWidget(edit)

        return edit
