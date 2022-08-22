import sqlite3
from sqlite3 import OperationalError

from config import RU


class ConnectionError(Exception):
    pass


class CredentialsError(Exception):
    pass


class SQLError(Exception):
    pass




class SQLighter:

    def __init__(self, database:str):
        """Подключаемся к БД и сохраняем курсор соединения"""
        self.connection = sqlite3.connect(database, check_same_thread=False)
        self.cursor = self.connection.cursor()
    
    def create_table(self):
        requests = [ 
            '''
                CREATE TABLE users (
                    id serial PRIMARY KEY,
                    username VARCHAR ( 255 ) UNIQUE NOT NULL,
                    user_id INT UNIQUE NOT NULL,
                    language INT DEFAULT 0
                )
            ''',
        ]
        try:
            for request in requests:
                self.cursor.execute(request)
        except OperationalError:
            pass

    def user_exists(self, user_id:int):
        """Проверяем, есть ли уже юзер в базе"""
        with self.connection:
            result = self.cursor.execute(
                'SELECT * FROM `users` WHERE `user_id` = ?', (user_id,)
                ).fetchall()
            return bool(len(result))

    def add_user(self, user_id:int, user_name:str, language:int=RU):
        """Добавляем нового пользователя"""
        with self.connection:
            return self.cursor.execute(
                "INSERT INTO `users` (`user_id`, `language`, 'username') VALUES(?,?,?)",
                (user_id, language, user_name))

    def switch_lang(self, user_id:int, language:int):
        return self.cursor.execute(
                "UPDATE `users` SET `language` = ? WHERE `user_id` = ?", 
                (language, user_id))

    def get_lang(self, user_id:int):
        lang = self.cursor.execute(
            'SELECT `language` FROM `users` WHERE `user_id` = ?', (user_id,)
            ).fetchall()
        return lang[0][0]

    def close(self):
        """Закрываем соединение с БД"""
        self.connection.close()


