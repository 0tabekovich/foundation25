import mysql.connector as my
class notebooks:
    def __init__(self,database_name):
        self.Con=my.connect(host='localhost',password='root',user='root')
        sql=f"Create database if not exists {database_name}"
        self.Con.cursor().execute(sql)
        self.Con.cursor().execute(f"Use {database_name}")
        self.Con.commit()
    def create_table(self,table):
        self.table_name=table
        sql=f"Create table if not exists {table}(id int auto_increment primary key,model varchar(128),cpu varchar(64),frequency float,ram int ,gpu int, price float);"
        self.Con.cursor().execute(sql)
        self.Con.commit()
    def insert_into(self,ls,table):
        value=""
        for x in ls:
            for y in x:
                value+='%s,'
            break
        sql = f"Insert into {table}(model,cpu,frequency,ram,gpu,price) values({value[0:len(value)-1]});"
        for x in ls:
            self.Con.cursor().execute(sql,x)
            self.Con.commit()
    def select(self,table):
    # ram 8 dan katta va gpu 2 bolgan noutbooklar
        sql=f'select * from {table} where ram>2 and gpu = 8; '
        self.Con.cursor().execute(sql)
        for x in self.Con.cursor() :
            print(x)
    #


n=notebooks("Notebook")
n.create_table("note")
ls=[('HP','Core i9',4.2,64,8,12000000),('Macbook','M 12',1.3,4,8,6700000),('HP','Core i9',4.2,64,8,12000000)]
n.insert_into(ls,'note')
n.select('note')