from app import app
import MySQLdb
from flask import render_template

conn = MySQLdb.connect(host="localhost",
                    user = "root",
                    passwd = "rollins",
                    db = "tarveltparking")
cur = conn.cursor()


@app.route('/')
@app.route('/index')
def index():
    cur.execute("SELECT COUNT(*) FROM floor_one WHERE spot_avail = 1")
    data = cur.fetchall()
    return render_template('index.html', data = data[0][0])


if __name__ == '__main__':
    app.run(debug=True)


