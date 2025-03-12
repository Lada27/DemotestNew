import psycopg2

from DATABASE import CONFIG

from CheckInputData import start_check


class Database():
    def __init__(self):
        self.connection_uri = self.connect_to_db()

    def connect_to_db(self):
        try:
            print('База данных -> Подключение')
            # Создание строки подключения
            connection = psycopg2.connect(
                user=CONFIG.USER,
                host=CONFIG.HOST,
                password=CONFIG.PASS,
                dbname=CONFIG.DBNAME
            )
            print('База данных -> Подключена')
            return connection
        except Exception as error:
            print(f':: {error}')
            return None

    def take_all_partners_info(self):

        try:
            query = '''
            SELECT *
            FROM partners_import;
            '''
            cursor = self.connection_uri.cursor()
            cursor.execute(query)

            partners_data = []
            for return_row in cursor.fetchall():
                partners_data.append(
                    {
                        'type': return_row[0].strip(),
                        'name': return_row[1].strip(),
                        'dir': return_row[2].strip(),
                        'mail': return_row[3].strip(),
                        'phone': return_row[4].strip(),
                        'addr': return_row[5].strip(),
                        'inn': return_row[6].strip(),
                        'rate': return_row[7].strip()
                    }
                )
            # Возврат данных
            return partners_data
        except Exception as error:
            print(f':: {error}')
            return []

    def take_count_of_sales(self, partner_name: str):

        try:
            query = f'''
            SELECT SUM(product_count)
            FROM partner_products_import
            WHERE partner_name = '{partner_name}';
            '''
            cursor = self.connection_uri.cursor()
            cursor.execute(query)
            count = cursor.fetchone()
            cursor.close()
            if count:
                return count[0]
            return None
        except Exception as error:
            print(f'::^ {error}')
            return None

    def add_new_partner(self, partner_data: dict):

        try:
            if not start_check(partner_data):
                return False

            query = f'''
            INSERT INTO partners_import
            VALUES (
            '{partner_data['type']}', 
            '{partner_data['name']}', 
            '{partner_data['dir']}', 
            '{partner_data['mail']}', 
            '{partner_data['phone']}', 
            '{partner_data['addr']}', 
            '{partner_data['inn']}', 
            '{partner_data['rate']}');
            '''

            cursor = self.connection_uri.cursor()
            cursor.execute(query)
            self.connection_uri.commit()
            cursor.close()
            return True
        except Exception as error:
            print(f'::^ {error}')
            return False

    def take_partner_info(self, partner_name: str):

        try:
            query = f'''
            SELECT *
            FROM partners_import
            WHERE partner_name = '{partner_name}';
            '''
            cursor = self.connection_uri.cursor()
            cursor.execute(query)
            partners_data = dict()
            for data in cursor.fetchall():
                partners_data = {
                    'type': data[0].strip(),
                    'name': data[1].strip(),
                    'dir': data[2].strip(),
                    'mail': data[3].strip(),
                    'phone': data[4].strip(),
                    'addr': data[5].strip(),
                    'inn': data[6].strip(),
                    'rate': data[7].strip()
                }
            cursor.close()
            return partners_data
        except Exception as error:
            print(f':: {error}')
            return dict()

    def update_partner(self, partner_data: dict, partner_name: str):

        try:
            if not start_check(partner_data):
                return False

            query = f'''
            UPDATE partners_import
            SET 
            partner_type = '{partner_data['type']}', 
            partner_name = '{partner_data['name']}', 
            partner_dir = '{partner_data['dir']}', 
            partner_mail = '{partner_data['mail']}', 
            partner_phone = '{partner_data['phone']}', 
            partner_addr = '{partner_data['addr']}', 
            partner_inn = '{partner_data['inn']}', 
            partner_rate = '{partner_data['rate']}'
            
            WHERE partner_name = '{partner_name}';
            '''

            cursor = self.connection_uri.cursor()
            cursor.execute(query)
            self.connection_uri.commit()
            cursor.close()
            return True
        except Exception as error:
            print(f'::^ {error}')
            return False


    def take_sales_info(self, partner_name: str):

        try:
            query = f'''
                    SELECT *
                    FROM partner_products_import
                    WHERE partner_name = '{partner_name}';
                    '''
            cursor = self.connection_uri.cursor()
            cursor.execute(query)
            partners_data = []
            for data in cursor.fetchall():
                partners_data.append(
                    {
                        'product': data[0].strip(),
                        'partner': data[1].strip(),
                        'count': data[2],
                        'date': data[3],
                    }
                )

            cursor.close()
            return partners_data
        except Exception as error:
            print(f':: {error}')
            return []