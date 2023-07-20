import mysql.connector as Con
class base():
    def __init__(self):
        con=Con.connect(host='localhost',password='root',user='root',database='milliy_taomlar')
        con.cursor().execute('use milliy_taomlar;')
        con.cursor().execute('select * from airoport;')
        for x in con.cursor().fetchall():
            print(x)

b=base()