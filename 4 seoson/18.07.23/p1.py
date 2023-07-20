import mysql.connector as con
def baza_yaratish(database_name):
    Con=con.connect(user='root', host='localhost',password='root')
    cur=Con.cursor()
    sql=f"""Create database if not exists {database_name}"""
    cur.execute(sql)

def create_table(database_name,table_name):
    Con = con.connect(user='root', host='localhost', password='root', database=f"{database_name}")
    cur = Con.cursor()
    sql=f''' Create table if not exists {table_name}(id int ,name varchar(20),grand bool);'''
    cur.execute(sql)
    print("yaratildi")

def insert(database_name,table_name):
    Con = con.connect(user='root', host='localhost', password='root', database=f"{database_name}")
    cur = Con.cursor()
    sql=f'''Insert into {table_name} values(4,"Obid",False)'''
    cur.execute(sql)
    Con.commit()

def show_da(database_name,table_name):
    Con = con.connect(user='root', host='localhost', password='root', database=f"{database_name}")
    cur = Con.cursor()
    sql=f"select * from {table_name}"
    cur.execute(sql)
    res=cur.fetchall()
    for x in res:
        print(x)

baza_yaratish("market")
create_table('market','talaba')
show_da("market","talaba")
insert("market","talaba")