import sqlite3
## Created by Abhiyantriki.in
## Cookies in python same as Browser's Cookie.

class Cookies:
    def __init__(self):
        connection = sqlite3.connect("cookies.db")
        self.cursor = connection.cursor()
        try:
            self.cursor.execute(f"CREATE TABLE Cookies (key TEXT, val TEXT );")
        except sqlite3.OperationalError:
            pass

    def set_item(self,key,value):
        val = self.get_item(key)
        if val:
            self.cursor.execute("UPDATE Cookies SET val = ? WHERE key = ?",(value,key))
        else:
            self.cursor.execute("INSERT INTO Cookies VALUES ( ?, ?)",(key,value))
        return value

    def get_item(self,key):
        rows = self.cursor.execute(f"SELECT val FROM Cookies where  key = ? ",(key,)).fetchall()
        return rows[0][0] if rows else None

    def delete_item(self,key):
        self.cursor.execute(
            "DELETE FROM Cookies WHERE key = ?",
            (key,)
        )

    def get_all(self):
        rows = self.cursor.execute(f"SELECT key,val FROM Cookies ").fetchall()
        return rows
      
