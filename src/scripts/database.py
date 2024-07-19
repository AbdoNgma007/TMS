import sqlite3
import os


class DB:

    def __init__(self):
        self.createTable("train")
        self.createTable("ticket")
        self.createTable("report_problem")
        self.createTable("report_solve")
        self.createTable("employee")
        self.createTable("company")


    def __path__(self):
        path = os.path.dirname(os.path.abspath(__file__))
        return path

    def __connect(self):
        filedatabase = os.path.join(self.__path__(), "database.db")
        connect = sqlite3.connect(filedatabase, timeout=60)
        cursor = connect.cursor()
        return connect, cursor

    def createTable(self, name_script: str):
        connect, cursor = self.__connect()
        script = os.path.join(self.__path__(), f"tables\\{name_script}.sql")
        file = open(script, 'r')
        sql = file.read()
        file.close()
        cursor.executescript( sql )
        cursor.close()
        connect.close()

    def insert(self, table: str, data: tuple | list) -> str:
        connect, cursor = self.__connect()
        script = os.path.join(self.__path__(), f"insert\\{table}.sql")
        file = open(script, 'r')
        sql = file.read()
        file.close()
        print(data, table)
        try:
            cursor.executemany( sql, (data, ) )
        except sqlite3.IntegrityError:
            cursor.close()
            connect.close()
            return "unique"
        connect.commit()
        cursor.close()
        connect.close()
        return "inserted :)"

    def select(self, table: str):
        connect, cursor = self.__connect()
        script = os.path.join(self.__path__(), f"select\\{table}.sql")
        file = open(script, 'r')
        sql = file.read()
        file.close()
        cursor.execute( sql )
        data = cursor.fetchall()
        cursor.close()
        connect.close()
        return data

    def customSelect(self, sql: str):
        connect, cursor = self.__connect()
        cursor.execute( sql )
        data = cursor.fetchall()
        cursor.close()
        connect.close()
        return data

    def update(self, table: str, data: tuple | list):
        connect, cursor = self.__connect()
        script = os.path.join(self.__path__(), f"update\\{table}.sql")
        file = open(script, 'r')
        sql = file.read()
        file.close()
        cursor.executemany( sql, (data, ) )
        connect.commit()
        cursor.close()
        connect.close()

    def delete(self, table: str, data: tuple | list):
        connect, cursor = self.__connect()
        script = os.path.join(self.__path__(), f"delete\\{table}.sql")
        file = open(script, 'r')
        sql = file.read()
        file.close()
        cursor.executemany( sql, (data, ) )
        connect.commit()
        cursor.close()
        connect.close()
