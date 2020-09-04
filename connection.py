import mysql.connector


class db:
    def __init__(self):
        self.connecti = mysql.connector.connect(user="root", port=3306, host="localhost", password="", database="hotel_management")
        self.cursori = self.connecti.cursor()

    def uid(self, qry, values):
        self.cursori.execute(qry, values)
        self.connecti.commit()

    def show(self, qry):
        self.cursori.execute(qry)
        info = self.cursori.fetchall()
        return info

d=db()
print(d.connecti)

