import os, mysql.connector as con

os.system("cls")


class Student:
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
        sql=f'create table if not exists {table_name}(id int,name varchar(20),data_birth varchar(30),score int)'
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
#5-masala yechimi
    def update_score4toscore5(self,table_name):
        sql=f"update {table_name} set score=5  where data_birth like '%-12-%' or data_birth like '%-01-%' or data_birth like '%-02-%' and score=4"
        self.cur.execute(sql)
        self.Con.commit()
#2-masala yechimi
    def update_qishoyidatugilgan_and_score2(self,table_name):
        sql = f"delete from {table_name} where score=2"
        self.cur.execute(sql)
        self.Con.commit()
        sql=f"select * from {table_name} where data_birth like '%-12-%' or data_birth like '%-01-%' or data_birth like '%-02-%'"
        self.cur.execute(sql)
        for x in self.cur:
            print(x)
        self.Con.commit()
#4-masala yechimi
    def update_score4andfevral(self,table_name):
        sql = f"update {table_name} set score=5 where data_birth like '%-02-%' and score=4"
        self.cur.execute(sql)
        self.Con.commit()

    def show_info(self,table_name):
        sql=f'select distinct  id,name,data_birth,score from {table_name}'
        self.cur.execute(sql)
        for x in self.cur:
            print(x)
ls=[
    (1,'Abdulla',"25-01-2000",4),
    (2,'Nodira','22-05-1998',5),
    (3,'Shoxrux','20-07-1999',3),
    (4,'Hilola','21-12-2001',4),
    (5,'Jalil','18-09-1997',5),
    (6,'Temur','23-02-2002',4),
    (7,'Sardor','20-06-1996',3),
    (8,'Botir','19-03-2004',2),
    (9,'Lola','24-08-2003',5),
    (10,'Maftuna','19-10-1995',2)
]
ls1=['id','name','data_birth','score']
t=Student('Institut')
t.create_table('talabalar')
t.insert_into(ls,'talabalar',ls1)
t.show_info('talabalar')
t.update_score4toscore5('talabalar')
t.update_qishoyidatugilgan_and_score2('talabalar')
t.show_info('talabalar')