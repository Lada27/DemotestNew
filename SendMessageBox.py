from PySide6.QtWidgets import (
    QMessageBox
)
# итформационное сообщение
def send_I_message(message_text: str):
    messageBox = QMessageBox()
    messageBox.setText(message_text)
    messageBox.setIcon(QMessageBox.Icon.Information)
    messageBox.setStandardButtons(QMessageBox.StandardButton.Yes)
    result = messageBox.exec()
    return result

# критическое сообщение
def send_C_message(message_text: str):
    # Создание объекта сообщение
    message = QMessageBox()
    message.setText(message_text)
    message.setIcon(QMessageBox.Icon.Critical)
    message.setStandardButtons(QMessageBox.StandardButton.Yes)
    user_result = message.exec()
    return user_result