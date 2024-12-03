import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

try:
    connection = psycopg2.connect(user='postgres',
                                  password = 'Bravo005',
                                  host = '127.0.0.1',
                                  port='5432')
    # connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connection.cursor()
    # sql_create_database = 'create database postgres_db'
    # cursor.execute(sql_create_database)
    
    # create_table_query = '''CREATE TABLE tovar
    #                         (ID INT PRIMARY KEY   NOT NULL,
    #                         Name                 TEXT   NOT NULL,
    #                         Price                REAL);'''
    
    # cursor.execute(create_table_query)
    # connection.commit()
    # print("Таблица создана")

    # insert_query = """ INSERT INTO tovar (ID, Name, Price) VALUES (1, 'Water', 50),
    #                                                                     (2, 'Bread', 100),
    #                                                                     (3, 'Milk', 200)"""

    # cursor.execute(insert_query)
    # connection.commit()
    # print('Запись вставлена')
    
    # create_table_query = '''CREATE TABLE Name
    #                         (ID INT PRIMARY KEY   NOT NULL,
    #                         name           TEXT   NOT NULL,
    #                         old             INT   NOT NULL);'''

    # create_table_query = '''CREATE TABLE Orders
    #                         (ID INT PRIMARY KEY   NOT NULL,
    #                         colvo           INT   NOT NULL,
    #                         tovar_id        INT REFERENCES tovar (ID),
    #                         name_id         INT REFERENCES Name (ID));'''
    
    # cursor.execute(create_table_query)
    # connection.commit()
    # print("Таблица создана")
    
    # insert_query = """ INSERT INTO Name (ID, name, old) VALUES  (1, 'Saha', 18),
    #                                                             (2, 'Egor', 19),
    #                                                             (3, 'Vika', 18)"""
    
    # cursor.execute(insert_query)
    # connection.commit()
    # print('Запись вставлена')
    
    # insert_query = """ INSERT INTO Orders (ID, colvo, tovar_id, name_id) 
    #                     VALUES  (1, 2, 1, 2),
    #                             (2, 3, 2, 1),
    #                             (3, 1, 3, 3)"""
    
    # cursor.execute(insert_query)
    # connection.commit()
    # print('Запись вставлена')

    # Мой запрос подтверждающий все связи
    # SELECT Name.name, Tovar.name, Orders.colvo, Tovar.price * Orders.colvo AS TotalSum From Orders, Name, Tovar 
    # Where Orders.tovar_id = Tovar.ID
    # and Orders.name_id = Name.ID;
   
    cursor.execute("SELECT Name.name, Tovar.name, Orders.colvo, Tovar.price * Orders.colvo AS TotalSum From Orders, Name, Tovar Where Orders.tovar_id = Tovar.ID and Orders.name_id = Name.ID;")
    record = cursor.fetchall()
    print("Результат", record)
    
    
    
except (Exception, Error) as error:
    print("Ошибка: ", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение закрыто")