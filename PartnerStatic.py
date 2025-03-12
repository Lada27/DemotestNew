class Partner:
    name = None

    @staticmethod
    def get_name():
        # Возврат имени партнера по запросу
        return Partner.name

    @staticmethod
    def set_name(new_name: str):
        # Запись нового имени, с которым будет вестись работа
        Partner.name = new_name
