import pymysql.cursors

# 链接mysql数据库

connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='demo1',charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

# 通过cursor创建游标
cursor = connection.cursor()

# 创建sql语句并执行
#sql = "INSERT into `demo` (`name`, `sex`, `class`) VALUES ('王大锤', 1, 1501)"
sql = "INSERT INTO `test` (`name`, `sex`, `class`, `remark`) VALUES ('王大锤6', '77', '1005', 'jhgj')"
cursor.execute(sql)

# 提交sql
connection.commit()

# 查询单条数据
sql1 = "select `id`, `name`, 'sex' from `test` where class=1002"
cursor.execute(sql1)
res1 = cursor.fetchone()
print(res1)

# 查询多条数据
sql2 = "select `id`, `name` from `test`"
cursor.execute(sql2)
res2 = cursor.fetchall()
# print(res2)
for val in res2:
    print(val)
