from .config import Config
import pymysql


class Query:
    def __init__(self):
        connect = Config()
        self.db, self.cursor = connect.console()

    def run(self, query, params):
        try:
            resp = self.cursor.execute(query, params)
            self.db.commit()

            return self.cursor.lastrowid, resp
        except pymysql.MySQLError as err:
            print("error: ", err)

    def fetch(self, query, param):
        try:
            self.cursor.execute(query, param)
            rows = self.cursor.fetchall()
            return rows
        except ValueError as error:
            return error

    def selectall(self, query):
        try:
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            return rows
        except ValueError as error:
            return error

    def search(self, query):
        try:
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            return rows
        except ValueError as error:
            return error


    def update(self, query, param):
        try:
            resp = self.cursor.execute(query, param)
            self.db.commit()

            return resp
        except ValueError as error:
            return error

    def delete(self, query, param):
        try:
            resp = self.cursor.execute(query, param)
            self.db.commit()

            return resp
        except ValueError as error:
            return error