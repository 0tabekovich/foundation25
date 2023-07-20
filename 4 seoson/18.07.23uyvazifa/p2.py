import os, mysql.connector as con

os.system("cls")


class Kompyuter:
    def __init__(self, database_name):
        self.Con = con.connect(
            user="root",
            host="localhost",
            password="root"
        )
        self.cur = self.Con.cursor()
        sql = f"""Create database if not exists {database_name} """
        self.cur.execute(sql)
        sql = f"use {database_name}"
        self.cur.execute(sql)
    def create_table(self,table_name):
        sql=f'create table if not exists {table_name}(id int,modeli varchar(20),tarkibi varchar(50),narxi int)'
        self.cur.execute(sql)
        self.Con.commit()

    def insert_into(self,data,table_name,keys):
        val=""
        st=""
        for x in keys:
            val+='%s,'
            st+=f'{x},'
        sql=f'Insert into {table_name}({st[0:len(st)-1]}) Values({val[0:len(val)-1]})'
        print(sql)
        for x in data:
            self.cur.execute(sql,x)
        self.Con.commit()

    def show_info(self, table_name):
        sql = f'select * from {table_name}'
        self.cur.execute(sql)
        for x in self.cur:
            print(x)
    def select(self,table_name):
        sql = f"select * from {table_name} where tarkibi like '%videokarta%'"
        self.cur.execute(sql)
        for x in self.cur:
            print(x)
        self.Con.commit()

ls=[
    (1,'Asus',"videokarta,operativka,monitor,protsessor",4),
    (2,'Lenova',"operativka,monitor,protsessor",5),
    (3,'Asus',"videokarta,operativka,monitor,protsessor",3),
    (4,'Dell',"videokarta,monitor,protsessor",4),
    (5,'Acer',"videokarta,operativka,monitor,protsessor",5),
    (6,'Macbook',"videokarta,operativka,protsessor",4),
    (7,'MSS',"videokarta,operativka,monitor",3),
]
ls1=['id','modeli','tarkibi','narxi']
t=Kompyuter('Institut')
t.create_table('pc')
t.insert_into(ls,'pc',ls1)
t.show_info('pc')
t.select('pc')