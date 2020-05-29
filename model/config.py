import pymysql


class Config:
    def __init__(self):
        self.host = "localhost"
        self.username = "root"
        self.password = ""
        self.database = "db_inventory"

    def console(self):
        db = pymysql.connect(self.host, self.username, self.password, self.database)
        cur = db.cursor(pymysql.cursors.DictCursor)
        return db, cur
