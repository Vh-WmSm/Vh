import pymysql

class DataBase:
    def __init__(self, host):
        self.conn = pymysql.connect(host=host, port=3306, user='root', password='1234', database='db1',
                               charset='utf8')
        self.cursor = self.conn.cursor()
    def insert(self, tb_title, data, data_num, field_alias=''):
        sql = f'insert into {tb_title}({field_alias}) values('
        for i in range(data_num - 1):
            sql += '%s,'
        sql += '%s);'
        self.cursor.execute(sql, data)
    def insert_staff(self, data):
        sql = f'insert into tb_staff values(%s, default)'
        self.cursor.execute(sql, data)
    def select_tb_project_admin(self, project_admin_name):
        sql = 'select * from tb_project_admin where project_admin_name = "{}"'.format(project_admin_name)
        self.cursor.execute(sql)
        # 该项目经理不存在
        if self.cursor.fetchone() is None:
            return 1
        # 该项目经理已存在
        else:
            return 0
    def select_tb_staff(self, staff_name):
        sql = 'select * from tb_staff where staff_name = "{}"'.format(staff_name)
        self.cursor.execute(sql)
        if self.cursor.fetchone() is None:
            return 1
        else:
            return 0
    def create_staff_if_not_exists(self):
        sql = f'''
        CREATE TABLE IF NOT EXISTS tb_staff(
            staff_name VARCHAR(8) NOT NULL, -- 员工姓名
            staff_password VARCHAR(30) DEFAULT '123'); -- 员工密码
                    '''
        self.cursor.execute(sql)
    def create_task_table_if_not_exists(self, tb_title):
        sql = f'''create table if not exists {tb_title}(
                        task_project_name VARCHAR(50) NOT NULL, -- 项目名称
                        task_project_admin_name VARCHAR(8), -- 该项目所属项目经理
                        task_description VARCHAR(100) , -- 结果定义
                        task_principal_name VARCHAR(8) ); -- 项目负责人
                        '''
        self.cursor.execute(sql)
    def create_project_admin_table_if_not_exists(self):
        sql = f'''CREATE TABLE tb_project_admin(
	                project_admin_name VARCHAR(8) NOT NULL); -- 项目经理姓名
                    '''
        self.cursor.execute(sql)
    def drop_table_if_exists(self, tb_title):
        sql = f'drop table if exists {tb_title}'
        self.cursor.execute(sql)

    def commit_and_close(self):
        self.conn.commit()
        self.conn.close()