import os
import psycopg2
from flask import Flask, render_template

app = Flask(__name__)

def db_connection():
    connection = psycopg2.connect(user='postgres',
                                  password = 'Bravo005',
                                  host = '127.0.0.1',
                                  port='5432')
    return connection

@app.route('/')
def index():
    conn = db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * From Name")
    out = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', out=out)
@app.route('/tovar/')
def tovar():
    conn = db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * From tovar")
    out = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('tovar.html', out=out)
@app.route('/orders/')
def order():
    conn = db_connection()
    cur = conn.cursor()
    cur.execute("""select orders.id, orders.colvo, name.name, tovar.name, orders.colvo * tovar.price as totalsum from orders, tovar, name
                where orders.tovar_id = tovar.id
                and orders.name_id = name.id""")
    out = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('orders.html', out=out)
if __name__ == '__main__':
    app.run()