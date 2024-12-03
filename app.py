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
    cur.execute("SELECT Name.name, Tovar.name, Orders.colvo, Tovar.price * Orders.colvo AS TotalSum From Orders, Name, Tovar Where Orders.tovar_id = Tovar.ID and Orders.name_id = Name.ID;")
    out = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', out=out)