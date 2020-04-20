from flask import Flask, render_template, request, redirect
from flaskext.mysql import MySQL

app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'mypass'
app.config['MYSQL_DATABASE_DB'] = 'botdata'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql = MySQL()
mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()

#endpoint for search
@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == "POST":
        account = request.form['account']
        
        cursor.execute("SELECT d_from, label from data WHERE d_from LIKE %s ",(account) )
        conn.commit()
        data = cursor.fetchall()
        # all in the search box will return all the tuples
        if len(account) == 0 and account == 'all': 
            cursor.execute("SELECT d_from, label from data")
            conn.commit()
            data = cursor.fetchall()
        return render_template('search.html', data=data)
    return render_template('search.html')
if __name__ == '__main__':
    app.debug = True
    app.run()