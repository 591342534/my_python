
'my sqlite module demo'
_author = 'dai'

global _dbfile
_dbfile = "test.db"
global _conn
global _cursor

_conn = None
_cursor = None

import os, sys, shutil
import sqlite3

# create database name; 
# use databasename; 
def con_db(filename):
    bRet = False
    global _dbfile
    _dbfile = filename
    try:
        global _conn
        _conn = sqlite3.connect(_dbfile)
        global _cursor
        _cursor = _conn.cursor()
        bRet = True
    except Exception as e:
        print("except:", e)
    return bRet

# 备份数据文件名
def bakup_db(old_filename, new_filename):
    bRet = False
    try:
        shutil.copy(old_filename, new_filename)
        bRet = True
    except Exception as e:
        print("except:", e)
    return bRet

    
# 重命名数据文件名
def rename_db(old_filename, new_filename):
    bRet = False
    try:
        os.rename(old_filename, new_filename)
        bRet = True
    except Exception as e:
        print("except:", e)
    return bRet

# drop database name
def drop_db(filename):
    bRet = False
    try:
        os.remove(filename)
        bRet = True
    except Exception as e:
        print("except:", e)
    return bRet

# show tables;
def show_tables(filename):    
    table_list = []
    try:
        global _conn
        global _cursor
        # select name from sqlite_master where type='table' order by name;
        _cursor = _conn.cursor()
        sql = "select * from sqlite_master"
        _cursor.execute(sql)
        result_excute = _cursor.fetchall()
        for item in result_excute:
            table_list.append(item)
        bRet = True
    except Exception as e:
        print("except:", e)
    return table_list

# describe tablename; 
def des_table_att(filename, table_name):
    table_dict = {}
    try:
        bRet = True
    except Exception as e:
        print("except:", e)
    return table_dict

# create table table_name (字段1 数据类型 , 字段2 数据类型);
def create_table(filename, table_name, **kwargs):
    bRet = False
    try:
        
        bRet = True
    except Exception as e:
        print("except:", e)
    return bRet

# 改表的名字 
# alter table table_name rename to new_table_name;
def alter_tablename(filename, old_table_name, new_table_name):
    bRet = False
    try:
        
        bRet = True
    except Exception as e:
        print("except:", e)
    return bRet

# Insert into 表名 [(字段1 , 字段2 , ….)] values (值1 , 值2 , …..); 
def insert_data(filename, table_name, values_dict):
    bRet_list = []
    try:
        pass
    except Exception as e:
        print("except:", e)
    return bRet_list

# select 字段1 , 字段2 from table_name; 
def select_data(filename, table_name, sql_text):
    bRet_list = []
    try:
        
        bRet = True
    except Exception as e:
        print("except:", e)
    return bRet_list

# Update table_name set 字段名=’新值’ [, 字段2 =’新值’ , …..][where id=id_num] [order by 字段 顺序] 
def update_data(filename, table_name, values_dict):
    bRet_list = []
    try:
        
        bRet = True
    except Exception as e:
        print("except:", e)
    return bRet_list

# delete from table_name where 条件语句 ; 条件语句如 : id=3; 
def delete_data(filename, table_name, sql_text):
    bRet_list = []
    try:
        
        bRet = True
    except Exception as e:
        print("except:", e)
    return bRet_list

# 删除表，之后表不再存在
def drop_table(filename, table_name):
    bRet = False
    try:
        
        bRet = True
    except Exception as e:
        print("except:", e)
    return bRet

# 清空表，之后表依然存在
# 一次性清空表中的所有数据 
# truncate table table_name; 此方法也会使表中的取号器(ID)从1开始 
def clear_table(filename, table_name):
    bRet = False
    try:
        
        bRet = True
    except Exception as e:
        print("except:", e)
    return bRet

# 增加一个字段格式
# alter table table_name add column (字段名 字段类型); ----此方法带括号
def add_column(filename, table_name, colunm_name):
    bRet = False
    try:
        
        bRet = True
    except Exception as e:
        print("except:", e)
    return bRet

# 指定字段插入的位置： 
# alter table table_name add column 字段名 字段类型 after 某字段
def insert_column(filename, table_name, colunm_name):
    bRet = False
    try:
        
        bRet = True
    except Exception as e:
        print("except:", e)
    return bRet

# 删除一个字段： 
def delete_column(filename, table_name, colunm_name):
    bRet = False
    try:
        
        bRet = True
    except Exception as e:
        print("except:", e)
    return bRet
    
# 修改字段名称/类型 ： 
# alter table table_name change 旧字段名 新字段名 新字段的类型; 
def delete_column(filename, table_name, colunm_name):
    bRet = False
    try:
        
        bRet = True
    except Exception as e:
        print("except:", e)
    return bRet

# 判断表是否存在
def is_exist_table(filename, table_name):
    bRet = False
    try:
        # select count(*)  from sqlite_master wheretype='table' and name = 'yourtablename';
        bRet = True
    except Exception as e:
        print("except:", e)
    return bRet
    
# 判断表中某列是否存在
def is_exist_colunm(filename, table_name, colunm_name):
    bRet = False
    try:
        
        bRet = True
    except Exception as e:
        print("except:", e)
    return bRet

# 关闭连接数据库
def close_db(filename):
    bRet = False
    try:
        
        bRet = True
    except Exception as e:
        print("except:", e)
    return bRet


def main():
    print("begin main")
    args = sys.argv
    if len(args) == 1:
        print("hello world!")
    elif len(args)==2:        
        global _dbfile
        print("conn db file: ", con_db(_dbfile))
        print("bakup db file: ", bakup_db(_dbfile, "123.db"))
        print("rename db file: ", rename_db("123.db", "test_bak.db"))
        print("drop db file: ", drop_db("test_bak.db"))
        print("show tables: ", show_tables(_dbfile))
    else:
        print("too many arguments!")
    print("end main")

if __name__ == '__main__':
    main()