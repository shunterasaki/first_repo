import sqlite3


conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()

schema = "select * from sqlite_schema"
table_list = "select name from sqlite_master where type = 'table'"

select_all_product = "select * from mamazon_product"

c.execute(select_all_product)
for r in c:
    print(r)


conn.close()
