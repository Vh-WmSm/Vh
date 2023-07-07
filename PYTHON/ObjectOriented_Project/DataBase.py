import pymysql


class DataBase:
    def __init__(self, host):
        self.conn = pymysql.connect(host=host, port=3306, user='root', password='1234', database='db1',
                                    charset='utf8')
        self.cursor = self.conn.cursor()

    def insert(self, tb_title, data, data_num, field_alias='', first_id=False):
        sql = f'insert into {tb_title}({field_alias}) values('
        if first_id is True:
            sql += 'default,'
        for i in range(data_num - 1):
            sql += '%s,'
        sql += '%s);'
        self.cursor.execute(sql, data)

    def insert_staff(self, data):
        # 未传入staff_role_id则默认值为1（普通员工）
        if len(data) == 1:
            sql = f'insert into tb_staff values(default, %s, default, default)'
        else:
            sql = f'insert into tb_staff values(default, %s, default, %s)'
        self.cursor.execute(sql, data)

    def select_tb_staff_by_name(self, staff_name):
        sql = f'select staff_name from tb_staff where staff_name = "{staff_name}"'
        self.cursor.execute(sql)
        # 员工不存在，可以插入
        if self.cursor.fetchone() is None:
            return False
        return True

    def create_staff_if_not_exists(self):
        sql = f'''CREATE TABLE IF NOT EXISTS tb_staff(
                staff_id integer primary key auto_increment, -- 员工id
                staff_name VARCHAR(8) NOT NULL, -- 员工姓名
                staff_password VARCHAR(30) DEFAULT '000000', -- 员工密码
                staff_role INT DEFAULT 1); -- 员工角色
                    '''
        self.cursor.execute(sql)

    def create_task_table_if_not_exists(self, tb_title):
        sql = f'''create table if not exists {tb_title}(
                        task_id integer primary key auto_increment, -- 任务id
                        task_project_name VARCHAR(50) NOT NULL, -- 项目名称
                        task_project_admin_name VARCHAR(8), -- 该项目所属项目经理
                        task_description VARCHAR(100) , -- 结果定义
                        task_principal_name VARCHAR(8) ); -- 项目负责人
                        '''
        self.cursor.execute(sql)

    def drop_table_if_exists(self, tb_title):
        sql = f'drop table if exists {tb_title}'
        self.cursor.execute(sql)

    def commit(self):
        self.conn.commit()

    def close(self):
        self.conn.close()
